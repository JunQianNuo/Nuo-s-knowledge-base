import datetime as dt

from scripts import pull_tmeet_recordings as recordings


TIMETABLE = """---
学期: 测试学期
开学日期: 2026-10-05
停课: 2026-10-09
---

| 课程 | 星期 | 节次 | 时间段 | 周次 | 会议号 | 教师 |
|:--|:--|:--|:--|:--|:--|:--|
| 测试课程 | 五 | 5-6 | 14:30-16:05 | 1-2 |  | 测试教师 |
"""


def write_timetable(tmp_path):
    path = tmp_path / "课表.md"
    path.write_text(TIMETABLE, encoding="utf-8")
    return recordings.load_timetable(path)


def test_cancelled_date_does_not_increment_later_class_number(tmp_path):
    timetable = write_timetable(tmp_path)
    course = timetable["courses"][0]

    class_no = recordings.class_no_for(
        course, dt.date(2026, 10, 16), timetable
    )

    assert class_no == 1


def test_cancelled_date_does_not_match_a_course(tmp_path):
    timetable = write_timetable(tmp_path)
    meeting_time = dt.datetime.fromisoformat("2026-10-09T14:30:00+08:00")

    assert recordings.match_course(meeting_time, timetable) == (None, None)
