
import uvicorn
import os
from dotenv import load_dotenv

def main():
    load_dotenv()
    host = os.getenv("HOST", "127.0.0.1")
    port = int(os.getenv("PORT", 8000))
    uvicorn.run("main:app", host=host, port=port, reload=True)

if __name__ == "__main__":
    main()
