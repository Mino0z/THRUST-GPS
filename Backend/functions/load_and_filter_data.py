import pandas as pd
import os

def load_and_filter_data(dataset_dir: str):
    """
    Wczytuje zbiory danych GTFS i odfiltrowuje zbędne kolumny.
    Zwraca słownik z oczyszczonymi danymi (DataFrames).
    """
    data = {}
    
    # routes.txt
    routes_path = os.path.join(dataset_dir, "routes.txt")
    if os.path.exists(routes_path):
        routes = pd.read_csv(routes_path)
        cols_to_keep = ["route_id", "route_short_name", "route_long_name"]
        data["routes"] = routes[[c for c in cols_to_keep if c in routes.columns]]
        
    # stops.txt
    stops_path = os.path.join(dataset_dir, "stops.txt")
    if os.path.exists(stops_path):
        stops = pd.read_csv(stops_path)
        cols_to_keep = ["stop_id", "stop_name", "stop_lat", "stop_lon"]
        data["stops"] = stops[[c for c in cols_to_keep if c in stops.columns]]
        
    # trips.txt
    trips_path = os.path.join(dataset_dir, "trips.txt")
    if os.path.exists(trips_path):
        trips = pd.read_csv(trips_path)
        cols_to_keep = ["route_id", "service_id", "trip_id", "trip_headsign"]
        data["trips"] = trips[[c for c in cols_to_keep if c in trips.columns]]
        
    # stop_times.txt
    stop_times_path = os.path.join(dataset_dir, "stop_times.txt")
    if os.path.exists(stop_times_path):
        stop_times = pd.read_csv(stop_times_path)
        cols_to_keep = ["trip_id", "arrival_time", "departure_time", "stop_id", "stop_sequence"]
        data["stop_times"] = stop_times[[c for c in cols_to_keep if c in stop_times.columns]]

    # calendar.txt
    calendar_path = os.path.join(dataset_dir, "calendar.txt")
    if os.path.exists(calendar_path):
        calendar = pd.read_csv(calendar_path)
        cols_to_keep = ["service_id", "monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday", "start_date", "end_date"]
        data["calendar"] = calendar[[c for c in cols_to_keep if c in calendar.columns]]

    # calendar_dates.txt
    calendar_dates_path = os.path.join(dataset_dir, "calendar_dates.txt")
    if os.path.exists(calendar_dates_path):
        calendar_dates = pd.read_csv(calendar_dates_path)
        cols_to_keep = ["service_id", "date", "exception_type"]
        data["calendar_dates"] = calendar_dates[[c for c in cols_to_keep if c in calendar_dates.columns]]

    return data

