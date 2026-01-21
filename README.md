# Sasha API

API zrobione w FastAPI.

## Co robi aplikacja?

Po uruchomieniu API i wejściu na stronę główną (`/`) aplikacja zwraca:
{"message": "Sasha API is running!"}
http://localhost:8000

## Jak uruchomić lokalnie?

1. Otwórz repozytorium:
   https://github.com/ssasshahrybovska/dsw48739.git

2.Wejdź do folderu projektu:

cd dsw48739

3. Uruchom Docker Compose:

docker-compose up --build

4. Otwórz w przeglądarce:

http://localhost:8000

## Jak uruchomić testy lokalnie?

W terminalu, w katalogu projektu:

pytest

## Co jest w repozytorium?

- `app/main.py` – kod API
- `Dockerfile` – obraz Docker (multi-stage build)
- `docker-compose.yml` – uruchomienie aplikacji przez Docker Compose
- `.github/workflows/ci.yml` – pipeline CI na GitHub Actions
- `requirements.txt` – biblioteki potrzebne do uruchomienia
- `tests/test_basic.py` – testy

## CI (GitHub Actions)

W repozytorium jest pipeline, który uruchamia:

- `flake8` (sprawdza formatowanie kodu)
- `pytest` (uruchamia testy)

Jeśli wszystko przejdzie, pipeline będzie zielony.

