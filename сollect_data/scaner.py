import asyncio
import aiohttp
from abc import ABC, abstractmethod

class AsyncScanner(ABC):
    def __init__(self, rate_limit):
        self.session = None
        self.rate_limit = rate_limit 
        self.semaphore = asyncio.Semaphore(rate_limit) 
    
    async def fetch(self, url):
        """
        Асинхронный запрос на получение HTML-кода страницы.
        """
        async with self.semaphore:
            async with self.session.get(url) as response:
                response.raise_for_status()  # Генерирует исключение для ответов с ошибкой
                return await response.text()

    @abstractmethod
    async def parse(self, html):
        """
        Абстрактный метод для парсинга HTML-кода.
        Должен быть реализован в дочерних классах.
        """
        pass

    async def run(self, urls):
        """
        Основной метод класса, получает список URL и обрабатывает их с ограничением скорости запросов.
        """
        async with aiohttp.ClientSession() as self.session:
            tasks = [self.process_url(url) for url in urls]
            results = await asyncio.gather(*tasks, return_exceptions=True)
            return results

    async def process_url(self, url):
        """
        Обработка одного URL: запрос + парсинг.
        """
        html = await self.fetch(url)
        await self.parse(html)
