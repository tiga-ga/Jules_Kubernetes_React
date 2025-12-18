# Flask App Kubernetes Setup

このリポジトリには、FlaskアプリケーションをローカルのKubernetes環境で実行するための設定ファイルが含まれています。

## 前提条件

以下のツールがインストールされていることを確認してください。

*   Docker
*   kubectl
*   Minikube

## 手順

### 1. Dockerイメージのビルド

まず、アプリケーションのDockerイメージをビルドします。`k8s/deployment.yaml`で指定されているイメージ名 `my-flask-app:latest` と一致させる必要があります。

```bash
docker build -t my-flask-app:latest .
```

### 2. イメージの読み込み

ビルドしたイメージをMinikubeのクラスタ内に読み込む必要があります。

```bash
minikube image load my-flask-app:latest
```

### 3. アプリケーションのデプロイ

Kubernetesのマニフェストファイルを適用して、アプリケーションをデプロイします。

```bash
kubectl apply -f k8s/
```

### 4. デプロイの確認

Podが正常に起動しているか確認します。

```bash
kubectl get pods
```

ステータスが `Running` になるまで待ちます。

### 5. アプリケーションへのアクセス

Serviceは `ClusterIP` タイプとして定義されているため、ローカルからアクセスするにはポートフォワードを使用するのが最も簡単です。

```bash
kubectl port-forward service/flask-app-service 8080:80
```

ブラウザで [http://localhost:8080](http://localhost:8080) にアクセスして、アプリケーションが表示されることを確認してください。

## クリーンアップ

リソースを削除するには、以下のコマンドを実行します。

```bash
kubectl delete -f k8s/
```
