# GEMINI_DEV_FLOW.md

## 1. 概要 (Manifesto)
このドキュメントは、**「思考（GEMINI.md）」**と**「地図（GEMINI_AGENTS.md）」**を用いた、**ドキュメント駆動型バイブコーディング (DDVC)** の標準プロトコルです。
我々の開発は「いきなりコードを書く」のではなく、「バイブをドキュメントに定着させてからコードに落とす」プロセスを徹底します。

---

## 2. ゼロからのスタート (Setup Phase)
プロジェクト開始時に1回だけ行うイニシャライズ手順です。

1.  **ファイルの配置:**
    * ルートに `GEMINI.md`, `GEMINI_AGENTS.md`, `GEMINI_DEV_FLOW.md`, `GEMINI_DEV_LOG.md` を配置。
2.  **AGENTS.md の記入:**
    * `GEMINI_AGENTS.md` の「Project Overview」と「Constraints」を埋める。
3.  **キックオフ・プロンプト:**
    * AIチャット（Cursor/Windsurf等）で以下を送信し、私（AI）と同期する。

> 「プロジェクトを開始します。GEMINI.md と GEMINI_AGENTS.md を読み込み、未定の技術スタック（Unselected部分）について提案を行ってください。」

---

## 3. 日常の開発サイクル (The DDVC Loop)
機能を実装する際は、以下の **4ステップ** を1サイクルとして回します。

### STEP 1: Vibe Input (要望の入力)
自然言語で、実現したい機能の「ゴール」や「雰囲気」を伝えてください。
* 🗣️ **You:** 「ログイン画面を作りたい。Google認証で、シュッとした感じで。」
* 🗣️ **You:** 「ユーザーがタスク登録できるAPIを生やして。」

### STEP 2: Doc Update (地図の更新)
私はコードを書く前に、まず**ドキュメント（仕様・設計）の更新**を提案します。
* 🤖 **AI:** `GEMINI_AGENTS.md` や `docs/` 以下の変更案を提示。
* 👉 **Action:** その仕様で良いか確認。「OK」「ここはこう変えて」と合意形成を行う。

### STEP 3: Implementation (実装)
ドキュメントの合意が取れて初めて、コードを生成します。
* 🤖 **AI:** `GEMINI_AGENTS.md` の技術スタックと制約に従ってコーディング。
* ⚠️ **Warning:** もし私が勝手にライブラリを追加しようとしたら、「`GEMINI_AGENTS.md` に記載がないぞ」と指摘してください。

### STEP 4: Verification & Log (検証と記録)
実装完了後の「完了宣言」プロセスです。
* 👉 **Action:** 実際に動かして動作確認。
* 🤖 **AI:** 重要な変更や学びを `GEMINI_DEV_LOG.md` に記録し、`GEMINI_AGENTS.md` の構成情報（Architecture Registry）を最新化する。

---

## 4. シーン別対応ガイド (Use Cases)

### ケースA: 技術選定を相談したい (Architecting)
`GEMINI_AGENTS.md` で未定の項目を決める場合。
* **Prompt:**
    > 「バックエンドの構成を決めたい。`GEMINI_AGENTS.md` の要件に基づいて、GoとPythonのどちらが良いか、理由付きで比較提案して。」

### ケースB: バグ修正 (Bug Fix)
ロジックに関わる修正は、必ず「仕様」から疑う。
* **Prompt:**
    > 「計算ロジックにバグがある気がする。修正してほしいが、仕様自体が間違っている可能性があるので、まず `GEMINI_AGENTS.md` (または該当ドキュメント) の記述を確認して。」

### ケースC: 開発再開 (Context Resume)
久しぶりの開発で、AIに記憶を取り戻させる。
* **Prompt:**
    > 「開発を再開する。`GEMINI_AGENTS.md` と `GEMINI_DEV_LOG.md` を読んで、現在のプロジェクトの状態と、前回やり残したタスクを教えて。」

---

## 5. 禁忌 (Anti-Patterns)
以下の行動はプロジェクトの崩壊（スパゲッティ化）を招くため禁止とする。

* ❌ **ドキュメント無視:** 「面倒だからとりあえず動くコード書いて」と指示する。（→ 将来の負債確定）
* ❌ **AGENTSの手動更新忘れ:** 新しいライブラリを入れたのに `GEMINI_AGENTS.md` に書かない。（→ AIが幻覚を見る原因）
* ❌ **英語での指示:** `GEMINI.md` で日本語思考を指定しているため、英語指示はペルソナのブレを招く。

---

## 6. 完了の定義 (Definition of Done)
タスク完了とは、以下の3点が揃った状態を指す。

1.  ✅ **Code:** コードが動作し、テストが通る。
2.  ✅ **Map:** `GEMINI_AGENTS.md` (構成図) が実態と一致している。
3.  ✅ **Memory:** `GEMINI_DEV_LOG.md` に作業ログが残っている。