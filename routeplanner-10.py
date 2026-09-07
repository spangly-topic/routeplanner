# === Stage 10: Add case-insensitive search across the most useful fields ===
# Project: RoutePlanner
def search_stops(query, field=None):
    """Case-insensitive search across stop fields.
    
    Searches by default across all fields. Pass field='name' to search only by name.
    Returns list of matching Stop objects.
    """
    query_lower = query.lower().strip()
    if not query_lower:
        return list(stops)
    
    matches = []
    for stop in stops:
        if field == 'name':
            if query_lower in stop.name.lower():
                matches.append(stop)
        elif field == 'address':
            if query_lower in stop.address.lower():
                matches.append(stop)
        elif field == 'city':
            if query_lower in stop.city.lower():
                matches.append(stop)
        elif field == 'phone':
            if query_lower in stop.phone.lower():
                matches.append(stop)
        elif field == 'notes':
            if query_lower in stop.notes.lower():
                matches.append(stop)
        else:
            # Search all fields
            for attr_name in ['name', 'address', 'city', 'phone', 'notes']:
                if query_lower in getattr(stop, attr_name, '').lower():
                    matches.append(stop)
                    break
    
    return matches
