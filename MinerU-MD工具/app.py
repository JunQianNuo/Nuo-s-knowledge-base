#!/usr/bin/env python3
"""MinerU 转 MD 桌面工具 — 支持拖拽文件和选择文件夹。

运行:
    python app.py

依赖:
    pip install PySide6 requests pypdfium2
"""
from __future__ import annotations

import json
import sys
from pathlib import Path

try:
    from PySide6.QtCore import QThread, Signal, Qt, QUrl
    from PySide6.QtWidgets import (
        QApplication,
        QCheckBox,
        QComboBox,
        QDialog,
        QDialogButtonBox,
        QFileDialog,
        QFormLayout,
        QHBoxLayout,
        QLabel,
        QLineEdit,
        QListWidget,
        QListWidgetItem,
        QMainWindow,
        QPlainTextEdit,
        QProgressBar,
        QPushButton,
        QVBoxLayout,
        QWidget,
    )
except ImportError:
    print("缺少 PySide6，请先安装：")
    print("    pip install PySide6 requests pypdfium2")
    sys.exit(1)

from converter import Converter, collect_files

if getattr(sys, "frozen", False):
    APP_DIR = Path(sys.executable).resolve().parent
else:
    APP_DIR = Path(__file__).resolve().parent


class DropListWidget(QListWidget):
    """支持拖拽文件和文件夹的列表。"""

    files_dropped = Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setSelectionMode(QListWidget.SelectionMode.ExtendedSelection)

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            super().dragEnterEvent(event)

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            super().dragMoveEvent(event)

    def dropEvent(self, event):
        urls = event.mimeData().urls()
        paths = [u.toLocalFile() for u in urls if u.isLocalFile()]
        if paths:
            self.files_dropped.emit(paths)
            event.acceptProposedAction()


class ConvertWorker(QThread):
    log = Signal(str)
    progress = Signal(int)
    finished_all = Signal(dict)

    def __init__(self, paths, output_dir, method, subject, add_frontmatter, postprocess, config):
        super().__init__()
        self.paths = paths
        self.output_dir = output_dir
        self.method = method
        self.subject = subject
        self.add_frontmatter = add_frontmatter
        self.postprocess = postprocess
        self.config = config

    def run(self):
        converter = Converter(
            config=self.config,
            log_callback=self.log.emit,
            progress_callback=self.progress.emit,
        )
        result = converter.convert_files(
            self.paths,
            self.output_dir,
            method=self.method,
            subject=self.subject,
            add_frontmatter=self.add_frontmatter,
            postprocess=self.postprocess,
        )
        self.finished_all.emit(result)


class SettingsDialog(QDialog):
    """设置对话框：可调整 MinerU 云 API、本地 MinerU、OCR 等配置。"""

    def __init__(self, config: dict, parent=None):
        super().__init__(parent)
        self.setWindowTitle("设置")
        self.resize(560, 520)
        self.result_config = dict(config)

        root = QVBoxLayout(self)
        form = QFormLayout()

        self.api_token_edit = QLineEdit(config.get("mineru_api_token", ""))
        self.api_token_edit.setPlaceholderText("MinerU 云 API Token")
        form.addRow("云 API Token", self.api_token_edit)

        self.api_url_edit = QLineEdit(config.get("mineru_api_url", "https://mineru.net/api/v4"))
        form.addRow("云 API URL", self.api_url_edit)

        self.model_version_edit = QLineEdit(config.get("mineru_model_version", "vlm"))
        self.model_version_edit.setPlaceholderText("vlm / auto / 其他支持的模型版本")
        form.addRow("模型版本", self.model_version_edit)

        self.mineru_cmd_edit = QLineEdit(config.get("mineru_command", "mineru"))
        form.addRow("本地 mineru 命令", self.mineru_cmd_edit)

        self.backend_combo = QComboBox()
        self.backend_combo.addItems([
            "pipeline",
            "vlm-auto-engine",
            "hybrid-auto-engine",
            "vlm-http-client",
            "hybrid-http-client",
        ])
        current_backend = config.get("mineru_backend", "pipeline")
        idx = self.backend_combo.findText(current_backend)
        self.backend_combo.setCurrentIndex(idx if idx >= 0 else 0)
        form.addRow("本地后端", self.backend_combo)

        self.lang_edit = QLineEdit(config.get("mineru_lang", "ch"))
        form.addRow("语言", self.lang_edit)

        self.tesseract_edit = QLineEdit(config.get("tesseract_path", r"C:\Program Files\Tesseract-OCR\tesseract.exe"))
        form.addRow("Tesseract 路径", self.tesseract_edit)

        self.pdftocairo_edit = QLineEdit(config.get("pdftocairo_command", "pdftocairo"))
        form.addRow("pdftocairo 命令", self.pdftocairo_edit)

        self.default_output_edit = QLineEdit(config.get("default_output_dir", ""))
        form.addRow("默认输出目录", self.default_output_edit)

        root.addLayout(form)

        btns = QDialogButtonBox(
            QDialogButtonBox.StandardButton.Save | QDialogButtonBox.StandardButton.Cancel
        )
        btns.accepted.connect(self.accept)
        btns.rejected.connect(self.reject)
        root.addWidget(btns)

    def accept(self):
        self.result_config = {
            "mineru_api_token": self.api_token_edit.text().strip(),
            "mineru_api_url": self.api_url_edit.text().strip(),
            "mineru_model_version": self.model_version_edit.text().strip() or "vlm",
            "mineru_command": self.mineru_cmd_edit.text().strip() or "mineru",
            "mineru_backend": self.backend_combo.currentText(),
            "mineru_lang": self.lang_edit.text().strip() or "ch",
            "tesseract_path": self.tesseract_edit.text().strip(),
            "pdftocairo_command": self.pdftocairo_edit.text().strip() or "pdftocairo",
            "default_output_dir": self.default_output_edit.text().strip(),
        }
        super().accept()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("MinerU 转 Markdown 工具")
        self.resize(820, 620)

        self.config = self._load_config()
        self.worker = None
        self._build_ui()

    # ---------- 界面 ----------
    def _build_ui(self):
        central = QWidget()
        root = QVBoxLayout(central)

        # 文件列表
        root.addWidget(QLabel("文件列表（可拖拽文件/文件夹到此处，或点击添加）"))
        self.file_list = DropListWidget()
        self.file_list.files_dropped.connect(self.add_paths)
        root.addWidget(self.file_list, stretch=3)

        # 添加/移除按钮
        btn_row = QHBoxLayout()
        add_files_btn = QPushButton("添加文件")
        add_folder_btn = QPushButton("选择文件夹")
        remove_btn = QPushButton("移除选中")
        clear_btn = QPushButton("清空")
        settings_btn = QPushButton("设置")
        add_files_btn.clicked.connect(self.choose_files)
        add_folder_btn.clicked.connect(self.choose_folder)
        remove_btn.clicked.connect(self.remove_selected)
        clear_btn.clicked.connect(self.file_list.clear)
        settings_btn.clicked.connect(self.open_settings)
        btn_row.addWidget(add_files_btn)
        btn_row.addWidget(add_folder_btn)
        btn_row.addWidget(remove_btn)
        btn_row.addWidget(clear_btn)
        btn_row.addWidget(settings_btn)
        btn_row.addStretch()
        root.addLayout(btn_row)

        # 输出目录
        out_row = QHBoxLayout()
        out_row.addWidget(QLabel("输出目录"))
        self.output_edit = QLineEdit(self.config.get("default_output_dir", ""))
        out_btn = QPushButton("选择...")
        out_btn.clicked.connect(self.choose_output_dir)
        out_row.addWidget(self.output_edit, stretch=1)
        out_row.addWidget(out_btn)
        root.addLayout(out_row)

        # 转换方式 + 课程名
        opt_row = QHBoxLayout()
        opt_row.addWidget(QLabel("转换方式"))
        self.method_combo = QComboBox()
        self.method_combo.addItem("自动（云API优先）", "auto")
        self.method_combo.addItem("MinerU 云 API", "cloud")
        self.method_combo.addItem("MinerU 本地", "local")
        self.method_combo.addItem("OCR 兜底", "ocr")
        opt_row.addWidget(self.method_combo)
        opt_row.addSpacing(12)
        opt_row.addWidget(QLabel("课程/主题"))
        self.subject_edit = QLineEdit()
        self.subject_edit.setPlaceholderText("例如：最优化方法")
        opt_row.addWidget(self.subject_edit, stretch=1)
        root.addLayout(opt_row)

        # 选项
        opt_row2 = QHBoxLayout()
        self.frontmatter_check = QCheckBox("自动添加 frontmatter")
        self.frontmatter_check.setChecked(True)
        self.postprocess_check = QCheckBox("转换后自动清理")
        self.postprocess_check.setChecked(True)
        opt_row2.addWidget(self.frontmatter_check)
        opt_row2.addWidget(self.postprocess_check)
        opt_row2.addStretch()
        root.addLayout(opt_row2)

        # 开始按钮 + 进度
        run_row = QHBoxLayout()
        self.start_btn = QPushButton("开始转换")
        self.start_btn.clicked.connect(self.start_convert)
        self.progress_bar = QProgressBar()
        self.progress_bar.setValue(0)
        run_row.addWidget(self.start_btn)
        run_row.addWidget(self.progress_bar, stretch=1)
        root.addLayout(run_row)

        # 日志
        root.addWidget(QLabel("日志"))
        self.log_view = QPlainTextEdit()
        self.log_view.setReadOnly(True)
        root.addWidget(self.log_view, stretch=2)

        self.setCentralWidget(central)

    # ---------- 文件操作 ----------
    def choose_files(self):
        files, _ = QFileDialog.getOpenFileNames(
            self,
            "选择要转换的文件",
            "",
            "支持的文件 (*.pdf *.pptx *.ppt *.docx *.doc *.xlsx *.xls *.html *.htm *.jpg *.jpeg *.png *.bmp *.tif *.tiff *.webp);;所有文件 (*.*)",
        )
        if files:
            self.add_paths(files)

    def choose_folder(self):
        folder = QFileDialog.getExistingDirectory(self, "选择文件夹（递归查找支持的格式）")
        if folder:
            self.add_paths([folder])

    def choose_output_dir(self):
        folder = QFileDialog.getExistingDirectory(self, "选择输出目录")
        if folder:
            self.output_edit.setText(folder)

    def open_settings(self):
        dlg = SettingsDialog(self.config, self)
        if dlg.exec():
            self.config = dlg.result_config
            self.output_edit.setText(self.config.get("default_output_dir", self.output_edit.text()))
            self._save_config()
            self.log("设置已保存。")

    def _save_config(self):
        config_path = APP_DIR / "config.json"
        with open(config_path, "w", encoding="utf-8") as f:
            json.dump(self.config, f, ensure_ascii=False, indent=2)

    def add_paths(self, paths):
        files = collect_files(paths)
        if not files:
            self.log("没有在拖入内容中找到支持的文件。")
            return
        existing = {self.file_list.item(i).data(Qt.ItemDataRole.UserRole) for i in range(self.file_list.count())}
        for f in files:
            if str(f) not in existing:
                item = QListWidgetItem(str(f))
                item.setData(Qt.ItemDataRole.UserRole, str(f))
                self.file_list.addItem(item)
                existing.add(str(f))
        self.log(f"已添加 {len(files)} 个文件，当前共 {self.file_list.count()} 个。")

    def remove_selected(self):
        for item in self.file_list.selectedItems():
            self.file_list.takeItem(self.file_list.row(item))

    # ---------- 转换 ----------
    def start_convert(self):
        if self.worker and self.worker.isRunning():
            self.log("正在转换中，请稍候。")
            return

        paths = [self.file_list.item(i).data(Qt.ItemDataRole.UserRole) for i in range(self.file_list.count())]
        if not paths:
            self.log("请先添加文件或文件夹。")
            return
        output_dir = self.output_edit.text().strip()
        if not output_dir:
            self.log("请选择输出目录。")
            return
        Path(output_dir).mkdir(parents=True, exist_ok=True)

        self.start_btn.setEnabled(False)
        self.progress_bar.setValue(0)
        self.log("开始转换...")

        self.worker = ConvertWorker(
            paths=paths,
            output_dir=output_dir,
            method=self.method_combo.currentData(),
            subject=self.subject_edit.text().strip(),
            add_frontmatter=self.frontmatter_check.isChecked(),
            postprocess=self.postprocess_check.isChecked(),
            config=self.config,
        )
        self.worker.log.connect(self.log)
        self.worker.progress.connect(self.progress_bar.setValue)
        self.worker.finished_all.connect(self.on_finished)
        self.worker.start()

    def on_finished(self, result):
        self.start_btn.setEnabled(True)
        self.progress_bar.setValue(100)
        self.log(
            f"\n=== 全部完成：成功 {result.get('success', 0)}，"
            f"失败 {result.get('failed', 0)} ==="
        )

    # ---------- 日志 ----------
    def log(self, msg: str):
        self.log_view.appendPlainText(msg)
        # 自动滚动到底部
        sb = self.log_view.verticalScrollBar()
        sb.setValue(sb.maximum())

    # ---------- 配置 ----------
    @staticmethod
    def _load_config() -> dict:
        config_path = APP_DIR / "config.json"
        if config_path.exists():
            try:
                with open(config_path, "r", encoding="utf-8") as f:
                    return json.load(f)
            except Exception:
                return {}
        return {}


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
