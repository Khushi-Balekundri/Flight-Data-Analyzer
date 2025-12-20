# Aircraft Flight Data Analysis Tool

This project analyzes recorded aircraft flight data to reconstruct flight phases
and detect safety-relevant events using rule-based logic.

## Features
- Flight phase detection
- Rule-based safety event detection
- Modular, simulator-agnostic design

## Assumptions
- Thresholds are indicative and non-certified
- Intended for post-flight analysis only

## Rule Examples
- Excessive bank angle (>30°)
- Excessive pitch attitude
- Rapid descent rate
- Engine parameter mismatch

Rules are evaluated per time-step and reported with timestamps
for further inspection.

## Usage
python main.py


