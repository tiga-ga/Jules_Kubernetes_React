# フロントエンド設計書 (Frontend Design)

## 概要
React + Vite を使用したSPA (Single Page Application) の設計。
ユーザーはダッシュボードで成果物を管理する。

## 画面構成

### 1. ダッシュボード (Main View)
* **ヘッダー:** アプリケーションタイトルを表示。
* **統計エリア (Future):** 今月のアウトプット数などを表示。
* **新規登録ボタン:** 登録モーダルを開くFABまたはボタン。
* **成果物リスト:** APIから取得したデータをカードまたはリスト形式で表示。
    * 各アイテムに「編集」「削除」ボタンを配置。

### 2. 登録/編集モーダル (Modal)
* **タイトル:** 入力 (Text)
* **URL:** 入力 (URL type)
* **種別:** セレクトボックス (Blog, Video, Other)
* **日付:** カレンダーピッカー
* **コメント:** テキストエリア
* **アクション:** 保存 / キャンセル

## コンポーネント設計 (Components)

* `App.jsx`: ルーティングとメインレイアウト。
* `components/Header.jsx`: ヘッダー部分。
* `components/OutputList.jsx`: `outputs`配列を受け取り、リストを描画。
* `components/OutputItem.jsx`: 個別の成果物表示用コンポーネント。
* `components/OutputFormModal.jsx`: 新規登録・編集兼用のモーダルフォーム。
* `hooks/useOutputs.js`: API通信 (Axios/Fetch) を管理するカスタムフック。

## 状態管理 (State Management)
* シンプルなアプリのため、React Context またはローカルステート (`useState`, `useReducer`) で管理する。
* 必要に応じて `TanStack Query` (React Query) の導入を検討（サーバー状態の管理）。
