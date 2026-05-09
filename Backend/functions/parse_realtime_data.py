import os
import pandas as pd
from google.transit import gtfs_realtime_pb2

def parse_realtime_data(pb_filepath: str):
    """
    Wczytuje i parsuje plik Protocol Buffers (realtime.pb) z danymi GTFS-Realtime.
    Wydobywa informacje o aktualnych pozycjach pojazdów i zwraca je w czytelnym formacie (DataFrame).
    """
    if not os.path.exists(pb_filepath):
        return pd.DataFrame()

    feed = gtfs_realtime_pb2.FeedMessage()
    with open(pb_filepath, 'rb') as f:
        feed.ParseFromString(f.read())

    vehicles = []
    for entity in feed.entity:
        if entity.HasField('vehicle'):
            vehicle = entity.vehicle
            vehicles.append({
                'trip_id': vehicle.trip.trip_id if vehicle.HasField('trip') else None,
                'route_id': vehicle.trip.route_id if vehicle.HasField('trip') else None,
                'vehicle_id': vehicle.vehicle.id if vehicle.HasField('vehicle') else None,
                'latitude': vehicle.position.latitude if vehicle.HasField('position') else None,
                'longitude': vehicle.position.longitude if vehicle.HasField('position') else None,
                'current_stop_sequence': vehicle.current_stop_sequence if vehicle.HasField('current_stop_sequence') else None,
                'stop_id': vehicle.stop_id if vehicle.HasField('stop_id') else None,
                'timestamp': vehicle.timestamp if vehicle.HasField('timestamp') else None,
            })
            
    return pd.DataFrame(vehicles)

