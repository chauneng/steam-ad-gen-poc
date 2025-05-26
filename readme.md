# Steam 리뷰 기반 GenAI 광고문구 생성 PoC

# Steam Review-Based GenAI Ad Copy Generation PoC

이 PoC(Proof of Concept)는 Steam 게임 리뷰 데이터를 수집·전처리하고, OpenAI를 활용해 광고 문구를 생성·저장한 뒤, Streamlit UI에서 피드백을 수집·반영하는 **End-to-End** 워크플로우를 Python 생태계만으로 구현합니다.
This Proof of Concept (PoC) implements an end-to-end Python workflow to collect and preprocess Steam game review data, generate advertising copy using OpenAI, store results in Snowflake, and gather and apply feedback via a Streamlit UI.

---

## 🚀 주요 기능 / Key Features

| 한국어 설명                                                                          | English Description                                                                                                                                          |
| ------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| **리뷰 수집 & 분류**: `steamreviews` 또는 HTTP 호출로 한국어·영어 리뷰 자동 크롤링                     | **Review Collection & Classification**: Automatic crawling of language-specific (e.g., Korean, English) reviews using `steamreviews` or direct HTTP requests |
| **데이터 파이프라인**: Prefect로 수집→전처리→생성→Snowflake 적재 워크플로우 오케스트레이션                    | **Data Pipeline**: Workflow orchestration with Prefect for collection → preprocessing → generation → Snowflake loading                                       |
| **GenAI 광고문구 생성**: 리뷰 감성·키워드 기반 동적 프롬프트로 OpenAI API 호출                          | **GenAI Ad Copy Generation**: Dynamic prompt creation based on review sentiment and keywords for OpenAI API calls                                            |
| **DWH 저장**: Snowflake `staging_reviews`, `ads_generated`, `ads_feedback` 테이블 관리 | **DWH Storage**: Management of `staging_reviews`, `ads_generated`, and `ads_feedback` tables in Snowflake                                                    |
| **피드백 루프**: Streamlit UI에서 별점·코멘트를 수집하여 프롬프트 개선에 반영                             | **Feedback Loop**: Streamlit UI for star rating and comments, feeding back into prompt refinement                                                            |

---

## 🛠️ 기술 스택 / Tech Stack

| 한국어                                                               | English                                                                            |
| ----------------------------------------------------------------- | ---------------------------------------------------------------------------------- |
| 언어: Python 3.10+                                                  | Language: Python 3.10+                                                             |
| 워크플로우: [Prefect](https://www.prefect.io)                          | Workflow: [Prefect](https://www.prefect.io)                                        |
| 데이터베이스: [Snowflake](https://www.snowflake.com)                    | Database: [Snowflake](https://www.snowflake.com)                                   |
| AI API: [OpenAI](https://openai.com)                              | AI API: [OpenAI](https://openai.com)                                               |
| 웹 UI: [Streamlit](https://streamlit.io)                           | UI: [Streamlit](https://streamlit.io)                                              |
| 환경 관리: [Poetry](https://python-poetry.org)                        | Dependency Management: [Poetry](https://python-poetry.org)                         |
| 환경변수: [python-dotenv](https://github.com/theskumar/python-dotenv) | Environment Variables: [python-dotenv](https://github.com/theskumar/python-dotenv) |

---

## 🔧 사전 준비 / Prerequisites

1. Python 3.10 이상 설치
   Python 3.10 or higher
2. Poetry 설치
   Poetry
3. Snowflake 평가 계정(또는 유사 DWH)
   Snowflake trial account (or equivalent DWH)
4. OpenAI API 키 발급
   OpenAI API key

### 환경변수 파일 작성 / Environment Variables

```bash
cp .env.example .env
# .env 파일에 아래 값 설정 / Set the following in .env:
OPENAI_API_KEY=sk-...
SNOWFLAKE_USER=...
SNOWFLAKE_PASSWORD=...
SNOWFLAKE_ACCOUNT=...
```

---

## 📦 설치 & 실행 / Installation & Execution

```bash
# Repository 클론 / Clone the repository
git clone <your-repo-url>
cd steam-ad-gen-poc

# 의존성 설치 / Install dependencies
poetry install

# Prefect 로컬 서버 시작 (필요 시) / (Optional) Start Prefect local server
prefect server start &

# Flow 배포 및 실행 예시 / Build and apply the Prefect flow
prefect deployment build flows/collect_and_generate.py:flow \
  --name collect-generate \
  --apply
prefect deployment run collect-generate/flow

# Streamlit UI 실행 / Run Streamlit UI
poetry run streamlit run ui/app.py
```

---

## 📁 프로젝트 구조 / Project Structure

```
├── flows/               # Prefect Flow 정의 / Prefect flow definitions
│   └── collect_and_generate.py
├── src/                 # 데이터 수집·전처리·생성 스크립트 / Data collection, preprocessing, and generation scripts
├── ui/                  # Streamlit 앱 (피드백 루프) / Streamlit app for feedback loop
├── README.md            # 프로젝트 설명 (이 파일) / Project description (this file)
├── pyproject.toml       # Poetry 설정 / Poetry configuration
├── .env.example         # 환경변수 템플릿 / Environment variable template
└── .gitignore           # Git 무시 설정 / Git ignore settings
```

---

## 🤝 기여 및 확장 / Contribution & Extensions

* **버그 리포트 / Bug Reports**: 이슈 등록 / Open an issue
* **기능 요청 / Feature Requests**: 새로운 Flow 또는 추가 데이터 소스 제안 / Suggest new flows or data sources
* **코드 기여 / Code Contributions**: `src/`, `flows/`, `ui/`에 PR 제출 / Submit a PR under `src/`, `flows/`, or `ui/`

---

## 📄 라이선스 / License

MIT
