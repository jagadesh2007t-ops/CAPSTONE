Capstone ai iot sensors data analysis

 Data Cleaning and Preprocessing

**Objective:** To improve the quality and reliability of simulated IoT sensor data before AI-based analysis.

**Tools Used:** Python, Pandas, NumPy, Matplotlib and Google Colab.

**Methodology:** The dataset was examined for missing readings, duplicate records, invalid humidity values, negative light measurements and unusual temperature changes. Exact duplicate records were removed, while suitable missing and invalid readings were estimated using time-based interpolation. Suspicious temperature readings were flagged for further investigation rather than automatically deleted.

**Verification:** A before-and-after comparison was prepared to evaluate the effects of cleaning. All identified issues and corrective actions were documented in an error log.

**Limitations:** Interpolated values are estimates rather than actual sensor measurements. Temperature anomalies require additional evidence before being classified as sensor errors.

**Outcome:** The preprocessing workflow produces a cleaned dataset, error log, comparison summary and anomaly review file for subsequent AI analysis.

 AI-Based Sensor Data Analysis

**Objective:** To analyze temperature, humidity and light sensor readings using statistical techniques and artificial intelligence.

**Tools Used:** Python, Pandas, NumPy, Matplotlib, Seaborn and Scikit-learn.

**Methodology:** Descriptive statistics were calculated to examine the distribution of sensor measurements. Pearson correlation analysis was used to study linear relationships among temperature, humidity and light intensity. Time-series graphs were created to visualize changes throughout the monitoring period.

An Isolation Forest model was trained using standardized sensor measurements to identify unusual observations. The resulting predictions were compared with independent rule-based checks for temperature spikes and physically invalid measurements.

**Verification:** AI-flagged observations were compared with rule-based findings. Disagreements were recorded for further investigation rather than automatically classified as AI errors.

**Limitations:** Isolation Forest identifies statistical anomalies, which do not necessarily indicate faulty sensors. Its predictions depend on the training dataset, selected features and contamination parameter. Further verification is required to establish whether flagged readings represent genuine faults.

**Conclusion:** The analysis workflow provides a reproducible method for identifying unusual IoT sensor readings, visualizing environmental trends and evaluating the reliability of AI-generated findings.

Verification of AI Sensor Data Analysis

**Objective:** To independently verify AI-generated sensor analysis findings, investigate potential prediction errors, and document the reliability and limitations of the anomaly-detection system.

**Methodology:** Statistical calculations were independently recomputed using NumPy and compared with Pandas results. The original sensor dataset was inspected for deliberately introduced data-quality problems. Isolation Forest predictions were evaluated against a known injected temperature anomaly and compared with an independent rule-based detection method.

**Verification Approach:** Agreement between AI predictions and heuristic rules was measured, while disagreements were documented for further review. Rule-based findings were not treated as definitive ground truth.

**AI Error Evaluation:** The known injected temperature spike provided a controlled test case for identifying a confirmed detection or missed detection. Other AI-only and rule-only findings were classified as unresolved until supporting evidence could be obtained.

**Limitations:** The dataset is simulated, and verified anomaly labels are limited. A comprehensive evaluation of false-positive rates, recall and overall model accuracy would require additional independently labeled observations.

**Conclusion:** The verification workflow provides a transparent method for checking statistical calculations, assessing AI anomaly predictions, identifying potential errors, and documenting findings responsibly.

# CAPSTONE 14 — External Sensor Data Verification Report

## 1. Objective

To validate simulated IoT temperature, humidity and light sensor measurements against credible technical specifications and environmental guidance.

## 2. Dataset Description

The project uses a simulated dataset containing 150 original sensor readings collected at five-minute intervals. The data includes temperature, relative humidity, light intensity and timestamps. Several data-quality problems were intentionally introduced to evaluate preprocessing and anomaly-detection methods.

## 3. External References

**Temperature:** The DHT22/AM2302 temperature sensor supports measurements from −40°C to 80°C. Its typical specified accuracy is approximately ±0.5°C.

**Humidity:** The DHT22/AM2302 measures relative humidity from approximately 0% to 100%, with accuracy dependent on operating conditions.

**Light intensity:** The BH1750FVI is a digital ambient light sensor that measures illuminance in lux. Its measurement capabilities depend on the selected operating mode and configuration.

**Environmental conditions:** OSHA workstation guidance and ASHRAE thermal comfort information provide context for evaluating indoor temperature and humidity. Office lighting guidance provides comparative illuminance values.

## 4. Findings

The original simulated dataset contains an intentionally inserted temperature spike of 64.8°C, an invalid humidity value of 118%, and a negative illuminance value of −25 lux.

The humidity and illuminance values violate physical measurement constraints. The temperature spike remains within the DHT22 measurement range but is unusually high for the simulated indoor environment.

The cleaned dataset was compared with illustrative environmental reference ranges. The number of readings outside each reference band was calculated separately from sensor measurement-limit violations.

## 5. AI Verification

The external reference comparison was used to support interpretation of the Isolation Forest anomaly-detection results.

An AI-flagged reading was not automatically classified as a faulty measurement. Statistical anomalies, physical validity violations and environmental comfort deviations were evaluated separately.

## 6. Limitations

The dataset is simulated and was not collected using calibrated physical sensors. The DHT22 and BH1750FVI specifications are illustrative reference models.

Office environmental guidance is not a substitute for classroom-specific design requirements. Actual thermal comfort and lighting adequacy depend on occupancy, activity, ventilation, sensor placement and other environmental factors.

## 7. Conclusion

External verification improves the reliability of AI-assisted IoT sensor analysis by distinguishing invalid measurements from unusual but potentially valid environmental conditions.

The findings demonstrate the importance of combining AI anomaly detection, manufacturer specifications, independent calculations and contextual interpretation.

## 8. References

1. Aosong Electronics. *AM2302 Temperature and Humidity Sensor Datasheet.*
   https://www.makerguides.com/wp-content/uploads/2019/02/DHT22-AM2302-Datasheet.pdf

2. ROHM Semiconductor. *BH1750FVI Technical Note.*
   https://www.sunrom.com/download/725.pdf

3. Occupational Safety and Health Administration. *Computer Workstations — Workstation Environment.*
   https://www.osha.gov/etools/computer-workstations/workstation-environment

4. ASHRAE. *Standard 55 — Thermal Environmental Conditions for Human Occupancy.*
   https://www.ashrae.org/technical-resources/bookstore/standard-55-thermal-environmental-conditions-for-human-occupancy

5. U.S. Department of Energy, Better Buildings Solution Center. *Energy Best Management Practices: Lighting.*
   https://betterbuildingssolutioncenter.energy.gov/sites/default/files/tools/4519539_RTX%20Energy%20BMP%20Guidebook_Interactive_10-2022.pdf

## Executive Summary

The AI IoT Sensor Data Analyst project investigates the application of artificial intelligence to environmental sensor data analysis, anomaly detection and evidence-based reporting.

A simulated dataset containing 150 original observations of temperature, relative humidity and light intensity was prepared for analysis. Data preprocessing techniques were applied to address missing values, duplicate records and invalid measurements.

Statistical analysis and correlation analysis were performed using Python. An Isolation Forest machine-learning model was implemented to identify unusual combinations of sensor measurements.

The analysis included independent verification of statistical calculations, investigation of known injected anomalies and comparison of sensor readings with external technical references.

The project identified opportunities to improve data validation, sensor monitoring, anomaly investigation and reporting. It also demonstrated that AI-generated findings require verification before they can be used to support operational decisions.

Overall, the project illustrates how AI can improve the efficiency of IoT data analysis while emphasizing transparency, data quality and responsible interpretation.

## Step 8: Automated IoT Sensor Data Analysis and Weekly Reporting

**Objective:** To develop an automated Python workflow for analyzing IoT sensor data, detecting anomalies, generating visualizations and producing periodic reports.

**Tools Used:** Python, Pandas, NumPy, Scikit-learn, Matplotlib, Visual Studio Code and Windows Task Scheduler.

**Methodology:** A Python script was developed to load a cleaned sensor dataset, validate measurements, calculate descriptive statistics and identify anomalous observations using the Isolation Forest algorithm.

The script generates sensor trend visualizations, an anomaly-detection chart, CSV summaries and a structured Markdown report. Execution logs are maintained to support troubleshooting and reproducibility.

**Automation:** The reporting script can be scheduled to run weekly through Windows Task Scheduler. Updated sensor data must be supplied for each reporting period.

**Verification:** The automation is tested by executing the script and confirming that all expected outputs are generated. AI-flagged observations are treated as candidates for investigation rather than confirmed sensor faults.

**Limitations:** The current prototype operates on a simulated historical dataset. Continuous monitoring requires an updated data source. The model is retrained during each run, and additional labeled data would be needed to evaluate detection accuracy.

**Conclusion:** The automation workflow demonstrates how Python and machine learning can reduce repetitive analysis and reporting tasks while maintaining documented outputs for independent review.
