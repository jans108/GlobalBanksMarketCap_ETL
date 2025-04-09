import os
from datetime import datetime

log_path = "GlobalBanksMarketCap_ETL/Log_file/code_log.txt"
datetime_pattern = "%Y-%m-%d %H:%M:%S"

def log_progress(message: str):
    try:
        now = datetime.now()
        formatted_time = now.strftime(datetime_pattern)
        with open(log_path, "a") as file:
            file.write(f"{formatted_time} - {message}{os.linesep}")
    except Exception as e:
        with open(log_path, "a") as file:
            error_time = datetime.now().strftime(datetime_pattern)
            file.write(f"ERROR: {error_time} - Logging Error : {e}{os.linesep}")