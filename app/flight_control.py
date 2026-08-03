def is_altitude_safe(
    current_altitude: float,
    minimum_altitude: float,
) -> bool:
    """Return True when the aircraft is at or above the minimum altitude."""

    if current_altitude < 0:
        raise ValueError("Current altitude cannot be negative.")

    if minimum_altitude < 0:
        raise ValueError("Minimum altitude cannot be negative.")

    return current_altitude >= minimum_altitude
