from fastapi import FastAPI
from .routes import auth, programs
from .config import engine
from .models import Base

app = FastAPI()
Base.metadata.create_all(bind=engine)

# Register routers
app.include_router(auth.router)
app.include_router(programs.router)
