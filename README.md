

## Архитектура проекта

Микросервис на FastAPI для парсинга сайтов поставщиков для tokkaritailor работает по следующей схеме:

```
[Main]
  |
  +--> [Data Collection] -----> [External Websites]
  |        |
  |        V
  |    [Utilities]
  |
  +--> [Data Processing]
  |        |
  |        +--> [Database] <----> [API Integration] -----> [External Backend API]
  |                               |
  |                               V
  +----------------------------> [Utilities]
```

### Структура директорий проекта:

```
project_root/
│
├── data_collection/
│   ├── __init__.py
│   ├── scraper.py  # Общий интерфейс или базовый класс для сканеров
│   └── scanners/   # Директория со сканерами для каждого сайта
│       ├── __init__.py
│       ├── site_a_scanner.py
│       ├── site_b_scanner.py
│       └── ...    # и так далее для каждого сайта
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
│   ├── logger.py  # наверное?
│   └── config.py
│
└── main.py
```

### Процесс работы:

1. Данные собираются с сайтов поставщиков.
2. Затем происходит их валидация.
3. После чего они записываются в копию базы данных как на ядре tokkaritailor.
4. Готовая база данных парсера копируется на проект.

В теории можно будет перезапускать парсер отдельно, но это планируется реализовать позже.
```
