
from pathlib import Path
from datetime import datetime, timedelta
import logging

import numpy as np
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest

# ---------- CONFIGURATION ----------

BASE = Path(__file__).resolve().parent
INPUT = BASE / "cleaned_sensor_data.csv"
OUTPUT = BASE / "reports"
OUTPUT.mkdir(exist_ok=True)

FEATURES = ["temperature", "humidity", "light"]

logging.basicConfig(
    filename=OUTPUT / "automation.log",
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    encoding="utf-8"
)

def main():
    logging.info("Automation started")

    # 1. LOAD DATA
    df = pd.read_csv(INPUT)
    df.columns = df.columns.str.strip().str.lower()

    required = ["timestamp"] + FEATURES
    missing_columns = [
        c for c in required if c not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing columns: {missing_columns}"
        )

    df["timestamp"] = pd.to_datetime(
        df["timestamp"], errors="coerce"
    )

    for col in FEATURES:
        df[col] = pd.to_numeric(
            df[col], errors="coerce"
        )

    # 2. VALIDATE INPUT
    invalid = (
        df["timestamp"].isna()
        | df[FEATURES].isna().any(axis=1)
        | ~df["humidity"].between(0, 100)
        | (df["light"] < 0)
    )

    if invalid.any():
        logging.warning(
            "%d invalid or incomplete rows excluded",
            int(invalid.sum())
        )

    df = df.loc[~invalid].copy()

    df = df.drop_duplicates(
        subset=required
    ).sort_values("timestamp")

    if len(df) < 20:
        raise ValueError(
            "At least 20 valid readings required"
        )

    # 3. SELECT THE LATEST AVAILABLE 7-DAY PERIOD
    end = df["timestamp"].max()
    start = end - timedelta(days=7)

    week = df[
        (df["timestamp"] > start)
        & (df["timestamp"] <= end)
    ].copy()

    logging.info(
        "Analysis period: %s to %s",
        start, end
    )

    # 4. STATISTICAL ANALYSIS
    stats = week[FEATURES].agg(
        ["count", "mean", "median", "min",
         "max", "std"]
    ).T

    stats.to_csv(
        OUTPUT / "weekly_statistics.csv"
    )

    # 5. ISOLATION FOREST
    scaler = StandardScaler()
    X = scaler.fit_transform(week[FEATURES])

    model = IsolationForest(
        n_estimators=200,
        contamination=0.05,
        random_state=42
    )

    week["ai_prediction"] = model.fit_predict(X)
    week["ai_anomaly"] = (
        week["ai_prediction"] == -1
    )
    week["anomaly_score"] = (
        model.decision_function(X)
    )

    anomalies = week[week["ai_anomaly"]]

    anomalies.to_csv(
        OUTPUT / "weekly_anomalies.csv",
        index=False
    )

    # 6. SENSOR TREND CHARTS
    fig, axes = plt.subplots(
        3, 1, figsize=(12, 9),
        sharex=True
    )

    units = ["°C", "%", "lux"]

    for ax, col, unit in zip(
        axes, FEATURES, units
    ):
        ax.plot(
            week["timestamp"],
            week[col]
        )
        ax.set_title(f"{col.title()} Trend")
        ax.set_ylabel(unit)
        ax.grid(alpha=0.3)

    axes[-1].set_xlabel("Time")
    fig.autofmt_xdate()
    fig.tight_layout()

    fig.savefig(
        OUTPUT / "sensor_trends.png",
        dpi=180
    )
    plt.close(fig)

    # 7. AI ANOMALY CHART
    fig, ax = plt.subplots(figsize=(12, 5))

    ax.plot(
        week["timestamp"],
        week["temperature"],
        label="Temperature"
    )

    ax.scatter(
        anomalies["timestamp"],
        anomalies["temperature"],
        marker="x",
        s=90,
        label="AI flagged"
    )

    ax.set_title("AI Anomaly Detection")
    ax.set_xlabel("Time")
    ax.set_ylabel("Temperature (°C)")
    ax.legend()
    ax.grid(alpha=0.3)

    fig.autofmt_xdate()
    fig.tight_layout()

    fig.savefig(
        OUTPUT / "anomaly_chart.png",
        dpi=180
    )
    plt.close(fig)

    # 8. GENERATE WEEKLY REPORT
    coverage_hours = (
        week["timestamp"].max()
        - week["timestamp"].min()
    ).total_seconds() / 3600

    lines = [
        "# CAPSTONE 14 — Automated Sensor Report",
        "",
        f"Generated: {datetime.now():%Y-%m-%d %H:%M}",
        f"Period: {week['timestamp'].min()} "
        f"to {week['timestamp'].max()}",
        f"Observed coverage: {coverage_hours:.1f} hours",
        f"Valid readings: {len(week)}",
        f"AI-flagged readings: {len(anomalies)}",
        "",
        "## Statistical Summary",
        ""
    ]

    for sensor in FEATURES:
        values = week[sensor]
        lines.extend([
            f"### {sensor.title()}",
            f"- Mean: {values.mean():.2f}",
            f"- Minimum: {values.min():.2f}",
            f"- Maximum: {values.max():.2f}",
            f"- Standard deviation: {values.std():.2f}",
            ""
        ])

    lines.extend([
        "## AI Findings",
        "",
        f"Isolation Forest flagged {len(anomalies)} "
        "observations for investigation.",
        "",
        "AI flags are not confirmed sensor faults.",
        "",
        "## Recommendations",
        "",
        "- Review flagged timestamps and sensor logs.",
        "- Check missing and invalid incoming readings.",
        "- Verify suspected faults before corrective action.",
        "- Collect independently labeled examples.",
        "",
        "## Limitations",
        "",
        "- Data may be simulated.",
        "- Model is refitted for each reporting period.",
        "- A short observation window is not a full week.",
        "- Contamination is an assumed anomaly fraction.",
        ""
    ])

    (OUTPUT / "weekly_report.md").write_text(
        "\n".join(lines),
        encoding="utf-8"
    )

    logging.info(
        "Automation completed: %d rows, %d AI flags",
        len(week), len(anomalies)
    )

    print("Automation completed successfully!")
    print("Valid readings:", len(week))
    print("AI anomalies:", len(anomalies))
    print("Reports saved in:", OUTPUT)

if __name__ == "__main__":
    try:
        main()
    except Exception:
        logging.exception("Automation failed")
        raise
