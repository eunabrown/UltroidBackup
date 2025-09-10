import os
import nest_asyncio
import uvicorn
from fastapi import FastAPI

app = FastAPI(
    title="UltXtraHF",
    version="1.0.2",
    contact={
        "name": "🌀ʊʄ⊕ք🌀",
        "url": "https://github.com/ufoptg/UltroidBackup/",
    },
    docs_url=None,
    redoc_url="/"
)

@app.get("/status")
def status():
    return {"message": "running"}

if __name__ == "__main__":
    nest_asyncio.apply()
    PORT = os.getenv("PORT")
    uvicorn.run(app, host="0.0.0.0", port=PORT)
