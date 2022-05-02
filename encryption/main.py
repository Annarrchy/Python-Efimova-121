import uvicorn
from fastapi import FastAPI, File, UploadFile
from encryption import encrypt

app = FastAPI()

@app.post("/")
async def api_data(input_file: UploadFile, cipher: str, language: str, key: str):
	return encrypt(cipher, input_file.filename, language, key)
