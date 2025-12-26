# 要件定義書 (Requirements Document)

## プロジェクト概要
個人が作成したアウトプット（Zennの記事、YouTube動画など）を記録・可視化し、継続的な活動を促進するためのアプリケーション。

## ユーザー要件
1. **アウトプットの登録**: ユーザーは、記事や動画のURL、タイトル、公開日、種類（Zenn/YouTube等）を登録できる。
2. **アウトプットの一覧表示**: 登録されたアウトプットを時系列（新しい順）で閲覧できる。
3. **継続性の可視化**: （将来的な拡張）活動の継続状況を可視化し、モチベーション維持に貢献する。

## 機能要件

### 1. Backend (API)
*   **言語/フレームワーク**: Python / Flask
*   **APIエンドポイント**:
    *   `GET /api/outputs`: アウトプット一覧の取得
    *   `POST /api/outputs`: アウトプットの新規登録
    *   `DELETE /api/outputs/<id>`: アウトプットの削除
*   **データモデル**:
    *   **Output**:
        *   `id`: Integer (Primary Key)
        *   `title`: String (タイトル)
        *   `url`: String (URL)
        *   `type`: String (zenn, youtube, other)
        *   `published_date`: Date (公開日)
        *   `created_at`: Datetime (作成日時)

### 2. Frontend (UI)
*   **ライブラリ**: React (Vite)
*   **画面**:
    *   **Dashboard**: アウトプット一覧表示と新規登録フォームを統合したメイン画面。
*   **UIコンポーネント**:
    *   登録フォーム（URL, タイトル, 種類, 日付）
    *   一覧リスト（カード形式またはテーブル）

### 3. Database
*   **種類**: PostgreSQL
*   **永続化**: Kubernetes PersistentVolume (Minikube上のローカルストレージ)

### 4. Infrastructure
*   **プラットフォーム**: Kubernetes (Minikube)
*   **構成**:
    *   **Flask App Pod**: Backend API + Frontend Static Files
    *   **Postgres Pod**: Database

## 非機能要件
*   **保守性**: コードはシンプルに保ち、Type Hinting等を用いて可読性を高める。
*   **拡張性**: 将来的な認証機能やグラフ機能の追加を考慮した設計とする。
