import requests

# アップロードするファイルのパス
file_path = "input/sample.txt"

# API エンドポイント
url = "http://127.0.0.1:8000/upload_file/"

# ファイルをアップロード
with open(file=file_path, mode="rb") as file:
    files = {"file": file}
    response = requests.post(url=url, files=files)

# レスポンスを表示
print(response.json())
