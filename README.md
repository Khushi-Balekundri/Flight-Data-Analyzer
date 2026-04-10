# Flight Data Analyzer (Telemetry Analysis & System Health Monitoring)

A rule-based telemetry analysis system for classifying system states and detecting anomalies from time-series flight data.

Designed to emulate post-mission analysis workflows, enabling system health assessment, validation of expected behavior, and structured detection of safety-relevant events.

## Why this project matters
* Demonstrates how telemetry data can be used to infer system state and behavior
* Enables detection of anomalies and deviations from expected operating conditions
* Reflects concepts used in mission operations, system monitoring, and diagnostics

## Features
- Flight phase detection using altitude and vertical speed
- Rule-based anomaly detection using deterministic logic
- Time-step evaluation with timestamped event reporting
- Modular rule structure for extending system checks
- Designed for explainability, traceability, and debugging

## Rule Examples   
- Excessive bank angle (>30°)
- Excessive pitch attitude
- Rapid descent rate
- Engine parameter mismatch

Rules are evaluated at each time step, with detected events logged alongside timestamps for traceability and analysis.

## Assumptions
- Thresholds are indicative and non-certified
- Input data is pre-cleaned and time-ordered
- Intended for post-flight analysis (not real-time control systems)

## Limitations
- Rule-based detection may generate false positives near phase transitions
- Does not account for temporal smoothing or hysteresis effects
- Limited to predefined rules; does not adapt dynamically to new patterns
- Simplified phase classification based on a small set of parameters

## Future Improvements
- Introduce state-aware or multi-step phase detection
- Add smoothing to reduce noise-induced false positives
- Expand rule coverage for additional system parameters
- Support real-time streaming telemetry input

## License
MIT License

## Usage
python main.py  


