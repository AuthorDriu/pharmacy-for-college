## Инструкция по запуску сервера

**ВАЖНО Разработка сервера ведётся на версии Python3.11, так что рекоммедуется запускать сервер на этой же версии**

Поскольку проект приватный, тебе нужно подтвердить, что ты имеешь доступ к проекту.
Установив в VS Code расширение `GitHub Pull Requests` ты сможешь сделать это без заморочек. Иначе придётся разбираться с Access токенами, а я не хочу этого (мне лень).

Пропиши команду: `git clone https://github.com/AuthorDriu/pharmacy-for-college.git` в директории, куда хочешь установить проект.
Она скопирует директорию проекта в локальную директорию. Расширение `GitHub Pull Requests` спросит разрешение перейти в GitHub, чтоб подтвердить твой доступ. Разрешай не боись.

Потом перейди в каталог проекта и создай виртуальное окружение командой `python3 -m venv venv` (на Windows не python3, а py).
После этого активируй его скриптом, который находится в `venv/bin/activate` на Linux, или `venv/Scripts/activate.bat` на Windows.
Установи все зависимости проекта командой `python3 -m pip install -r requirements.txt`. Если возникнут проблемы с зависимости для зависимостей - решай сам :kissing_heart:.

Чтоб запустить сервер используй команду `uvicorn src.app:app`. Это запустит сервер. Ты сможешь увидеть результат вбив в поисковую строку браузера `http://127.0.0.1:8000`.

## Используемые материалы при написании системы
- Курс по FastAPI: https://youtube.com/playlist?list=PLeLN0qH0-mCVQKZ8-W1LhxDcVlWtTALCS&si=MUBeBteLrOy_W0xP
- Курс по Sqlalchemy: https://www.youtube.com/playlist?list=PLeLN0qH0-mCXARD_K-USF2wHctxzEVp40
- Курс по bootstrap 5: https://youtube.com/playlist?list=PL0lO_mIqDDFUQI5lrRlZfkApMWtJJ7GFE&si=kjKxRd1xagFzYFkd
- Курс по Jinja2: https://www.youtube.com/playlist?list=PLA0M1Bcd0w8wfmtElObQrBbZjY6XeA06U