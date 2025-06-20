# TurbotaBot

**TurbotaBot** — це Telegram-бот з підтримкою GPT, створений для надання моральної підтримки українцям, які не мають можливості звернутися до професійного психолога.

### 💡 Опис проєкту

Цей бот поєднує в собі GPT-інтелект і Telegram, щоб цілодобово надавати емпатичне спілкування та базову емоційну підтримку. Це не заміна терапії, а теплий співрозмовник у важкі моменти.

### 🧠 Основні функції

- Асинхронний Telegram-бот (aiogram)
- Інтеграція GPT-4o для діалогів
- SQLite для збереження історії повідомлень
- FastAPI як бекенд
- Підготовлено до Stripe (донати, платежі)

### 🛠️ Технології

- Python 3.11+
- FastAPI
- aiogram
- OpenAI API
- SQLite
- python-dotenv

### 🚀 Як запустити

1. Клонуйте репозиторій:
    ```bash
    git clone https://github.com/NicTurtle/turbotabot.git
    cd turbotabot
    ```

2. Створіть віртуальне середовище та встановіть залежності:
    ```bash
    python -m venv venv
    source venv/bin/activate  # Windows: venv\Scripts\activate
    pip install -r requirements.txt
    ```

3. Створіть `.env` файл:
    ```
    TELEGRAM_TOKEN=токен_тг_бота
    OPENAI_API_KEY=ваш_openai_ключ
    ```

4. Запустіть локально:
    ```bash
    uvicorn main:app --reload
    ```

### 📌 Увага

TurbotaBot не є ліцензованим психологом. Це інструмент з GPT, призначений для моральної підтримки та емпатичного спілкування.

---

### ⚖️ Ліцензія та використання

Цей проєкт опубліковано **винятково з ознайомчою та навчальною метою**.  
Весь код, логіка та структура належать автору.

> ❗️Копіювання, відтворення або використання цього коду в комерційних цілях **заборонено**.

Якщо ви хочете використати частину проєкту — зверніться до автора за дозволом.
