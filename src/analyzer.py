from src.phases import detect_flight_phase
from src import rules

def analyze_flight(df):
    results = []

    for _, row in df.iterrows():
        events = []

        phase = detect_flight_phase(row)

        if rules.excessive_bank(row):
            events.append("EXCESSIVE_BANK")

        if rules.excessive_pitch(row):
            events.append("EXCESSIVE_PITCH")

        if rules.rapid_descent(row):
            events.append("RAPID_DESCENT")

        if rules.engine_mismatch(row):
            events.append("ENGINE_MISMATCH")

        results.append({
            "Time": row["Time"],
            "Phase": phase,
            "Events": events
        })

    return results
