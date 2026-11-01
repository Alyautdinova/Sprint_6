# Sprint_6 — Автотесты для сервиса «Яндекс.Самокат»

Проект содержит UI-автотесты для учебного сервиса [Яндекс.Самокат](https://qa-scooter.praktikum-services.ru/), написанные на Python + Selenium + Pytest с отчётами Allure.

## Что проверяется

### 1. Раздел FAQ на главной странице
- Параметризованный тест: для каждого вопроса проверяется, что при клике открывается **правильный ответ**.

### 2. Заказ самоката (позитивный сценарий)
- **Две точки входа**: кнопка «Заказать» в хедере и в футере.
- **Два набора тестовых данных** (параметризация).
- Шаги:
  1. Нажать «Заказать».
  2. Заполнить форму заказа (имя, фамилия, адрес, метро, телефон, дата, срок аренды, цвет, комментарий).
  3. Проверить появление попапа «Заказ оформлен».

### 3. Логотипы на странице заказа
- Клик по логотипу **Самоката** → возврат на главную страницу в той же вкладке.
- Клик по логотипу **Яндекса** → открытие главной страницы **Яндекса** в новой вкладке (через редирект).

## Стек

- Python 3.11+
- Selenium 4
- Pytest
- Allure-pytest
- Firefox

## Структура проекта

Sprint_6/
├── data/                  # тестовые данные и URL
│   ├── data_test.py       # наборы данных (FAQ, заказы)
│   └── urls.py            # адреса страниц
├── locators/              # селекторы элементов
│   ├── header_locators.py
│   ├── home_locators.py
│   ├── order_locators.py
│   └── modal_locators.py
├── pages/                 # Page Object Model
│   ├── base_page.py       # обёртки над Selenium
│   ├── header_page.py     # хедер: логотипы, верхняя кнопка «Заказать»
│   ├── home_page.py       # главная: FAQ, нижняя кнопка «Заказать»
│   ├── order_page.py      # форма заказа
│   └── modal_page.py      # модалка «Заказ оформлен»
├── tests/                 # тесты
│   ├── tests_faq.py
│   └── tests_order.py
├── conftest.py            # фикстуры (driver)
├── requirements.txt
└── README.md

## Установка и запуск

### 1. Клонировать репозиторий

```bash
git clone <URL>
cd Sprint_6
```

### 2. Создать и активировать виртуальное окружение

```bash
python -m venv .venv
source .venv/bin/activate     # macOS / Linux
.venv\Scripts\activate        # Windows
```

### 3. Установить зависимости

```bash
pip3 install -r requirements.txt
```

### 4. Установить браузер и драйвер

- **Firefox** + [Geckodriver](https://github.com/mozilla/geckodriver/releases)

### 5. Запустить тесты

```bash
# все тесты
pytest tests

# конкретный файл
pytest tests/tests_order.py

# конкретный тест
pytest "tests/tests_order.py::TestOrder::test_order[order_data0]"

## Генерация Allure-отчёта

```bash
# 1. Запустить тесты с сохранением результатов
pytest tests --alluredir=allure_results --clean-alluredir

# 2. Сгенерировать HTML-отчёт
allure generate allure_results -o allure_report --clean

# 3. Открыть отчёт
allure open allure_report

# или посмотреть на лету без сохранения
allure serve allure_results
```
