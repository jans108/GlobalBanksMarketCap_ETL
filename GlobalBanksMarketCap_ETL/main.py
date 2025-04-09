import logger
import banks_project
import sqlite3

url = "https://en.wikipedia.org/wiki/List_of_largest_banks"
table_attrib = ["Name", "MC_USD_Billion"]
final_table_attrib = ["Name", "MC_USD_Billion", "MC_GDP_Billion", "MC_EUR_Billion", "MC_INR_Billion"]
csv_path = "GlobalBanksMarketCap_ETL/CSV_file/Largest_banks_data.csv"
exchange_csv_path = "GlobalBanksMarketCap_ETL/CSV_file/exchange_rate.csv"
db_name = "GlobalBanksMarketCap_ETL/Database/Banks.db"
table_name = "Largest_banks"

first_query = "SELECT * FROM Largest_banks"
second_query = "SELECT AVG(MC_GBP_Billion) FROM Largest_banks"
third_query = "SELECT Name FROM Largest_banks LIMIT 5"

logger.log_progress("Preliminaries complete. Initiating ETL process")

df = banks_project.extract(url, table_attrib)
logger.log_progress("Data extraction complete. Initiating Transformation process")

df = banks_project.transform(exchange_csv_path, df)
logger.log_progress("Data transformation complete. Initiating Loading process")

banks_project.load_to_csv(df, csv_path)
logger.log_progress("Data saved to CSV file")

with sqlite3.connect(db_name) as conn:
    banks_project.load_to_db(df, table_name, conn)
    banks_project.run_queries(first_query, conn)
    banks_project.run_queries(second_query, conn)
    banks_project.run_queries(third_query, conn) 

logger.log_progress("SQL Connection initiated")
logger.log_progress("Data loaded to Database as a table, Executing queries")
logger.log_progress("Process Complete")
logger.log_progress("Server Connection closed")
