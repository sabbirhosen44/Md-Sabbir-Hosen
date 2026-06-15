TRAVEL_TYPES = ["Budget", "Luxury", "Adventure", "Family"]


# Validation function for data
def validate_travel_deal(data):
    errors = []

    required_fields = ["destination", "price", "platform", "rating", "travel_type"]

    for field in required_fields:
        if field not in data:
            errors.append(f"{field} is required.")

    if errors:
        return errors

    if not data["destination"].strip():
        errors.append("destination cannot be empty")

    if data["price"] <= 0:
        errors.append("price must be positive")

    if data["rating"] < 1 or data["rating"] > 5:
        errors.append("rating must be between 1 and 5")

    if data["travel_type"] not in TRAVEL_TYPES:
        errors.append(f"travel_type must be one of {TRAVEL_TYPES}")

    return errors
