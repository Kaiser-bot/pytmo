# main.py (en la raíz del proyecto)
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routers import manga
from config.config import settings

app = FastAPI(
    title="Manga API",
    description="API para obtener información de mangas",
    # Configuración opcional para documentación
    docs_url=f"{settings.API_PREFIX}/docs",
    redoc_url=f"{settings.API_PREFIX}/redoc",
    openapi_url=f"{settings.API_PREFIX}/openapi.json"
)

# Configuración CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Registro de rutas
app.include_router(manga.router, prefix=settings.API_PREFIX)

if __name__ == "__main__":
    import uvicorn
    # Corrige la línea para ejecutar directamente el objeto app
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)