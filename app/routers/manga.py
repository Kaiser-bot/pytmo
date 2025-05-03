# app/routers/manga.py
from fastapi import APIRouter, Query, HTTPException
from typing import Optional
from ..services.scraper import MangaScraper
from ..models import ApiResponse

router = APIRouter()
scraper = MangaScraper()


@router.get("/manga/populares", response_model=ApiResponse)
async def get_popular_manga(pageNumber: int = Query(1)):
    """Obtiene los mangas populares para una página específica"""
    try:
        mangas = scraper.get_populares(page_number=pageNumber)
        return ApiResponse(statusCode=200, data=mangas)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))



@router.get("/manga/populares-seinen", response_model=ApiResponse)
async def get_popular_seinen(pageNumber: int = Query(1)):
    """Obtiene los mangas populares de demografía Seinen"""
    try:
        mangas = scraper.get_populares_seinen(page_number=pageNumber)
        return ApiResponse(statusCode=200, data=mangas)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/manga/populares-josei", response_model=ApiResponse)
async def get_popular_josei(pageNumber: int = Query(1)):
    """Obtiene los mangas populares de demografía Josei"""
    try:
        mangas = scraper.get_populares_josei(page_number=pageNumber)
        return ApiResponse(statusCode=200, data=mangas)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/get-manga", response_model=ApiResponse)
async def get_chapter_images(urlPage: str, urlRefer: Optional[str] = None):
    """Obtiene las imágenes de un capítulo específico"""
    try:
        if not urlPage:
            return ApiResponse(statusCode=400, data="El parámetro urlPage es requerido")

        images = scraper.get_chapter_images(chapter_url=urlPage, referer_url=urlRefer)

        if not images:
            return ApiResponse(statusCode=404, data="No se encontraron imágenes para mostrar")

        return ApiResponse(statusCode=200, data=images)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@router.get("/manga/library", response_model=ApiResponse)
async def search_manga(
    title: Optional[str] = None,
    _pg: int = 1,
    order_item: str = "likes_count",
    order_dir: str = "desc",
    filter_by: Optional[str] = None,
    Type: Optional[str] = None,
    demography: Optional[str] = None,
    status: Optional[str] = None,
    genres: Optional[str] = None,         # Añadir géneros
    exclude_genres: Optional[str] = None  # Añadir exclusión de géneros
):
    """Busca mangas según los criterios proporcionados"""
    try:
        results = scraper.search_manga(
            title=title,
            page=_pg,
            order_item=order_item,
            order_dir=order_dir,
            filter_by=filter_by,
            manga_type=Type,
            demography=demography,
            status=status,
            genres=genres,               # Pasar los géneros
            exclude_genres=exclude_genres # Pasar la exclusión de géneros
        )

        return ApiResponse(statusCode=200, data=results)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/manga/info", response_model=ApiResponse)
async def get_manga_details(mangaUrl: str):
    """Obtiene información detallada de un manga específico"""
    try:
        if not mangaUrl:
            return ApiResponse(statusCode=400, data="El parámetro mangaUrl es requerido")

        manga_info = scraper.get_manga_info(manga_url=mangaUrl)
        return ApiResponse(statusCode=200, data=manga_info)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/manga/{manga_url:path}/grupos")
async def get_manga_grupos(manga_url: str):
    """
    Obtiene los grupos que han trabajado en un manga específico
    """
    try:
        # Asegurarse de que manga_url es una URL completa
        if not manga_url.startswith("http"):
            manga_url = f"{scraper.base_url}/{manga_url}"

        grupos = scraper.get_manga_grupos(manga_url)
        return {
            "status": "success",
            "total": len(grupos),
            "grupos": grupos
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error al obtener los grupos: {str(e)}")