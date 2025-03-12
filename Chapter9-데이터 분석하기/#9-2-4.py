# [mplfinance 모듈 설치]
import subprocess
 
# 업로드된 .whl 파일 경로
whl_file_path = '/mnt/data/mplfinance-0.12.10b0-py3-none-any.whl'
 
# pip 명령어를 사용하여 .whl 파일 설치
subprocess.check_call(["pip", "install", whl_file_path])
