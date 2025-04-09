# 🏦 Largest Banks ETL Project

A Python project for extracting, transforming, and loading (ETL) data about the world's largest banks.

The data is scraped from Wikipedia, processed (including currency conversions), and then saved both as a CSV file and in a local SQLite database. The project also includes functions for running SQL queries and logging all operations.

## 📂 Project Structure

```
project_root/
│
├── main.py                   # Main entry point of the program
├── banks_project.py          # Core ETL functions (extract, transform, load)
├── logger.py                 # Logging configuration
│
├── CSV_file/                 # Folder for CSV files (input and output)
│   ├── exchange_rate.csv
│   └── largest_banks.csv
│
├── Database/                 # SQLite database
│   └── Banks.db
│
├── Log_file/                 # Execution logs
│   └── code_log.txt
│
└── README.md                 # Project documentation
```

## 🚀 How to Run the Project

1. **Clone the repository**

```bash
git clone https://github.com/jans108/largest-banks-etl.git](https://github.com/jans108/GlobalBanksMarketCap_ETL
cd GlobalBanksMarketCap_ETL
```


2. **Run the program**

```bash
python main.py
```

3. **Check the results in the following folders:**

- `CSV_file/largest_banks.csv` — processed CSV output
- `Database/Banks.db` — SQLite database
- `Log_file/code_log.txt` — log file containing execution details

## 🛠️ Requirements

- Python 3.8+
- Libraries:
  - pandas
  - numpy
  - requests
  - beautifulsoup4
  - sqlite3 (built into Python)


## 📊 Project Features

- ✅ Web scraping of the largest banks from Wikipedia
- ✅ Data transformation: adding currency conversions (GBP, EUR, INR)
- ✅ Exporting to CSV and SQLite database
- ✅ Running SQL queries on the stored database
- ✅ Logging all operations to `code_log.txt`

## 💡 Potential Improvements

- Add support for additional currencies
- Automatically fetch exchange rates from an API
- Add unit tests with pytest
- Automate execution with a scheduler (cron / task scheduler)
- Build a web interface (Flask / FastAPI)


## 📄 License

This project is licensed under the MIT License — you are free to use, copy, and modify it.

