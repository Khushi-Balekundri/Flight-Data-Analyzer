def detect_flight_phase(row):
    alt = row["Altitude"]
    vs = row["VerticalSpeed"]

    if alt < 50:
        return "GROUND"
    elif vs > 500:
        return "CLIMB"
    elif vs < -500 and alt < 3000:
        return "APPROACH"
    elif vs < -500:
        return "DESCENT"
    elif abs(vs) < 300:
        return "CRUISE"
    else:
        return "UNKNOWN"
