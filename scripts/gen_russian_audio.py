"""生成俄语对话音频 — 逐句 + 完整版."""
import sys, os
from gtts import gTTS
from pydub import AudioSegment

sys.stdout.reconfigure(encoding='utf-8')

VAULT = r"D:\知识库"
OUT_DIR = os.path.join(VAULT, "未命名")
OUT_FULL = os.path.join(OUT_DIR, "俄语对话-完整.mp3")
OUT_PRACTICE = os.path.join(OUT_DIR, "俄语对话-逐句练习.mp3")

# 对话内容（俄语原文）
lines = [
    ("Максим", "Привет!"),
    ("Анна", "Привет!"),
    ("Максим", "Давай познакомимся. Меня зовут Максим. А тебя?"),
    ("Анна", "Очень приятно. Меня зовут Анна."),
    ("Максим", "Ты студентка?"),
    ("Анна", "Да, я учусь в университете. Я из Китая. А ты?"),
    ("Максим", "Я тоже студент. Я изучаю экономику. А что ты изучаешь?"),
    ("Анна", "Я изучаю русский язык."),
    ("Максим", "Здорово! Ты уже хорошо говоришь по-русски."),
    ("Анна", "Спасибо! Но я ещё только учусь."),
    ("Максим", "Что ты любишь делать в свободное время?"),
    ("Анна", "Я люблю читать книги и слушать музыку. А ты?"),
    ("Максим", "Я тоже люблю музыку. Ещё я люблю спорт."),
    ("Анна", "Какой спорт ты любишь?"),
    ("Максим", "Я играю в футбол. Давай как-нибудь поиграем вместе?"),
    ("Анна", "С удовольствием!"),
    ("Максим", "Ой, уже много времени. Мне пора на лекцию."),
    ("Анна", "Хорошо. Было приятно познакомиться!"),
    ("Максим", "Мне тоже. До встречи!"),
    ("Анна", "Пока!"),
]

PAUSE_MS = 800      # 句间停顿
LONG_PAUSE_MS = 1500  # 角色切换停顿

print("🎙 正在生成音频（使用 Google TTS 俄语语音）...")

# --- 1. 完整版：连续播放 ---
full_audio = AudioSegment.silent(duration=300)
for i, (speaker, text) in enumerate(lines):
    mp3_path = os.path.join(OUT_DIR, f"_tmp_{i}.mp3")
    tts = gTTS(text=text, lang="ru", slow=False)
    tts.save(mp3_path)
    seg = AudioSegment.from_mp3(mp3_path)
    full_audio += seg
    pause = LONG_PAUSE_MS if i < len(lines) - 1 and lines[i+1][0] != speaker else PAUSE_MS
    full_audio += AudioSegment.silent(duration=pause)
    os.remove(mp3_path)

full_audio.export(OUT_FULL, format="mp3", bitrate="128k")
print(f"✅ 完整版 → {OUT_FULL}")

# --- 2. 逐句练习版：每句读两遍（慢速→常速），中间留跟读时间 ---
practice_audio = AudioSegment.silent(duration=500)
for i, (speaker, text) in enumerate(lines):
    mp3_path = os.path.join(OUT_DIR, f"_tmp_p_{i}.mp3")
    # 第一遍：常速
    tts = gTTS(text=text, lang="ru", slow=False)
    tts.save(mp3_path)
    seg1 = AudioSegment.from_mp3(mp3_path)
    # 第二遍：慢速
    tts_slow = gTTS(text=text, lang="ru", slow=True)
    tts_slow.save(mp3_path)
    seg2 = AudioSegment.from_mp3(mp3_path)

    practice_audio += seg1 + AudioSegment.silent(duration=400)
    practice_audio += seg2 + AudioSegment.silent(duration=2500)  # 跟读时间
    os.remove(mp3_path)

practice_audio.export(OUT_PRACTICE, format="mp3", bitrate="128k")
print(f"✅ 逐句练习版 → {OUT_PRACTICE}")
print("\n📁 音频文件已保存到 vault 的「未命名」文件夹。")
