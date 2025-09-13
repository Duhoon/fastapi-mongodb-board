# FastAPI-MongoDB 게시판

FastAPI와 MongoDB를 사용하여 구현한 간단한 게시판 API 서버입니다.

## 🌟 주요 기능

- 게시글 생성, 조회, 수정, 삭제 (CRUD)
- 페이지네이션을 통한 게시글 목록 조회

## 🛠️ 사용 기술

- **언어**: Python 3
- **프레임워크**: FastAPI
- **데이터베이스**: MongoDB
- **의존성 관리**: Poetry
- **기타**: Uvicorn, Pydantic, python-dotenv

## 📂 프로젝트 구조

```
.
├── app/                  # 애플리케이션 소스 코드
│   ├── db.py             # MongoDB 연결 및 설정
│   ├── dto.py            # 데이터 전송 객체 (DTO)
│   ├── model.py          # 데이터 모델 (Pydantic)
│   └── service.py        # 비즈니스 로직
├── .env.sample           # 환경변수 예시 파일
├── main.py               # FastAPI 애플리케이션 진입점
├── pyproject.toml        # 프로젝트 의존성 및 설정
└── README.md             # 프로젝트 소개
```

## 🚀 시작하기

### 1. 사전 준비

- Python 3.13+
- Poetry
- MongoDB

### 2. 설치 및 설정

1.  **저장소 복제**

    ```bash
    git clone https://github.com/your-username/fastapi-mongodb-board.git
    cd fastapi-mongodb-board
    ```

2.  **의존성 설치**

    Poetry를 사용하여 필요한 패키지를 설치합니다.

    ```bash
    poetry install
    ```

3.  **환경변수 설정**

    `.env.sample` 파일을 복사하여 `.env` 파일을 생성하고, MongoDB 연결 정보를 입력합니다.

    ```bash
    cp .env.sample .env
    ```

    `.env` 파일 내용:

    ```
    # .env
    DB_HOST=mongodb://<user>:<password>@<host>:<port>/
    DB_NAME=board
    ```

### 3. 애플리케이션 실행

Uvicorn을 사용하여 FastAPI 서버를 실행합니다.

```bash
poetry run uvicorn main:app --host 0.0.0.0 --port 8080 --reload
```

서버가 실행되면 `http://localhost:8080/docs` 에서 API 문서를 확인할 수 있습니다.

## 📖 API 엔드포인트

- `GET /status`: 서버 상태 확인
- `GET /posts`: 게시글 목록 조회 (페이지네이션)
- `GET /post/{_id}`: 특정 게시글 조회
- `POST /post`: 새 게시글 생성
- `PUT /post`: 기존 게시글 수정
- `DELETE /post/{_id}`: 게시글 삭제
