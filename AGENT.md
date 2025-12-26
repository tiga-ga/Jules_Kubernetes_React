## 1. プロジェクト定義 [User記入欄]
*人間が記入するエリア。プロジェクトの「核」となる定義。*

| 項目 | 内容 |
| :--- | :--- |
| **Project Name** | [ どんなことでもアウトプットこそ重要！ ] |
| **Vision / Goal** | [ 自分向け成果物（ZennブログとYoutubeなど）を記録するアプリ。継続率重視 ] |
| **Target User** | [ 自分用 ] |
| **Priority** | [ コード品質・保守性重視 ] |

## 2. 技術要件 (Constraints) [User記入欄]
*どうしても使いたい技術があれば記入。「お任せ」なら空白か「None」でOK。*

| カテゴリ | 必須技術 (Hard Constraints) |
| :--- | :--- |
| **Frontend** | [ None ] |
| **Backend** | [ Python ] |
| **Infra** | [ Kubernetes ] |
| **DB / Other** | [ None ] |

---
*これより下は、AI（あなた）が技術選定・実装後に自動的に更新・管理するエリア。*
*人間は原則ここを編集しなくてよい。*

## 3. アーキテクチャ・レジストリ (Architecture Registry)
*現在確定している技術スタック一覧*

* **Frontend:** React (Vite)
* **Backend:** Python (Flask)
* **Database:** PostgreSQL
* **Infrastructure:** Kubernetes (Minikube)
* **Testing/CI:** pytest (Backend), Vitest (Frontend)

## 4. 運用コンテキスト (Operational Context)
*開発に必要な動的情報*

**主要コマンド:**
* `deploy.sh`: ビルドおよびMinikubeへのデプロイ
* `minikube service flask-app-service`: ブラウザでアプリを開く

**ディレクトリ構造:**
* `/docs`: Specifications & Logs
* `/frontend`: React App Source
* `/k8s`: Kubernetes Manifests
* `/`: Flask App Source
