# PyTmo

Este proyecto proporciona una API REST para obtener información de mangas desde zonatmo.com, incluyendo listados populares, detalles, capítulos e imágenes.

## Requisitos

- Python 3.8+
- FastAPI
- BeautifulSoup4
- Requests
- Pydantic

## Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/Kaiser-bot/pytmo.git
   cd pytmo
   ```

2. Instalar dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Ejecución

Para iniciar el servidor:

```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

## Endpoints Disponibles

### 1. Mangas Populares

**Endpoint**: `/api/v1/manga/populares`  
**Método**: GET  
**Parámetros**:
- `pageNumber` (int, opcional): Número de página (default: 1)

**Ejemplo de respuesta**:
```json
{
  "statusCode": 200,
  "data": [
    {
      "title": "One Piece",
      "score": "9.50",
      "type": "MANGA",
      "demography": "Shonen",
      "mangaUrl": "https://zonatmo.com/manga/one-piece",
      "mangaImagen": "https://zonatmo.com/uploads/covers/one-piece.jpg"
    }
  ]
}
```

### 2. Mangas Populares Seinen

**Endpoint**: `/api/v1/manga/populares-seinen`  
**Método**: GET  
**Parámetros**:
- `pageNumber` (int, opcional): Número de página (default: 1)

**Ejemplo de respuesta**: Similar al anterior, filtrado por demografía Seinen.

### 3. Mangas Populares Josei

**Endpoint**: `/api/v1/manga/populares-josei`  
**Método**: GET  
**Parámetros**:
- `pageNumber` (int, opcional): Número de página (default: 1)

**Ejemplo de respuesta**: Similar al anterior, filtrado por demografía Josei.

### 4. Imágenes de Capítulo

**Endpoint**: `/api/v1/get-manga`  
**Método**: GET  
**Parámetros**:
- `urlPage` (string, requerido): URL del capítulo
- `urlRefer` (string, opcional): URL de referencia

**Ejemplo de respuesta**:
```json
{
  "statusCode": 200,
  "data": [
    "https://zonatmo.com/uploads/chapters/123/1.jpg",
    "https://zonatmo.com/uploads/chapters/123/2.jpg"
  ]
}
```

### 5. Búsqueda de Mangas

**Endpoint**: `/api/v1/manga/library`  
**Método**: GET  
**Parámetros**:
- `title` (string, opcional): Título para búsqueda
- `_pg` (int, opcional): Página (default: 1)
- `order_item` (string, opcional): Campo para ordenar (default: "likes_count")
- `order_dir` (string, opcional): Dirección de orden (default: "desc")
- `filter_by` (string, opcional): Filtro adicional
- `Type` (string, opcional): Tipo de manga
- `demography` (string, opcional): Demografía
- `status` (string, opcional): Estado
- `genres` (string, opcional): Géneros separados por comas
- `exclude_genres` (string, opcional): Géneros a excluir

**Ejemplo de respuesta**: Similar al primer ejemplo.

### 6. Detalles de Manga

**Endpoint**: `/api/v1/manga/info`  
**Método**: GET  
**Parámetros**:
- `mangaUrl` (string, requerido): URL del manga

**Ejemplo de respuesta**:
```json
{
  "statusCode": 200,
  "data": {
    "title": "One Piece",
    "image": "https://zonatmo.com/uploads/covers/one-piece.jpg",
    "tipo": "MANGA",
    "score": "9.50",
    "demografia": "Shonen",
    "descripcion": "La historia de un chico que quiere ser el Rey de los Piratas...",
    "estado": "En emisión",
    "generos": ["Aventura", "Acción", "Comedia"],
    "capitulo": [
      {
        "Title": "Capítulo 1000 [MangaPlus] (2023-01-15) ESP",
        "UrlLeer": "https://zonatmo.com/one-piece/1000/mangaplus"
      }
    ],
    "subtitle": "Subtítulo del manga",
    "titulos_alt": ["ワンピース", "Wan Pīsu"]
  }
}
```

## Notas Adicionales

- Todos los endpoints usan el prefijo configurado en `API_PREFIX` ("/api/v1" por defecto)
- La API devuelve códigos de estado HTTP estándar
- Las respuestas siguen el formato `ApiResponse` con los campos `statusCode` y `data`

## Créditos
- Basé este proyecto en el trabajo previo de [julioolivares90](https://github.com/julioolivares90) (su repositorio [TuMangaOnline-api](https://github.com/julioolivares90/TuMangaOnline-api)).
- Usé Claude 3.7 como apoyo durante el desarrollo y la documentación. 
