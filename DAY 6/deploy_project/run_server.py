import uvicorn
import os
from dotenv import load_dotenv

if __name__ == "__main__":
    # Load environment configs
    load_dotenv("configs/.env")
    port = int(os.getenv("API_PORT", 8000))
    
    print(f"🚀 Starting API in {os.getenv('MODEL_ENV')} mode on port {port}")
    uvicorn.run("app.main:app", host="0.0.0.0", port=port, reload=False)
