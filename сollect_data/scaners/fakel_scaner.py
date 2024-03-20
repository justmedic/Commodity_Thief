# import sys
# sys.path.append(r"C:\Users\bychk\Desktop\Commodity_Thief\сollect_data\scaners")

from scaner import AsyncScanner
import asyncio
import aiohttp
import xml.etree.ElementTree as ET

async def fetch_sitemap(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            response.raise_for_status()  # В случае ошибочного ответа возбуждает исключение :^)
            text = await response.text()
            return text

def find_catalog_links(xml_data):
    root = ET.fromstring(xml_data)
    catalog_links = []

    for url in root.findall('.//{http://www.sitemaps.org/schemas/sitemap/0.9}url'):
        loc = url.find('{http://www.sitemaps.org/schemas/sitemap/0.9}loc')
        if loc is not None and 'catalog' in loc.text:
            catalog_links.append(loc.text)
    
    return catalog_links

async def get_catalog_links(sitemap_url):
    sitemap_xml = await fetch_sitemap(sitemap_url)
    catalog_links = find_catalog_links(sitemap_xml)
    return catalog_links


sitemap_url = 'https://f-tk.ru/sitemap.xml'
catalog_links = asyncio.run(get_catalog_links(sitemap_url)) # список юрлов на товары


