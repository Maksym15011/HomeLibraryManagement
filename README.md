# HomeLibraryManagement

## Dane logowania

**Login:** admin
**Hasło:** nieznam

---

## Opis projektu

HomeLibraryManagement to aplikacja webowa stworzona w Django, służąca do zarządzania domową biblioteką. Użytkownik może dodawać, edytować, usuwać oraz przeglądać książki i powiązane z nimi informacje.

Projekt został wykonany w ramach przedmiotu **Architektura Oprogramowania 1**.

---

## Wykorzystane technologie

- Python 3
- Django 6
- SQLite
- HTML + Jinja
- Tailwind CSS

---

## Funkcjonalności

- logowanie i wylogowanie użytkowników,
- dodawanie, edycja i usuwanie książek,
- przeglądanie szczegółów książek,
- oznaczanie książek jako przeczytane i ulubione,
- dodawanie notatek do książek,
- przeglądanie autorów, wydawnictw, serii, gatunków i tematów,
- wyszukiwanie książek po tytule,
- filtrowanie książek według autora i gatunku.

---

## Uruchomienie projektu

Instalacja zależności:

```bash
pip install -r requirements.txt
```

Migracje bazy danych:

```bash
python manage.py migrate
```

Uruchomienie serwera:

```bash
python manage.py runserver
```

Aplikacja będzie dostępna pod adresem:

```text
http://127.0.0.1:8000/
```

---

## Autor

Projekt wykonany w ramach przedmiotu **Architektura Oprogramowania 1**.
