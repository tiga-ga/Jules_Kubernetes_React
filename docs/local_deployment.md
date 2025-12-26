# ローカル環境デプロイ手順書

本ドキュメントでは、ローカル環境（Minikube）にてアプリケーションをデプロイおよび実行する手順について説明します。

## 1. 前提条件

開発およびデプロイを行うためには、以下のツールがインストールされている必要があります。

*   **Docker**: コンテナイメージのビルドに使用します。
*   **Minikube**: ローカル環境でのKubernetesクラスタとして使用します。
*   **kubectl**: Kubernetesクラスタの操作に使用します。

## 2. 環境セットアップ

まず、Minikubeを起動してKubernetesクラスタを準備します。

```bash
minikube start
```

## 3. デプロイ手順

アプリケーションのデプロイには、自動化スクリプトを使用する方法（推奨）と、手動でコマンドを実行する方法の2通りがあります。

### 方法A: デプロイスクリプトを使用する（推奨）

プロジェクトルートにある `deploy.sh` スクリプトを使用することで、ビルドからデプロイまでを一括で行うことができます。

```bash
# スクリプトに実行権限を付与（初回のみ）
chmod +x deploy.sh

# デプロイを実行
./deploy.sh
```

このスクリプトは以下の処理を自動で行います：
1.  Dockerイメージ (`my-flask-app:latest`) のビルド
2.  ビルドしたイメージのMinikubeへのロード
3.  `k8s/` ディレクトリ内のマニフェストファイルの適用

### 方法B: 手動でデプロイする

手動でステップごとに実行する場合は、以下の手順に従ってください。

1.  **Dockerイメージのビルド**
    ```bash
    docker build -t my-flask-app:latest .
    ```

2.  **Minikubeへのイメージロード**
    Minikubeクラスタ内でイメージを利用できるようにロードします。
    ```bash
    minikube image load my-flask-app:latest
    ```

3.  **Kubernetesリソースの作成**
    マニフェストファイルを適用してDeploymentやServiceを作成します。
    ```bash
    kubectl apply -f k8s/
    ```

## 4. 動作確認

デプロイが完了したら、アプリケーションが正常に稼働しているか確認します。

### Podの状態確認

以下のコマンドでPodの状態を確認します。

```bash
kubectl get pods
```

`flask-app` で始まる名前のPodが表示され、`STATUS` が `Running` になっていれば起動成功です。

### アプリケーションへのアクセス

Minikubeの機能を使用して、ブラウザからアプリケーションにアクセスします。

```bash
minikube service flask-app-service
```

このコマンドを実行すると、デフォルトブラウザが立ち上がり、アプリケーションのトップページが表示されます。

## 5. クリーンアップ

作成したリソース（Deployment, Service, Ingressなど）を削除する場合は、以下のコマンドを実行します。

```bash
kubectl delete -f k8s/
```
