import pandas as pd

def get_trip_schedule(data: dict, trip_id: str):
    """
    Zwraca rozkład jazdy (przystanki i czasy) dla konkretnego przejazdu.
    """
    stop_times = data.get("stop_times")
    stops = data.get("stops")
    
    if stop_times is None or stops is None:
        return pd.DataFrame()
        
    trip_st = stop_times[stop_times["trip_id"] == trip_id]
    schedule = pd.merge(trip_st, stops, on="stop_id")
    schedule = schedule.sort_values(by="stop_sequence")
    
    return schedule

