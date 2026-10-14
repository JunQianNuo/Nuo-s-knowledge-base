function toIsoDate(value) {
  if (!value) return "";
  if (typeof value === "string") return value.slice(0, 10);
  if (typeof value.toFormat === "function") return value.toFormat("yyyy-MM-dd");
  if (value instanceof Date && !Number.isNaN(value.getTime())) {
    const year = value.getFullYear();
    const month = String(value.getMonth() + 1).padStart(2, "0");
    const day = String(value.getDate()).padStart(2, "0");
    return `${year}-${month}-${day}`;
  }
  return String(value).slice(0, 10);
}

function parseIsoDate(isoDate) {
  const match = /^(\d{4})-(\d{2})-(\d{2})$/.exec(isoDate);
  if (!match) return null;
  return new Date(Date.UTC(Number(match[1]), Number(match[2]) - 1, Number(match[3])));
}

function resolveNoteDate(inputDate, currentPage, currentFilePath) {
  const candidates = [inputDate, currentPage?.date, currentPage?.file?.day];
  for (const candidate of candidates) {
    const isoDate = toIsoDate(candidate);
    if (/^\d{4}-\d{2}-\d{2}$/.test(isoDate)) return isoDate;
  }

  const pathMatch = String(currentFilePath || "").match(/(?:^|\/)(\d{4}-\d{2}-\d{2})(?:\.md)?$/);
  return pathMatch ? pathMatch[1] : "";
}

function getTeachingDay(noteDate, semesterStart) {
  const current = parseIsoDate(toIsoDate(noteDate));
  const start = parseIsoDate(toIsoDate(semesterStart));
  if (!current || !start) return { week: 0, weekday: "" };

  const dayDifference = Math.floor((current - start) / 86400000);
  const weekdays = ["日", "一", "二", "三", "四", "五", "六"];
  return {
    week: dayDifference < 0 ? 0 : Math.floor(dayDifference / 7) + 1,
    weekday: weekdays[current.getUTCDay()],
  };
}

function parseWeekSpec(spec, week) {
  if (!Number.isInteger(week) || week < 1 || !spec) return false;

  return String(spec)
    .split(",")
    .some((part) => {
      const match = /^(\d+)(?:-(\d+))?(单|双)?$/.exec(part.trim());
      if (!match) return false;

      const start = Number(match[1]);
      const end = Number(match[2] || match[1]);
      const parity = match[3];
      const inRange = week >= start && week <= end;
      const parityMatches =
        !parity || (parity === "单" ? week % 2 === 1 : week % 2 === 0);
      return inRange && parityMatches;
    });
}

function parseScheduleTable(markdown) {
  const lines = String(markdown || "").split(/\r?\n/);
  const headerIndex = lines.findIndex((line) =>
    /^\|\s*课程\s*\|\s*星期\s*\|\s*节次\s*\|/.test(line),
  );
  if (headerIndex < 0) return [];

  const rows = [];
  for (const line of lines.slice(headerIndex + 2)) {
    if (!line.trim().startsWith("|")) break;
    const cells = line
      .trim()
      .replace(/^\|/, "")
      .replace(/\|$/, "")
      .split("|")
      .map((cell) => cell.trim());
    if (cells.length < 7 || !cells[0]) continue;
    rows.push({
      course: cells[0],
      weekday: cells[1],
      periods: cells[2],
      time: cells[3],
      weeks: cells[4],
      meeting: cells[5],
      teacher: cells[6],
    });
  }
  return rows;
}

function localTimestamp(date = new Date()) {
  const year = date.getFullYear();
  const month = String(date.getMonth() + 1).padStart(2, "0");
  const day = String(date.getDate()).padStart(2, "0");
  const hour = String(date.getHours()).padStart(2, "0");
  const minute = String(date.getMinutes()).padStart(2, "0");
  return { date: `${year}-${month}-${day}`, time: `${hour}:${minute}` };
}

function buildQuestionEntry(course, question, now = new Date()) {
  const timestamp = localTimestamp(now);
  const safeQuestion = String(question).trim().replace(/\r?\n/g, "\n> ");
  return [
    "",
    `### ${timestamp.time} · ${course.course}`,
    "",
    `> [!question] ${safeQuestion}`,
    `> **课程**：${course.course}`,
    `> **节次**：第${course.periods}节（${course.time}）`,
    `> **教师**：${course.teacher || "未填写"}`,
    `> **记录时间**：${timestamp.date} ${timestamp.time}`,
    "",
  ].join("\n");
}

function insertQuestionEntry(content, entry) {
  const marker = "<!-- 课堂疑惑：结束 -->";
  if (!content.includes(marker)) {
    throw new Error("当前笔记缺少课堂疑惑写入标记");
  }
  return content.replace(marker, `${entry}${marker}`);
}

async function appendQuestion(filePath, course, question) {
  const file = app.vault.getAbstractFileByPath(filePath);
  if (!file) {
    throw new Error("无法找到当前日记文件，请保存笔记后重试");
  }

  const entry = buildQuestionEntry(course, question);
  const insert = (content) => insertQuestionEntry(content, entry);

  if (typeof app.vault.process === "function") {
    await app.vault.process(file, insert);
  } else {
    const content = await app.vault.read(file);
    await app.vault.modify(file, insert(content));
  }
}

function openQuestionDialog(course, onSubmit, ownerDocument = document) {
  const overlay = ownerDocument.createElement("div");
  overlay.className = "daily-question-modal-overlay";
  overlay.setAttribute("role", "presentation");

  const dialog = ownerDocument.createElement("div");
  dialog.className = "daily-question-modal";
  dialog.setAttribute("role", "dialog");
  dialog.setAttribute("aria-modal", "true");
  dialog.setAttribute("aria-labelledby", "daily-question-modal-title");

  const title = ownerDocument.createElement("h3");
  title.id = "daily-question-modal-title";
  title.textContent = `记录「${course.course}」的疑惑`;

  const meta = ownerDocument.createElement("p");
  meta.className = "daily-question-modal-meta";
  meta.textContent = `第${course.periods}节 · ${course.time} · ${course.teacher || "教师未填写"}`;

  const textarea = ownerDocument.createElement("textarea");
  textarea.className = "daily-question-modal-input";
  textarea.rows = 5;
  textarea.placeholder = "写下这堂课中还没想明白的问题……";
  textarea.setAttribute("aria-label", "课堂疑惑");

  const status = ownerDocument.createElement("div");
  status.className = "daily-question-modal-status";
  status.setAttribute("role", "status");

  const actions = ownerDocument.createElement("div");
  actions.className = "daily-question-modal-actions";
  const cancelButton = ownerDocument.createElement("button");
  cancelButton.type = "button";
  cancelButton.textContent = "取消";
  const saveButton = ownerDocument.createElement("button");
  saveButton.type = "button";
  saveButton.className = "mod-cta";
  saveButton.textContent = "保存疑惑";
  actions.append(cancelButton, saveButton);

  dialog.append(title, meta, textarea, status, actions);
  overlay.appendChild(dialog);
  ownerDocument.body.appendChild(overlay);

  const close = () => overlay.remove();
  const save = async () => {
    const question = textarea.value.trim();
    if (!question) {
      status.textContent = "请先输入疑惑内容。";
      textarea.focus();
      return;
    }

    saveButton.disabled = true;
    cancelButton.disabled = true;
    status.textContent = "正在保存……";
    try {
      await onSubmit(question);
      close();
    } catch (error) {
      status.textContent = `保存失败：${error.message}`;
      saveButton.disabled = false;
      cancelButton.disabled = false;
      textarea.focus();
    }
  };

  cancelButton.addEventListener("click", close);
  saveButton.addEventListener("click", save);
  overlay.addEventListener("click", (event) => {
    if (event.target === overlay) close();
  });
  dialog.addEventListener("keydown", (event) => {
    if (event.key === "Escape") close();
    if (event.key === "Enter" && (event.ctrlKey || event.metaKey)) {
      event.preventDefault();
      void save();
    }
  });

  textarea.focus();
  return { overlay, textarea, saveButton };
}

async function renderDailyCourseQuestions() {
  const currentPage = dv.current?.() || {};
  const currentFilePath = dv.currentFilePath || currentPage.file?.path || "";
  const schedulePage = dv.page("课表");
  const noteDate = resolveNoteDate(input?.date, currentPage, currentFilePath);
  const semesterStart = toIsoDate(schedulePage?.["开学日期"]);
  const teachingDay = getTeachingDay(noteDate, semesterStart);
  const scheduleMarkdown = await dv.io.load("课表.md");

  if (!noteDate || !semesterStart || !scheduleMarkdown) {
    dv.paragraph("⚠️ 无法读取日记日期或 [[课表]]，请检查 frontmatter 与课表文件。");
    return;
  }

  const courses = parseScheduleTable(scheduleMarkdown)
    .filter(
      (course) =>
        course.weekday === teachingDay.weekday &&
        parseWeekSpec(course.weeks, teachingDay.week),
    )
    .sort((left, right) => Number(left.periods.split("-")[0]) - Number(right.periods.split("-")[0]));

  const summary = document.createElement("p");
  summary.className = "daily-course-summary";
  summary.textContent =
    teachingDay.week > 0
      ? `${noteDate} · 第 ${teachingDay.week} 周 · 星期${teachingDay.weekday}`
      : `${noteDate} · 尚未开学`;
  dv.container.appendChild(summary);

  if (courses.length === 0) {
    const empty = document.createElement("div");
    empty.className = "daily-course-empty";
    empty.textContent = teachingDay.week > 0 ? "今天没有有效课程。" : "该日期不在当前学期内。";
    dv.container.appendChild(empty);
    return;
  }

  const list = document.createElement("div");
  list.className = "daily-course-list";
  dv.container.appendChild(list);

  for (const course of courses) {
    const card = document.createElement("div");
    card.className = "daily-course-card";

    const details = document.createElement("div");
    details.className = "daily-course-details";
    const title = document.createElement("strong");
    title.textContent = course.course;
    const meta = document.createElement("span");
    meta.textContent = `第${course.periods}节 · ${course.time} · ${course.teacher || "教师未填写"}`;
    details.append(title, meta);

    const button = document.createElement("button");
    button.type = "button";
    button.textContent = "记录疑惑";
    button.addEventListener("click", () => {
      const ownerDocument = dv.container.ownerDocument || document;
      openQuestionDialog(
        course,
        (question) => appendQuestion(currentFilePath, course, question),
        ownerDocument,
      );
    });

    card.append(details, button);
    list.appendChild(card);
  }
}

if (typeof dv !== "undefined") {
  void renderDailyCourseQuestions().catch((error) => {
    dv.paragraph(`⚠️ 今日课表加载失败：${error.message}`);
  });
}

/* TEST_EXPORTS_START
({
  parseWeekSpec,
  parseScheduleTable,
  getTeachingDay,
  buildQuestionEntry,
  insertQuestionEntry,
  openQuestionDialog,
  resolveNoteDate,
})
TEST_EXPORTS_END */
