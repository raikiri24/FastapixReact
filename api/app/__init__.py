from fastapi import FastAPI,APIRouter
from app.api.user_profile.route import router as user_profile_router
from app.api.user_post.route import router as user_post_router
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
from fastapi.middleware.cors import CORSMiddleware

def create_app() -> FastAPI:
    app = FastAPI()
    
    init_routers(app)
    init_logging()
    init_database_service(app)
    init_cor_settings(app)
    return app

def init_cor_settings(app: FastAPI):
    
    origins = ["*"]

    app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

def init_logging():
    from app import logging
    logging.init_logger()

   

def init_database_service(
        app: FastAPI
):
    @app.on_event("startup")
    async def startup():
        # create db tables
        from app.service.database.database import Base, engine
        async with engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)



def init_routers(
        app: FastAPI
):
    router = APIRouter()
    templates = Jinja2Templates(directory="../client/dist")
    app.mount('/assets', StaticFiles(directory="../client/dist/assets/"), 'assets')
    
    @router.get('/api/health')
    async def health():
        return { 'status': 'healthy' }
   
    
    @router.get("/{rest_of_path:path}")
    async def react_app(req: Request, rest_of_path: str):
        word_to_find = "api/"

        if word_to_find not in rest_of_path:
           return templates.TemplateResponse('index.html', { 'request': req })
       
        
 
    app.include_router(user_profile_router)
    app.include_router(user_post_router)
    app.include_router(router)