# 1. 기본 이미지로 Python을 사용
FROM python:3.12-slim

# 2. 작업 디렉토리 설정
WORKDIR /app

# 3. 필요한 파일들을 컨테이너로 복사
COPY requirements.txt /app/

# 4. 필요한 패키지 설치
RUN pip install --no-cache-dir -r requirements.txt

# 5. 프로젝트 파일 복사
COPY . /app/

# 6. Streamlit을 실행할 포트 설정
EXPOSE 8501

# 7. Streamlit 앱 실행
CMD ["streamlit", "run", "app.py", "--server.port", "8501", "--server.address", "0.0.0.0"]
