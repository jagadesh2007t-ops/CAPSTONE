# CAPSTONE 14 — Automated Sensor Report

Generated: 2026-10-24 14:46
Period: 2026-10-20 06:00:00 to 2026-10-20 18:25:00
Observed coverage: 12.4 hours
Valid readings: 149
AI-flagged readings: 8

## Statistical Summary

### Temperature
- Mean: 29.12
- Minimum: 25.60
- Maximum: 64.80
- Standard deviation: 3.26

### Humidity
- Mean: 71.30
- Minimum: 66.20
- Maximum: 78.90
- Standard deviation: 2.68

### Light
- Mean: 639.39
- Minimum: 161.00
- Maximum: 921.00
- Standard deviation: 212.86

## AI Findings

Isolation Forest flagged 8 observations for investigation.

AI flags are not confirmed sensor faults.

## Recommendations

- Review flagged timestamps and sensor logs.
- Check missing and invalid incoming readings.
- Verify suspected faults before corrective action.
- Collect independently labeled examples.

## Limitations

- Data may be simulated.
- Model is refitted for each reporting period.
- A short observation window is not a full week.
- Contamination is an assumed anomaly fraction.
