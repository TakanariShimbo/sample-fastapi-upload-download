import os

from fastapi import FastAPI, File, UploadFile
import aiofiles


# 保存ディレクトリ
UPLOAD_DIR = "output"
os.makedirs(name=UPLOAD_DIR, exist_ok=True)

app = FastAPI()


@app.post(path="/upload_files/")
async def upload_files(files: list[UploadFile] = File(...)):
    uploaded_file_paths = []

    for file in files:
        # 保存するファイルのパス
        file_path = os.path.join(UPLOAD_DIR, file.filename)
        uploaded_file_paths.append(file_path)

        # ファイルを非同期で保存
        async with aiofiles.open(file=file_path, mode="wb") as f:
            content = await file.read()
            await f.write(content)

    return {"message": "Files uploaded successfully", "paths": uploaded_file_paths}
