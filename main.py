import pandas as pd
import json
import logging
import os
from validator import DataValidator
from datetime import datetime
from notifier import send_telegram_alert

# Logging Setup 
os.makedirs("logs", exist_ok=True)

logging.basicConfig(
    filename="logs/monitor.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Loading  Dataset
df = pd.read_csv("data/negative_sales.csv")

#  Load Config
with open("config.json") as f:
    config = json.load(f)

#  Run Validator 
validator = DataValidator(df, config)

validator.validate_schema()
validator.check_missing()
validator.check_business_rules()
validator.check_drift()
validator.check_outliers()

status = validator.get_status()

print("Final Status:", status)
print("Errors:", validator.errors)
print("Warnings:", validator.warnings)

# Logging
if status == "ERROR":
    logging.error(f"Validation failed: {validator.errors}")
elif status == "WARNING":
    logging.warning(f"Validation warnings: {validator.warnings}")
else:
    logging.info("Validation passed with no issues.")

# Generating report
os.makedirs("reports", exist_ok=True)

timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
report_file = f"reports/report_{timestamp}.txt"

with open(report_file, "w") as f:
    f.write("DATA QUALITY REPORT\n")
   
    f.write(f"Status: {status}\n\n")

    if validator.errors:
        f.write("Errors:\n")
        for err in validator.errors:
            f.write(f" - {err}\n")

    if validator.warnings:
        f.write("\nWarnings:\n")
        for warn in validator.warnings:
            f.write(f" - {warn}\n")

print(f"Report saved to {report_file}")

if config["enable_telegram"] and status in ["ERROR", "WARNING"]:
    
    message = f" DATA QUALITY ALERT\n\nStatus: {status}\n\n"
    
    if validator.errors:
        message += "Errors:\n"
        for err in validator.errors:
            message += f"- {err}\n"

    if validator.warnings:
        message += "\nWarnings:\n"
        for warn in validator.warnings:
            message += f"- {warn}\n"

    send_telegram_alert(
        message,
        config["telegram_token"],
        config["telegram_chat_id"]
    )
