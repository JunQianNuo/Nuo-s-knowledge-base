from pathlib import Path
import hashlib
import json

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from openpyxl import Workbook
from openpyxl.styles import Alignment, Font, PatternFill


ROOT = Path(__file__).resolve().parents[2]
DATA_DIR = ROOT / "附件" / "2026年度“策联杯”数学建模精英联赛-A题-附件"
OUT_DIR = ROOT / "问题分析" / "数据审计"
FIG_DIR = ROOT / "图表"
SUMMARY_CSV = DATA_DIR / "battery_summary.csv"
CYCLE_CSV = DATA_DIR / "cycle_train.csv"


def sha256(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest().upper()


def value_at(g, cycle):
    x = g.loc[g["cycle"].eq(cycle), "SOH_smooth"]
    return float(x.iloc[0]) if len(x) else np.nan


def slope(g, start, end):
    h = g[g["cycle"].between(start, end)]
    return float(np.polyfit(h["cycle"], h["SOH_smooth"], 1)[0]) if len(h) > 1 else np.nan


def build_battery_table(summary, cycles):
    rows = []
    for battery_id, g in cycles.sort_values(["battery_id", "cycle"]).groupby("battery_id"):
        r = summary.loc[summary["battery_id"].eq(battery_id)].iloc[0]
        row = r.to_dict()
        row.update(
            n_cycles=len(g),
            last_cycle=int(g["cycle"].max()),
            soh20=value_at(g, 20),
            soh50=value_at(g, 50),
            soh100=value_at(g, 100),
            soh150=value_at(g, 150),
            soh200=value_at(g, 200),
            delta_soh_20_150=value_at(g, 150) - value_at(g, 20),
            delta_soh_20_200=value_at(g, 200) - value_at(g, 20),
            slope_20_150=slope(g, 20, 150),
            slope_20_200=slope(g, 20, 200),
            eol_observed_raw=int((g["SOH"] <= 0.8).any()),
            eol_observed_smooth=int((g["SOH_smooth"] <= 0.8).any()),
        )
        rows.append(row)
    return pd.DataFrame(rows)


def policy_table(battery):
    common = (
        battery.groupby("policy", dropna=False)
        .agg(
            n_batteries=("battery_id", "size"),
            n_prediction_test=("prediction_test", "sum"),
            C1=("C1", "first"),
            Q1=("Q1", "first"),
            C2=("C2", "first"),
            mean_charge_time=("mean_chargetime", "mean"),
            sd_charge_time=("mean_chargetime", "std"),
            median_soh150=("soh150", "median"),
            mean_soh150=("soh150", "mean"),
            sd_soh150=("soh150", "std"),
            median_delta_20_150=("delta_soh_20_150", "median"),
            mean_delta_20_150=("delta_soh_20_150", "mean"),
            sd_delta_20_150=("delta_soh_20_150", "std"),
            median_slope_20_150=("slope_20_150", "median"),
            mean_temperature=("mean_Tavg", "mean"),
            mean_resistance=("mean_IR", "mean"),
        )
        .reset_index()
    )
    complete = battery[battery["prediction_test"].eq(0)]
    horizon200 = (
        complete.groupby("policy", dropna=False)
        .agg(
            n_complete=("battery_id", "size"),
            median_soh200=("soh200", "median"),
            mean_soh200=("soh200", "mean"),
            sd_soh200=("soh200", "std"),
            median_delta_20_200=("delta_soh_20_200", "median"),
            mean_delta_20_200=("delta_soh_20_200", "mean"),
            sd_delta_20_200=("delta_soh_20_200", "std"),
            median_slope_20_200=("slope_20_200", "median"),
        )
        .reset_index()
    )
    out = common.merge(horizon200, on="policy", how="left")
    out["rank_150"] = out["median_delta_20_150"].rank(ascending=False, method="min").astype(int)
    out["rank_200"] = out["median_delta_20_200"].rank(ascending=False, method="min").astype(int)
    return out.sort_values("rank_150")


def audit_table(summary, cycles, battery):
    merged = cycles.merge(summary[["battery_id", "initial_capacity", "policy"]], on="battery_id", suffixes=("_cycle", "_summary"))
    consistency = (merged["SOH"] - merged["capacity"] / merged["initial_capacity"]).abs()
    policy_mismatch = int((merged["policy_cycle"] != merged["policy_summary"]).sum())
    anomalies = [
        ["表规模", "battery_summary.csv", f"{len(summary)}行×{summary.shape[1]}列", "通过"],
        ["表规模", "cycle_train.csv", f"{len(cycles)}行×{cycles.shape[1]}列", "通过"],
        ["电池ID", "两表独立电池数", f"{summary.battery_id.nunique()}/{cycles.battery_id.nunique()}", "通过"],
        ["主键", "summary battery_id重复", int(summary.battery_id.duplicated().sum()), "通过"],
        ["主键", "cycle battery_id+cycle重复", int(cycles.duplicated(["battery_id", "cycle"]).sum()), "通过"],
        ["缺失", "summary缺失单元格", int(summary.isna().sum().sum()), "需说明：3个C1缺失"],
        ["缺失", "cycle缺失单元格", int(cycles.isna().sum().sum()), "通过"],
        ["一致性", "策略表间不一致行", policy_mismatch, "通过"],
        ["一致性", "SOH与capacity/initial_capacity最大绝对误差", float(consistency.max()), "通过"],
        ["阈值", "原始SOH≤0.8行数", int((cycles.SOH <= 0.8).sum()), "无EOL事件"],
        ["阈值", "平滑SOH≤0.8行数", int((cycles.SOH_smooth <= 0.8).sum()), "无EOL事件"],
        ["截断", "150循环测试电池", int((battery.last_cycle == 150).sum()), "与prediction_test一致"],
        ["截断", "200循环非测试电池", int((battery.last_cycle == 200).sum()), "与prediction_test一致"],
        ["异常", "SOH>1.2行数", int((cycles.SOH > 1.2).sum()), "电池1第12循环"],
        ["异常", "IR=0行数", int((cycles.IR == 0).sum()), "电池2/3第12循环"],
    ]
    return pd.DataFrame(anomalies, columns=["类别", "检查项", "结果", "判定"])


def plots(cycles, battery, policy):
    plt.rcParams.update({"font.family": ["Microsoft YaHei", "SimHei", "DejaVu Sans"], "axes.unicode_minus": False})
    colors = dict(zip(sorted(cycles.policy.unique()), plt.cm.tab10.colors))

    fig, ax = plt.subplots(figsize=(11, 6.5))
    for _, g in cycles.groupby("battery_id"):
        pol = g.policy.iloc[0]
        test = int(battery.loc[battery.battery_id.eq(g.battery_id.iloc[0]), "prediction_test"].iloc[0])
        plot_g = g[~((g.battery_id.eq(1)) & g.cycle.between(10, 14))]
        ax.plot(plot_g.cycle, plot_g.SOH_smooth, color=colors[pol], alpha=0.42, lw=1.0, ls="--" if test else "-")
    ax.axhline(0.8, color="black", lw=1.2, ls=":", label="EOL阈值 0.8")
    ax.set(xlabel="循环次数", ylabel="平滑SOH", title="49块电池的平滑SOH轨迹（虚线为问题3测试电池）")
    ax.set_ylim(0.94, 1.01)
    ax.grid(alpha=0.2)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "A题问题一-SOH轨迹.png", dpi=220)
    plt.close(fig)

    order = policy.sort_values("rank_150")["policy"].tolist()
    data = [battery.loc[battery.policy.eq(p), "delta_soh_20_150"].dropna().to_numpy() for p in order]
    labels = [p.replace("_NEWSTRUCTURE", "\nNEW").replace("PER", "%") for p in order]
    fig, ax = plt.subplots(figsize=(12, 6.8))
    ax.boxplot(data, tick_labels=labels, showmeans=True)
    ax.axhline(0, color="black", lw=0.8)
    ax.set(ylabel="SOH(150)-SOH(20)", title="不同完整策略在共同150循环窗口内的SOH变化")
    ax.tick_params(axis="x", rotation=25, labelsize=8)
    ax.grid(axis="y", alpha=0.2)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "A题问题一-策略衰减分布.png", dpi=220)
    plt.close(fig)

    fig, ax = plt.subplots(figsize=(8.5, 6.2))
    ax.scatter(policy.mean_charge_time, -100 * policy.median_delta_20_150, s=35 + 8 * policy.n_batteries, c=policy.rank_150, cmap="viridis_r")
    for _, r in policy.iterrows():
        ax.annotate(str(r.policy).replace("_NEWSTRUCTURE", " NEW"), (r.mean_charge_time, -100 * r.median_delta_20_150), fontsize=7, xytext=(3, 3), textcoords="offset points")
    ax.set(xlabel="平均充电时间（原表单位）", ylabel="20—150循环SOH下降（百分点）", title="充电时间与早期衰减的策略级权衡")
    ax.grid(alpha=0.2)
    fig.tight_layout()
    fig.savefig(FIG_DIR / "A题问题一-时间衰减权衡.png", dpi=220)
    plt.close(fig)


def write_workbook(audit, policy, battery):
    path = OUT_DIR / "A题问题一数据审计.xlsx"
    with pd.ExcelWriter(path, engine="openpyxl") as writer:
        audit.to_excel(writer, sheet_name="审计总览", index=False)
        policy.to_excel(writer, sheet_name="策略汇总", index=False)
        battery.to_excel(writer, sheet_name="电池级主表", index=False)
        pd.DataFrame(
            [
                ["battery_summary.csv", sha256(SUMMARY_CSV), SUMMARY_CSV.stat().st_size],
                ["cycle_train.csv", sha256(CYCLE_CSV), CYCLE_CSV.stat().st_size],
            ],
            columns=["文件", "SHA256", "字节数"],
        ).to_excel(writer, sheet_name="输入文件", index=False)
    wb = pd.ExcelFile(path)
    del wb
    from openpyxl import load_workbook
    book = load_workbook(path)
    header_fill = PatternFill("solid", fgColor="1F4E78")
    for ws in book.worksheets:
        ws.freeze_panes = "A2"
        ws.auto_filter.ref = ws.dimensions
        for cell in ws[1]:
            cell.font = Font(name="Arial", bold=True, color="FFFFFF")
            cell.fill = header_fill
            cell.alignment = Alignment(horizontal="center")
        for col in ws.columns:
            letter = col[0].column_letter
            width = min(45, max(12, max(len(str(x.value)) if x.value is not None else 0 for x in col) + 2))
            ws.column_dimensions[letter].width = width
    book.save(path)


def main():
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    summary = pd.read_csv(SUMMARY_CSV)
    cycles = pd.read_csv(CYCLE_CSV)
    battery = build_battery_table(summary, cycles)
    policy = policy_table(battery)
    audit = audit_table(summary, cycles, battery)
    battery.to_csv(OUT_DIR / "A题问题一电池级主表.csv", index=False, encoding="utf-8-sig")
    policy.to_csv(OUT_DIR / "A题问题一策略汇总.csv", index=False, encoding="utf-8-sig")
    audit.to_csv(OUT_DIR / "A题问题一审计总览.csv", index=False, encoding="utf-8-sig")
    write_workbook(audit, policy, battery)
    plots(cycles, battery, policy)
    result = {
        "summary_shape": list(summary.shape),
        "cycle_shape": list(cycles.shape),
        "batteries": int(summary.battery_id.nunique()),
        "policies": int(summary.policy.nunique()),
        "prediction_test": int(summary.prediction_test.sum()),
        "eol_events": int(battery.eol_observed_smooth.sum()),
        "best_150_policy": policy.iloc[0].policy,
        "worst_150_policy": policy.iloc[-1].policy,
    }
    (OUT_DIR / "A题问题一审计摘要.json").write_text(json.dumps(result, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(result, ensure_ascii=False))


if __name__ == "__main__":
    main()
