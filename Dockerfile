# 1. 파이썬 3.9 환경 이미지 사용
FROM python:3.9-slim

# 2. 컨테이너 내부의 작업 폴더 설정
WORKDIR /app

# 3. 필요한 파일들을 컨테이너 안으로 복사
# (현재 폴더의 requirements.txt, app.py, models 폴더를 컨테이너의 /app으로 복사)
COPY requirements.txt .
COPY app.py .
COPY models/ ./models/

# 4. 패키지 설치
RUN pip install --no-cache-dir -r requirements.txt

# 5. API 서버가 사용할 8000번 포트 개방
EXPOSE 8000

# 6. 컨테이너 실행 시 서버 시작 명령어
CMD ["python", "app.py"]
