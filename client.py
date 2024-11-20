import requests

# アップロードするファイルのパス
file_paths = [
    "input/sample.txt",
    "input/sample.mp3",
]

# API エンドポイント
url = "http://127.0.0.1:8000/upload_files/"

# アップロードするファイルを準備
files = [("files", open(file_path, "rb")) for file_path in file_paths]

# ファイルをアップロード
response = requests.post(url=url, files=files)

# レスポンスを表示
print(response.json())
