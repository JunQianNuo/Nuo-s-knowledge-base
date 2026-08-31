#!/usr/bin/env python3
"""Run mineru vlm-auto-engine on 总结 1.pdf, 5 pages test."""
import subprocess, sys, os

# Ensure proxy works by inheriting system settings
cmd = [
    sys.executable, "-m", "mineru.cli.client",
    "-p", r"D:\知识库\课程\数值分析\课件\总结 1.pdf",
    "-o", r"D:\知识库\课程\数值分析\课件\MD",
    "-b", "vlm-auto-engine",
    "-l", "ch",
    "--start", "0",
    "--end", "4"
]
print("Running:", " ".join(cmd[-6:]))
result = subprocess.run(cmd)
sys.exit(result.returncode)
