# GenAI Deployment Project

## Structure
- `/app`: FastAPI deployment stubs
- `/artifacts`: Pickled models and `eval_report.json`
- `/configs`: `.env` environment variables

## Quickstart
1. Install dependencies: `pip install fastapi uvicorn python-dotenv`
2. Run server: `python run_server.py`
3. Test API: `curl -X POST http://localhost:8000/predict -d '{"prompt": "hello"}'`
