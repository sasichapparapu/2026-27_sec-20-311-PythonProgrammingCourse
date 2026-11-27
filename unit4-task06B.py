class InvalidSpeedError(Exception):
    """Raised when the vehicle speed is outside the allowed range."""


speed = float(input("Enter vehicle speed in km/h: "))

if not 0 <= speed <= 120:
    raise InvalidSpeedError("Speed must be between 0 and 120 km/h.")

print(f"Valid speed: {speed:g} km/h")