# 要件定義書 (Requirements Definition)

## 1. プロジェクト概要
**プロジェクト名:** どんなことでもアウトプットこそ重要！
**目的:** 自身の成果物（Zennブログ、YouTube動画など）を一元管理・記録し、アウトプットの継続率を高めること。
**ターゲット:** 開発者自身 (自分用)

## 2. 機能要件 (Functional Requirements)

### 2.1 成果物管理機能 (Core)
- **成果物の登録 (Create):**
  - タイトル、URL、種別（ブログ、動画、その他）、日付、コメントを登録できること。
- **成果物の一覧表示 (Read):**
  - 登録された成果物を一覧で表示できること。
  - 日付順（新しい順）で表示されること。
- **成果物の編集・削除 (Update/Delete):**
  - 登録済みの情報を修正または削除できること。

### 2.2 ダッシュボード/統計 (Future)
- **継続記録の可視化:**
  - 週間/月間のアウトプット数をグラフまたは数値で表示（モチベーション維持のため）。

## 3. 非機能要件 (Non-Functional Requirements)

### 3.1 技術スタック (Architecture)
`GEMINI.md` 及び `AGENT.md` の指針に基づき、以下の構成を採用する。

*   **Frontend:** React (Vite)
    *   モダンなUI構築のため。既存の `frontend/` ディレクトリを活用。
*   **Backend:** Python (Flask)
    *   `AGENT.md` の Hard Constraints に準拠。軽量かつ柔軟なAPIサーバーとして利用。
*   **Database:** PostgreSQL
    *   データの永続化に使用。Kubernetes上での運用を想定。
    *   *補足:* 現在の実装はモックデータ (`app.py`) であるため、DB連携の実装が必要。
*   **Infrastructure:** Kubernetes (Minikube)
    *   `AGENT.md` の Hard Constraints に準拠。ローカル環境でのコンテナオーケストレーション。

### 3.2 品質・運用
*   **コード品質:** `AGENT.md` のPriorityに基づき、保守性と可読性を重視する。
*   **ドキュメント:** DDVC (Document Driven Vibrating Coding) に従い、機能実装前に必ずドキュメントを更新する。

## 4. 開発ロードマップ (Phase)

1.  **Phase 1: 基礎構築 (Current)**
    *   Flask + React の連携（完了済み）
    *   要件定義書の作成（本ドキュメント）
2.  **Phase 2: データ永続化**
    *   PostgreSQLのK8sデプロイメント
    *   BackendへのDB接続処理実装
3.  **Phase 3: CRUD機能実装**
    *   APIエンドポイントの整備
    *   Frontendの入力フォーム・一覧画面実装
