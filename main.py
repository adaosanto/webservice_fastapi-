from fastapi import FastAPI
from api.v1.api import api_router

from core.config import settings

app = FastAPI(title='API')
app.include_router(api_router, prefix=settings.API_V1_STR)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run('main:app', reload=True)



"""
"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0eXBlIjoiYWNlc3NfdG9rZW4iLCJleHAiOjE2NzE0ODY0NjksImlhdCI6MTY3MDg4MTY2OSwic3ViIjoiMSJ9.llsCMHXq_5gm2zhoERegash2jxuT9Mw_rzUUcDMW7no
"""