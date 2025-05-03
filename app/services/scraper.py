# Código completo de app/services/scraper.py con los cambios aplicados:

import re
import requests
from bs4 import BeautifulSoup
from typing import List, Dict, Any, Optional
from config.config import settings
from ..models import MangaPreview, MangaInfo, Chapter


class MangaScraper:
    def __init__(self):
        self.base_url = settings.BASE_URL
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }

    def get_populares(self, page_number: int = 1, demography: str = None) -> list:
        url = f"{settings.MANGA_BASE_URL}populars?page={page_number}"
        if demography:
            url += f"&demography={demography}"

        print(f"Accediendo a URL: {url}")  # Para depuración

        response = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        mangas = []
        # Selecciona los elementos con la clase "element" dentro del contenedor
        elements = soup.select('div.element')

        for element in elements:
            try:
                # Obtener el enlace y URL del manga
                link_element = element.select_one('a')
                manga_url = link_element['href'] if link_element else ""

                # Obtener el título del manga
                title_element = element.select_one('.thumbnail-title h4')
                title = title_element.get('title', "") if title_element else ""

                # Obtener puntuación
                score_element = element.select_one('.score span')
                score = score_element.text.strip() if score_element else "0.00"

                # Obtener tipo de libro (MANGA, MANHWA, etc.)
                type_element = element.select_one('.book-type')
                manga_type = type_element.text.strip() if type_element else ""

                # Obtener demografía
                demography_element = element.select_one('.demography')
                demography = demography_element.text.strip() if demography_element else ""

                # Obtener URL de imagen desde el estilo CSS
                style_element = element.select_one('style')
                if style_element and style_element.text:
                    image_match = re.search(r"background-image: url\('([^']+)'\)", style_element.text) or \
                                  re.search(r"url\('([^']+)'\)", style_element.text)
                    image_url = image_match.group(1) if image_match else ""
                else:
                    image_url = ""

                # Crear objeto MangaPreview
                manga = MangaPreview(
                    title=title,
                    score=score,
                    type=manga_type,
                    demography=demography,
                    mangaUrl=manga_url,
                    mangaImagen=image_url
                )
                mangas.append(manga)
            except Exception as e:
                print(f"Error extrayendo manga: {e}")

        return mangas

    def get_populares_seinen(self, page_number: int = 1) -> list:
        url = f"{settings.MANGA_BASE_URL}populars-boys"
        if page_number > 1:
            url += f"?page={page_number}"

        print(f"Accediendo a URL Seinen: {url}")  # Para depuración

        response = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        mangas = []
        elements = soup.select('div.element')

        for element in elements:
            try:
                # Obtener el enlace y URL del manga
                link_element = element.select_one('a')
                manga_url = link_element['href'] if link_element else ""

                # Obtener el título del manga
                title_element = element.select_one('.thumbnail-title h4')
                title = title_element.get('title', "") if title_element else ""

                # Obtener puntuación
                score_element = element.select_one('.score span')
                score = score_element.text.strip() if score_element else "0.00"

                # Obtener tipo de libro (MANGA, MANHWA, etc.)
                type_element = element.select_one('.book-type')
                manga_type = type_element.text.strip() if type_element else ""

                # Obtener demografía
                demography_element = element.select_one('.demography')
                demography = demography_element.text.strip() if demography_element else "Seinen"

                # Obtener URL de imagen desde el estilo CSS
                style_element = element.select_one('style')
                if style_element and style_element.text:
                    image_match = re.search(r"background-image: url\('([^']+)'\)", style_element.text) or \
                                  re.search(r"url\('([^']+)'\)", style_element.text)
                    image_url = image_match.group(1) if image_match else ""
                else:
                    image_url = ""

                # Crear objeto MangaPreview
                manga = MangaPreview(
                    title=title,
                    score=score,
                    type=manga_type,
                    demography=demography,
                    mangaUrl=manga_url,
                    mangaImagen=image_url
                )
                mangas.append(manga)
            except Exception as e:
                print(f"Error extrayendo manga seinen: {e}")

        return mangas

    def get_populares_josei(self, page_number: int = 1) -> list:
        url = f"{settings.MANGA_BASE_URL}populars-girls"
        if page_number > 1:
            url += f"?page={page_number}"

        print(f"Accediendo a URL Josei: {url}")  # Para depuración

        response = requests.get(url, headers=self.headers)
        soup = BeautifulSoup(response.text, 'html.parser')

        mangas = []
        elements = soup.select('div.element')

        for element in elements:
            try:
                # Obtener el enlace y URL del manga
                link_element = element.select_one('a')
                manga_url = link_element['href'] if link_element else ""

                # Obtener el título del manga
                title_element = element.select_one('.thumbnail-title h4')
                title = title_element.get('title', "") if title_element else ""

                # Obtener puntuación
                score_element = element.select_one('.score span')
                score = score_element.text.strip() if score_element else "0.00"

                # Obtener tipo de libro (MANGA, MANHWA, etc.)
                type_element = element.select_one('.book-type')
                manga_type = type_element.text.strip() if type_element else ""

                # Obtener demografía
                demography_element = element.select_one('.demography')
                demography = demography_element.text.strip() if demography_element else "Josei"

                # Obtener URL de imagen desde el estilo CSS
                style_element = element.select_one('style')
                if style_element and style_element.text:
                    image_match = re.search(r"background-image: url\('([^']+)'\)", style_element.text) or \
                                  re.search(r"url\('([^']+)'\)", style_element.text)
                    image_url = image_match.group(1) if image_match else ""
                else:
                    image_url = ""

                # Crear objeto MangaPreview
                manga = MangaPreview(
                    title=title,
                    score=score,
                    type=manga_type,
                    demography=demography,
                    mangaUrl=manga_url,
                    mangaImagen=image_url
                )
                mangas.append(manga)
            except Exception as e:
                print(f"Error extrayendo manga josei: {e}")

        return mangas

    def get_manga_grupos(self, manga_url):
        """Obtiene los grupos que han trabajado en un manga específico"""
        response = requests.get(manga_url, headers=self.headers)
        soup = BeautifulSoup(response.text, "html.parser")

        # Diccionario para almacenar información de grupos
        grupos = {}

        # Buscar todos los capítulos
        chapter_headers = soup.select("li.list-group-item.p-0.bg-light")

        for chapter_header in chapter_headers:
            # Buscar grupos dentro de cada capítulo
            upload_items = chapter_header.select("ul.chapter-list li.list-group-item")

            for upload_item in upload_items:
                # Extraer información del grupo
                group_element = upload_item.select_one("div.col-4.col-md-6 a")
                if not group_element:
                    continue

                grupo_nombre = group_element.text.strip()
                grupo_url = group_element.get("href", "")

                # Extraer fecha si está disponible
                date_element = upload_item.select_one("span.badge.badge-primary")
                fecha = date_element.text.replace("2025-", "").strip() if date_element else ""

                # Actualizar información del grupo
                if grupo_nombre not in grupos:
                    grupos[grupo_nombre] = {
                        "nombre": grupo_nombre,
                        "url": grupo_url,
                        "capitulos": 1,
                        "ultima_actividad": fecha
                    }
                else:
                    grupos[grupo_nombre]["capitulos"] += 1
                    # Actualizar última actividad si la nueva fecha es más reciente
                    if fecha and (not grupos[grupo_nombre]["ultima_actividad"] or
                                  fecha > grupos[grupo_nombre]["ultima_actividad"]):
                        grupos[grupo_nombre]["ultima_actividad"] = fecha

        # Convertir diccionario a lista
        return list(grupos.values())

    def get_manga_info(self, manga_url):
        """Obtiene información detallada de un manga específico"""
        response = requests.get(manga_url, headers=self.headers)
        soup = BeautifulSoup(response.text, "html.parser")

        # Extracción de datos básicos (sin cambios)
        title_element = soup.select_one("h1.element-title")
        title = title_element.text.strip() if title_element else ""

        subtitle_element = soup.select_one("h2.element-subtitle")
        subtitle = subtitle_element.text.strip() if subtitle_element else ""

        image_element = soup.select_one(".element-image img.book-thumbnail")
        image = image_element["src"] if image_element and image_element.has_attr("src") else ""

        tipo_element = soup.select_one(".book-type")
        tipo = tipo_element.text.strip() if tipo_element else "MANGA"

        score_element = soup.select_one(".score span")
        score = score_element.text.strip() if score_element else "0.00"

        demografia_element = soup.select_one(".demography")
        demografia = demografia_element.text.strip() if demografia_element else ""

        descripcion_element = soup.select_one(".element-description")
        descripcion = descripcion_element.text.strip() if descripcion_element else ""

        estado_element = soup.select_one(".book-status")
        estado = estado_element.text.strip() if estado_element else ""

        # Géneros (sin cambios)
        generos = []
        generos_elements = soup.select("h5.element-subtitle:contains('Géneros') + h6 a.badge")
        if not generos_elements:
            generos_elements = soup.select("a.badge-primary")

        for genre in generos_elements:
            generos.append(genre.text.strip())

        # Títulos alternativos (sin cambios)
        titulos_alt = []
        alt_titles_section = soup.find("h5", string="Títulos alternativos")
        if alt_titles_section:
            alt_titles = alt_titles_section.find_next_siblings("span")
            for alt in alt_titles:
                titulos_alt.append(alt.text.strip())

        # Capítulos - NUEVA IMPLEMENTACIÓN para múltiples grupos
        capitulos = []
        # Primero identificamos los elementos de cada capítulo
        chapter_headers = soup.select("li.list-group-item.p-0.bg-light")

        for chapter_header in chapter_headers:
            # Obtener el título del capítulo
            title_element = chapter_header.select_one("h4 a.btn-collapse")
            if not title_element:
                continue

            cap_title = title_element.text.strip()

            # Obtener el contenedor de subgrupos
            chapter_id = title_element.get("onclick", "").replace("collapseChapter('collapsible", "").replace("')", "")
            if not chapter_id:
                continue

            # Buscar todos los grupos que han subido este capítulo
            upload_items = chapter_header.select("ul.chapter-list li.list-group-item")

            for upload_item in upload_items:
                # Extraer el grupo
                group_element = upload_item.select_one("div.col-4.col-md-6 a")
                grupo = group_element.text.strip() if group_element else "Desconocido"

                # Extraer la fecha
                date_element = upload_item.select_one("span.badge.badge-primary")
                fecha = date_element.text.replace("2025-", "").strip() if date_element else ""

                # Extraer el idioma
                lang_element = upload_item.select_one("i.flag-icon")
                idioma = lang_element.get("class", [])[1].replace("flag-icon-", "") if lang_element else ""

                # Extraer la URL de lectura
                link_element = upload_item.select_one("a.btn.btn-default")
                if link_element and link_element.has_attr("href"):
                    cap_url = link_element["href"]

                    # Crear título compuesto con información del grupo
                    title_compuesto = f"{cap_title} [{grupo}]"
                    if fecha:
                        title_compuesto += f" ({fecha})"
                    if idioma:
                        title_compuesto += f" {idioma.upper()}"

                    capitulo = Chapter(
                        Title=title_compuesto,
                        UrlLeer=cap_url
                    )
                    capitulos.append(capitulo)

        return MangaInfo(
            title=title,
            image=image,
            tipo=tipo,
            score=score,
            demografia=demografia,
            descripcion=descripcion,
            estado=estado,
            generos=generos,
            capitulo=capitulos,
            subtitle=subtitle,
            titulos_alt=titulos_alt
        )

    def _get_cookies(self):
        """Obtiene cookies necesarias para acceder al contenido"""
        response = requests.get(self.base_url, headers=self.headers)
        return response.cookies

    def search_manga(self, title=None, page=1, order_item="likes_count", order_dir="desc",
                     filter_by=None, manga_type=None, demography=None, status=None,
                     genres=None, exclude_genres=None):
        """Busca mangas según los criterios proporcionados"""
        # URL base para la biblioteca
        url = f"{self.base_url}/library"

        # Corrige los parámetros para que coincidan con zonatmo.com
        params = {"_pg": page}
        if title:
            params["title"] = title
        if order_item:
            params["order_item"] = order_item
        if order_dir:
            params["order_dir"] = order_dir
        if filter_by:
            params["filter_by"] = filter_by
        if manga_type:
            params["type"] = manga_type
        if demography:
            params["demography"] = demography
        if status:
            params["status"] = status
        if genres:
            params["genres[]"] = genres.split(',') if isinstance(genres, str) else genres
        if exclude_genres:
            params["exclude_genres[]"] = exclude_genres.split(',') if isinstance(exclude_genres,
                                                                                 str) else exclude_genres

        print(f"Buscando en: {url} con parámetros: {params}")
        response = requests.get(url, params=params, headers=self.headers)
        soup = BeautifulSoup(response.text, "html.parser")

        manga_list = []
        # Actualiza el selector para que coincida con el HTML real
        manga_items = soup.select("div.element")

        for item in manga_items:
            try:
                # Obtener URL y título
                link_element = item.select_one("a")
                manga_url = link_element["href"].strip() if link_element and link_element.has_attr("href") else ""

                # Título del manga
                title_element = item.select_one(".thumbnail-title h4")
                title = title_element.get("title") or title_element.text.strip() if title_element else ""

                # Puntuación
                score_element = item.select_one(".score span")
                score = score_element.text.strip() if score_element else "0.00"

                # Tipo de manga
                type_element = item.select_one(".book-type")
                manga_type = type_element.text.strip() if type_element else ""

                # Demografía
                demography_element = item.select_one(".demography")
                demography = demography_element.text.strip() if demography_element else ""

                # Imagen (extraída del estilo CSS)
                style_element = item.select_one("style")
                image_url = ""
                if style_element and style_element.text:
                    image_match = re.search(r"background-image: url\('([^']+)'\)", style_element.text)
                    if image_match:
                        image_url = image_match.group(1)

                manga = MangaPreview(
                    title=title,
                    score=score,
                    type=manga_type,
                    demography=demography,
                    mangaUrl=manga_url,
                    mangaImagen=image_url
                )
                manga_list.append(manga)
            except Exception as e:
                print(f"Error extrayendo manga: {e}")

        return manga_list