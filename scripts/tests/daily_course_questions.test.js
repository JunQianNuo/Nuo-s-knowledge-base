const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

const vaultRoot = path.resolve(__dirname, "../..");
const viewPath = path.join(vaultRoot, "scripts/dataview/每日课堂疑惑/view.js");
const templatePath = path.join(vaultRoot, "模板/每日计划模板.md");

assert.ok(fs.existsSync(viewPath), "每日课堂疑惑 Dataview 视图尚未创建");

const source = fs.readFileSync(viewPath, "utf8");
const exportsMatch = source.match(
  /\/\* TEST_EXPORTS_START\s*([\s\S]*?)\s*TEST_EXPORTS_END \*\//,
);
assert.ok(exportsMatch, "视图需要暴露可测试的纯函数");
const runtimeSource = source.replace(exportsMatch[0], "");
const templateSource = fs.readFileSync(templatePath, "utf8");
assert.doesNotMatch(
  templateSource,
  /dv\.current\(\)\.date/,
  "模板调用不能假设 dv.current() 已完成索引",
);
assert.doesNotMatch(
  runtimeSource,
  /return\s*\{\s*parseWeekSpec/,
  "测试导出不能成为 Dataview 视图的返回值",
);
assert.doesNotMatch(
  runtimeSource,
  /window\.prompt\s*\(/,
  "Electron 不支持 window.prompt，疑惑输入必须使用 Obsidian 内部界面",
);

const exported = vm.runInNewContext(`(() => {${runtimeSource}\nreturn ${exportsMatch[1]};})()`, {
  console,
  Date,
  Math,
  RegExp,
});

const {
  parseWeekSpec,
  parseScheduleTable,
  getTeachingDay,
  buildQuestionEntry,
  insertQuestionEntry,
  openQuestionDialog,
  resolveNoteDate,
} = exported;
assert.equal(typeof openQuestionDialog, "function");
assert.equal(typeof resolveNoteDate, "function");
const plain = (value) => JSON.parse(JSON.stringify(value));

assert.equal(parseWeekSpec("1-16", 9), true);
assert.equal(parseWeekSpec("1-8单", 7), true);
assert.equal(parseWeekSpec("1-8单", 8), false);
assert.equal(parseWeekSpec("2-16双", 12), true);
assert.equal(parseWeekSpec("3,5,7", 5), true);
assert.equal(parseWeekSpec("1-4,6-12", 5), false);
assert.equal(parseWeekSpec("1-4,6-12", 6), true);

assert.deepEqual(
  plain(getTeachingDay("2026-09-15", "2026-08-31")),
  { week: 3, weekday: "二" },
);

assert.equal(resolveNoteDate("2026-09-16", undefined, "每日疑惑/2026-09-15.md"), "2026-09-16");
assert.equal(resolveNoteDate(undefined, { date: "2026-09-15" }, "每日疑惑/旧文件名.md"), "2026-09-15");
assert.equal(resolveNoteDate(undefined, undefined, "每日疑惑/2026-09-15.md"), "2026-09-15");
assert.deepEqual(
  plain(getTeachingDay("2026-08-30", "2026-08-31")),
  { week: 0, weekday: "日" },
);

const timetable = fs.readFileSync(path.join(vaultRoot, "课表.md"), "utf8");
const rows = parseScheduleTable(timetable);
assert.equal(rows.length, 17);
assert.deepEqual(plain(rows[0]), {
  course: "习近平新时代中国特色社会主义思想概论",
  weekday: "二",
  periods: "1-2",
  time: "08:30-10:05",
  weeks: "1-11",
  meeting: "",
  teacher: "朱晶",
});

const today = getTeachingDay("2026-09-15", "2026-08-31");
const activeCourses = rows.filter(
  (row) => row.weekday === today.weekday && parseWeekSpec(row.weeks, today.week),
);
assert.deepEqual(
  plain(activeCourses.map((row) => row.course)),
  [
    "习近平新时代中国特色社会主义思想概论",
    "专业写作基础",
    "泛函分析",
    "数理统计",
  ],
);

const entry = buildQuestionEntry(
  {
    course: "数理统计",
    periods: "7-8",
    time: "16:20-17:55",
    teacher: "陈碧",
  },
  "为什么这里使用充分统计量？",
  new Date(2026, 8, 15, 16, 42),
);
assert.match(entry, /### 16:42 · 数理统计/);
assert.match(entry, /\*\*记录时间\*\*：2026-09-15 16:42/);

const marker = "<!-- 课堂疑惑：结束 -->";
const inserted = insertQuestionEntry(`开头\n${marker}\n结尾`, entry);
assert.ok(inserted.indexOf(entry) < inserted.indexOf(marker));
assert.throws(
  () => insertQuestionEntry("缺少标记", entry),
  /缺少课堂疑惑写入标记/,
);

console.log("daily_course_questions: 26 assertions passed");
