# Pythonの公式イメージをベースにする
FROM python:3.13-slim

# 環境変数を設定
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

# 作業ディレクトリを指定
WORKDIR /app

# ローカルのrequirements.txtをコンテナ内にコピー
COPY requirements.txt /app/

# 必要なパッケージをインストール
RUN pip install --no-cache-dir -r requirements.txt

# アプリケーションコードをコンテナにコピー
COPY . /app/

# ポート8000を開放
EXPOSE 8000
