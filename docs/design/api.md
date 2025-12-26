# API設計書 (API Specification)

## 概要
Backend (Flask) が提供するRESTful APIの定義。
Frontend (React) からの非同期通信により利用される。

## 基本設計
* **Base URL:** `/api`
* **Content-Type:** `application/json`
* **Error Handling:** HTTPステータスコードを使用し、エラー詳細はJSONで返却。

## エンドポイント一覧

### 1. 成果物一覧取得 (List Outputs)
登録された成果物を日付の降順で取得する。

* **URL:** `/outputs`
* **Method:** `GET`
* **Response (200 OK):**
  ```json
  [
    {
      "id": 1,
      "title": "My First Blog",
      "url": "https://zenn.dev/...",
      "content_type": "Blog",
      "published_at": "2023-10-27",
      "comment": "頑張って書いた",
      "created_at": "2023-10-27T10:00:00Z"
    }
  ]
  ```

### 2. 成果物登録 (Create Output)
新しい成果物を登録する。

* **URL:** `/outputs`
* **Method:** `POST`
* **Request Body:**
  ```json
  {
    "title": "My New Video",
    "url": "https://youtube.com/...",
    "content_type": "Video",
    "published_at": "2023-10-28",
    "comment": "動画編集が大変だった"
  }
  ```
* **Response (201 Created):**
  ```json
  {
    "id": 2,
    "message": "Output created successfully"
  }
  ```

### 3. 成果物更新 (Update Output)
既存の成果物情報を更新する。

* **URL:** `/outputs/<id>`
* **Method:** `PUT`
* **Request Body:**
  ```json
  {
    "title": "Updated Title",
    "comment": "Updated comment"
  }
  ```
* **Response (200 OK):**
  ```json
  {
    "id": 1,
    "message": "Output updated successfully"
  }
  ```

### 4. 成果物削除 (Delete Output)
成果物を削除する。

* **URL:** `/outputs/<id>`
* **Method:** `DELETE`
* **Response (200 OK):**
  ```json
  {
    "message": "Output deleted successfully"
  }
  ```
