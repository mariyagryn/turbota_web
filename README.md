# Turbota+

**Turbota+** — веб-платформа для інтернату з інтелектуальними порушеннями, яка поєднує:

* освітні ресурси (PDF-матеріали),
* розвивальні міні-ігри,
* інформаційну підтримку для батьків,
* організацію розкладу занять,
* можливість волонтерської допомоги.

  Розроблено в межах практики дослідницької ІПЗ-2 НаУКМА 2025.

---

## Тестові користувачі

**Вчитель:**
- Логін: `teacher_user`
- Email: `teacher@mail.com`
- Пароль: `Test12345`

**Батько:**
- Логін: `parent_user`
- Email: `parent@mail.com`
- Пароль: `Test12345`

**Адміністратор (superuser):**
- Логін: `admin_user`
- Email: `admin@mail.com`
- Пароль: `Test12345`

---

## Швидкий старт (Docker)

**Передумови:**

1. Встановлений Git.
1. Встановлений Docker Desktop (Windows/macOS) або Docker Engine (Linux).

### Кроки

1. **Клонуйте репозиторій (запускайте команду з місця, куди хочете клонувати)**

   ```
   git clone https://github.com/mariyagryn/turbota_web.git
   ```

2. **Перейдіть до директорії проєкту**

   ```
   cd turbota_web
   ```
   
3. **Скопіюйте приклад файлу `.env.example` у `.env`**

   ```
   cp .env.example .env
   ```

   У файлі `.env` за потреби можна відредагувати значення (SECRET_KEY, DEBUG, ALLOWED_HOSTS).

4. **Побудуйте й запустіть Docker-контейнери**

   ```
   docker-compose up --build
   ```

   Перший раз збірка образу може зайняти 1–2 хвилини.
5. **Застосуйте міграції бази даних**

   ```
   docker-compose exec web python manage.py migrate
   ```
6. **Імпортуйте початкові дані**

   ```
   docker-compose exec web python manage.py loaddata initial_groups initial_users initial_news initial_needs
   ```
   

7. **Відкрийте у браузері:**

   ```
   http://localhost:8000/
   ```

   Ви побачите головну сторінку додатку.

---

## Швидкий старт без Docker (через venv)

### Передумови
- Встановлений Python 3.10+ (рекомендовано 3.11 або новіше)
- pip (зазвичай йде разом із Python)
- git (для клонування репозиторію)

### Покрокова інструкція

1. **Клонувати репозиторій:**
   ```
   git clone https://github.com/mariyagryn/turbota_web.git
   cd turbota_web
   ```

2. **Створити та активувати віртуальне середовище:**
   - Windows:
     ```
     python -m venv .venv
     .venv\Scripts\activate
     ```
   - Linux/macOS:
     ```
     python3 -m venv .venv
     source .venv/bin/activate
     ```

3. **Встановити залежності:**
   ```
   pip install -r requirements.txt
   ```

4. **Скопіювати .env.example у .env:**
   ```
   cp .env.example .env
   ```
   (або вручну створити .env на основі .env.example)

5. **Застосувати міграції:**
   ```
   python manage.py migrate
   ```

6. **Імпортувати початкові дані:**
   ```
   python manage.py loaddata initial_groups initial_users initial_news initial_needs
   ```

7. **Запустити сервер розробки:**
   ```
   python manage.py runserver
   ```

8. **Відкрити у браузері:**
   ```
   http://localhost:8000/
   ```

---
