def get_active_services(data: dict, date_str: str, day_of_week: str):
    """
    Sprawdza aktywne serwisy
    """
    calendar = data.get("calendar")
    calendar_dates = data.get("calendar_dates")
    
    active_services = set()
    
    if calendar is not None and not calendar.empty:
        date_int = int(date_str)
        valid_cal = calendar[
            (calendar["start_date"] <= date_int) & 
            (calendar["end_date"] >= date_int) & 
            (calendar[day_of_week] == 1)
        ]
        active_services.update(valid_cal["service_id"].tolist())
        
    if calendar_dates is not None and not calendar_dates.empty:
        date_int = int(date_str)
        added = calendar_dates[(calendar_dates["date"] == date_int) & (calendar_dates["exception_type"] == 1)]
        removed = calendar_dates[(calendar_dates["date"] == date_int) & (calendar_dates["exception_type"] == 2)]
        
        active_services.update(added["service_id"].tolist())
        active_services.difference_update(removed["service_id"].tolist())
        
    return list(active_services)
