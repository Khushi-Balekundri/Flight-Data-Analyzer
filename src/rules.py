def excessive_bank(row):
    return abs(row["Roll"]) > 30

def excessive_pitch(row):
    return row["Pitch"] > 25 or row["Pitch"] < -15

def rapid_descent(row):
    return row["VerticalSpeed"] < -3000

def engine_mismatch(row):
    return abs(row["Engine1"] - row["Engine2"]) > 15
