## 概要

Fast API でファイルのアップロードとダウンロードを行うサンプル

## 環境構築

```bash
conda create -n py311_fastapi_upload_download python=3.11 -y

conda activate py311_fastapi_upload_download

pip install -r requirements.txt
```

## サーバー起動

```bash
uvicorn server:app --reload
```

## クライアント実行

```bash
python client.py
```
