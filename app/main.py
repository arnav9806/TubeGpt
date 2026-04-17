from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.v1.api import api_router
from app.db.session import engine
from app.db.base import Base

# Create DB tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="TubeGPT API",
    version="1.0.0",
    description="AI-powered YouTube Assistant"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routes
app.include_router(api_router, prefix="/api/v1")


@app.get("/")
def root():
    return {"message": "TubeGPT Backend Running 🚀"}