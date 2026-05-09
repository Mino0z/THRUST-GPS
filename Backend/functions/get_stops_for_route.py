import pandas as pd

def get_stops_for_route(data: dict, route_id: str):
    """
    Zwraca listę przystanków dla podanej trasy (route_id).
    """
    trips = data.get("trips")
    stop_times = data.get("stop_times")
    stops = data.get("stops")
    
    if trips is None or stop_times is None or stops is None:
        return pd.DataFrame()
        
    # Pobierz trip_id dla danej trasy
    route_trips = trips[trips["route_id"] == route_id]["trip_id"]
    
    # Pobierz stop_id dla tych przejazdów
    route_stops = stop_times[stop_times["trip_id"].isin(route_trips)]["stop_id"].unique()
    
    # Zwróć dane o przystankach
    return stops[stops["stop_id"].isin(route_stops)]

