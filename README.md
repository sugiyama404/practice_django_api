# Django REST Todo List API

Django REST Framework を使ったシンプルなTodoリストAPIです。
Docker ComposeでPostgreSQLとDjangoアプリを簡単に起動できます。

## 機能
+ タスクの作成 (Create)
+ タスクの取得 (Read)
+ タスクの更新 (Update)
+ タスクの削除 (Delete)
+ ヘルスチェックエンドポイント

## 技術スタック
+ Django REST Framework
+ PostgreSQL
+ Docker & Docker Compose

## 起動方法
1. 以下のコマンドでDockerコンテナを起動します。

```bash
docker compose up --build
```

2. 別のターミナルでコンテナ内でマイグレーションとデータ初期化を実行します

```bash
python manage.py makemigrations
python manage.py migrate
python manage.py loaddata initial_data.json
```

3. ブラウザまたはAPIクライアントで `http://localhost:8000/api/health/` にアクセスして動作確認します。


## API エンドポイント

```http
GET /api/health/ HTTP/1.1
Response: 200 OK (20 bytes)

POST /api/todos/ HTTP/1.1
Response: 201 Created (126 bytes)

GET /api/todos/6 HTTP/1.1
Response: 301 Moved Permanently (0 bytes)

PUT /api/todos/6/ HTTP/1.1
Response: 200 OK (128 bytes)

GET /api/todos/6/ HTTP/1.1
Response: 200 OK (128 bytes)

DELETE /api/todos/6/ HTTP/1.1
Response: 204 No Content (0 bytes)
```
