import subprocess
 
# Wheel 파일 설치
subprocess.run(["pip", "install", "/mnt/data/koreanize_matplotlib-0.1.1-py3-none-any.whl"])
 
# 설치 확인
import koreanize_matplotlib
koreanize_matplotlib.__version__
