from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os

# Importy naszych funkcji do obsługi GTFS
from functions.load_and_filter_data import load_and_filter_data
from functions.get_stops_for_route import get_stops_for_route
from functions.get_trip_schedule import get_trip_schedule
from functions.get_active_services import get_active_services
from functions.parse_realtime_data import parse_realtime_data

app = FastAPI(
    title="T:H:RUST GPS API",
    description="API do obsługi danych GTFS statycznych i czasu rzeczywistego (realtime). Automatycznie wygenerowana dokumentacja Swagger.",
    version="1.0.0",
    docs_url="/",
    redoc_url="/redoc"
)

# Konfiguracja CORS (pozwala na komunikację z frontendem np. w Vue/React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Ścieżki do plików
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATASET_DIR = os.path.join(BASE_DIR, "datasets")
REALTIME_FILE = os.path.join(DATASET_DIR, "realtime.pb")

# Globalny obiekt na dane statyczne, żeby wczytać je tylko raz
gtfs_data = {}

@app.on_event("startup")
def startup_event():
    """
    Wywoływane przy starcie serwera - ładuje (filtruje) wszystkie statyczne dane do pamięci RAM.
    """
    global gtfs_data
    print("Wczytywanie statycznych zbiorów danych GTFS...")
    gtfs_data = load_and_filter_data(DATASET_DIR)
    print("Zakończono wczytywanie danych GTFS!")

@app.get("/status")
def read_status():
    return {"status": "ok", "message": "API T:H:RUST GPS działa"}

@app.get("/routes")
def get_routes():
    """
    Zwraca wszystkie dostępne trasy.
    """
    if "routes" not in gtfs_data or gtfs_data["routes"].empty:
        return []
    return gtfs_data["routes"].fillna("").to_dict(orient="records")

@app.get("/route/{route_id}/stops")
def route_stops(route_id: str):
    """
    Zwraca wszystkie stop_id i współrzędne dla wybranej trasy (skrót).
    """
    stops_df = get_stops_for_route(gtfs_data, route_id)
    if stops_df.empty:
        raise HTTPException(status_code=404, detail="Brak przystanków dla tej trasy.")
    return stops_df.fillna("").to_dict(orient="records")

@app.get("/trip/{trip_id}/schedule")
def trip_schedule(trip_id: str):
    """
    Zwraca pełen rozkład dla konkretnego przejazdu.
    """
    schedule_df = get_trip_schedule(gtfs_data, trip_id)
    if schedule_df.empty:
        raise HTTPException(status_code=404, detail="Brak rozkładu dla tego trip_id.")
    return schedule_df.fillna("").to_dict(orient="records")

@app.get("/services/active")
def active_services(date: str, day: str):
    """
    Zwraca aktywne service_id na konkretny dzień.
    np. /services/active?date=20260509&day=saturday
    """
    services = get_active_services(gtfs_data, date, day)
    return {"active_services": services}

@app.get("/realtime")
def realtime_positions():
    """
    Parsuje na żywo (co każde zapytanie frontendu) plik .pb i zwraca pozycje GPS. 
    """
    rt_df = parse_realtime_data(REALTIME_FILE)
    if rt_df.empty:
        return []
    return rt_df.fillna("").to_dict(orient="records")
