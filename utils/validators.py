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


# Validation check function for min price and max price
def validate_price_filter(
    min_price,
    max_price,
):
    errors = []

    try:
        if min_price is not None:
            min_price = float(min_price)
    except ValueError:
        errors.append("minimum price must be a number")

    try:
        if max_price is not None:
            max_price = float(max_price)
    except ValueError:
        errors.append("maximum price must be a number")

    if errors:
        return errors

    if min_price is not None and min_price < 0:
        errors.append("minimum price cannot be negative")

    if min_price is not None and max_price is not None and max_price < min_price:
        errors.append("maximum price cannot be smaller than minimum price")

    return errors
