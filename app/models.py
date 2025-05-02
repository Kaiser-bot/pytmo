# app/models.py
from pydantic import BaseModel
from typing import List, Optional, Union, Any

class MangaPreview(BaseModel):
    title: str
    score: str
    type: str
    demography: str
    mangaUrl: str
    mangaImagen: str

class Chapter(BaseModel):
    Title: str
    UrlLeer: str

class MangaInfo(BaseModel):
    title: str
    image: str
    tipo: str
    score: str
    demografia: str
    descripcion: str
    estado: str
    generos: List[str]
    capitulo: List[Chapter]
    subtitle: Optional[str] = ""
    titulos_alt: Optional[List[str]] = []

class ApiResponse(BaseModel):
    statusCode: int
    data: Optional[Union[List[MangaPreview], MangaInfo, List[str], str, Any]] = None