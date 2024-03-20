# Commodity_Thief
Микросервис на fastapi для парсинга сайтов поставщиков для tokkaritailor

Работать все должно по такой схеме:
[Main]
  |
  +--> [Data Collection] -----> [External Websites]
  |        |           \        
  |        V            -> [Utilities]
  |    [Data Processing]        
  |        |
  +--> [Database] <----> [API Integration] -----> [External Backend API]
               \
                -> [Utilities]


project_root/
│
├── data_collection/
│   ├── __init__.py
│   ├── scraper.py (общий интерфейс или базовый класс для сканеров)
│   └── scanners/     (директория со сканерами для каждого сайта)
│       ├── __init__.py
│       ├── site_a_scanner.py
│       ├── site_b_scanner.py
│       └── ...       (и так далее для каждого сайта)
│ 
├── data_processing/
│   ├── __init__.py
│   ├── data_cleaner.py
│   └── data_transformer.py
│
├── database/
│   ├── __init__.py
│   ├── models.py
│   └── db_manager.py
│
├── api_integration/
│   ├── __init__.py
│   ├── api_client.py
│   └── data_exporter.py
│
├── utilities/
│   ├── __init__.py
│   ├── logger.py # наверное?
│   └── config.py
│
└── main.py


Данные собираются с сайтов поставщиков, потом происходит валидация, после чего они записываются в копию бд как на ядре tokkaritailor. Потом уже готовая бд парсера копируется на проект. 

В теории можно будет перезапускать парсер отдельно, но это потом.