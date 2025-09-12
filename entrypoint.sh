#!/usr/bin/env bash
set -euo pipefail

# (필요하다면 앱 자체에서도 DB 준비 확인 로직 추가 가능)
# 여기서는 단순히 서버 실행만
# FastAPI라면:
# exec uvicorn main:app --host 0.0.0.0 --port "${APP_PORT:-8000}"

# 현재 구조가 CLI 실행이라면(예: main.py)
exec python -m main
