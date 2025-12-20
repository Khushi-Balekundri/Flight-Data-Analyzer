from src.loader import load_flight_data
from src.analyzer import analyze_flight

df = load_flight_data("data/sample_flight.csv")
results = analyze_flight(df)

for r in results:
    if r["Events"]:
        print(f'Time {r["Time"]}: {r["Phase"]} → {r["Events"]}')
