from src.core.server import app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("src.core.server:app", reload=True)
