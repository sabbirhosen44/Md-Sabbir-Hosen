# Standardizes the API response envelope.
def api_response(success, message, data=None, status=200):
    return {"success": success, "message": message, "data": data}, status


# Formats a list of items into a standard collection object.
def serialize_collection(items):
    return {"count": len(items), "travel_deals": [item.to_dict() for item in items]}
