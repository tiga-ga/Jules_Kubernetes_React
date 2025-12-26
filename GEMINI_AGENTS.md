# GEMINI_AGENTS.md

> **役割:** プロジェクトの「地図」兼「憲法」。
> **ルール:** 上半分は人間が決定し、下半分はAIが実装に伴い更新する。

---

## 1. Human Context (Input Area) 🧠
*ここはあなたが記入・決定するエリアです。プロジェクトの「魂」を吹き込んでください。*

### 1-1. Project Definition (Vision & Vibe)
| 項目 | 内容 (編集してください) |
| :--- | :--- |
| **Project Name** | [ プロジェクト名を記入 ] |
| **Vision / Goal** | [ 何を作る？何を解決したい？（例：自分専用の学習ログアプリ。継続率重視） ] |
| **Target User** | [ 誰が使う？（例：自分のみ、特定のチーム、一般公開） ] |
| **Priority** | [ 何を優先する？（例：爆速開発、堅牢性・保守性、リッチなUIアニメーション） ] |

### 1-2. Tech Constraints (Hard Requirements)
*絶対に使いたい技術があれば記入。「お任せ」なら `None` や `Unselected` のままでOK。*

| カテゴリ | 必須技術 (Hard Constraints) |
| :--- | :--- |
| **Frontend** | [ 指定なし / React / Next.js / Vue など ] |
| **Backend** | [ 指定なし / Python / Go / Node.js など ] |
| **Infra** | [ 指定なし / Vercel / AWS / Docker / K8s など ] |
| **DB / Other** | [ 指定なし / PostgreSQL / Firebase / Supabase など ] |

---
---

## 2. AI Context (Managed Area) 🤖
*実装が進むにつれて、AIが自動的に詳細を追記・更新します。*

### 2-1. Architecture Registry (Current Stack)
*確定した技術スタックとバージョン*

* **Frontend:** (Unselected - 提案待ち)
* **Backend:** (Unselected - 提案待ち)
* **Database:** (Unselected - 提案待ち)
* **Infrastructure:** (Unselected - 提案待ち)
* **Testing:** (Unselected)

### 2-2. Directory Structure (The Map)
*プロジェクトの最新のディレクトリ構成と、各ファイルの役割定義*

```text
/
├── GEMINI.md           # 🧠 Core: AIの行動指針・人格・プロトコル定義
├── GEMINI_AGENTS.md    # 🗺️ Context: プロジェクトの仕様・地図・制約（本ファイル）
├── GEMINI_DEV_FLOW.md  # 🌊 Workflow: 開発フローとコマンド手順書
├── GEMINI_DEV_LOG.md   # 📝 Memory: 開発ログ・意思決定・反省の記録
└── (Not yet initialized)
```

### 2-3. Dev Cheatsheet
*開発によく使うコマンド集*

* **Setup:** (未定義)

* **Run Local**: (未定義)

* **Test**: (未定義)

* **Deploy**: (未定義)

---