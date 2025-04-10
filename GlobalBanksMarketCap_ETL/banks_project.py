"""ETL process for bank market cap."""

import csv

import numpy as np
import pandas as pd
import requests
from bs4 import BeautifulSoup


def extract(url, data_attributes):
    data_list = []
    scraping = requests.get(url, timeout=5).text
    parse = BeautifulSoup(scraping, "html.parser")
    tables = parse.find_all("tbody")
    rows = tables[2].find_all("tr")
    for row in rows:
        col = row.find_all("td")
        if len(col) != 0:
            if col[0].find("a") and col[2].text.strip():
                columns_map = {"Name": 0, "MC_USD_Billion": 2}
                data_dict = {
                    key: col[index].get_text(strip=True)
                    for key, index in columns_map.items()
                }
                data_list.append(data_dict)
    df = pd.DataFrame(data_list, columns=data_attributes)
    return df


def transform(csv_file, df: pd.DataFrame):
    exchange_rate = {}
    with open(csv_file, "r", encoding="utf-8") as file:
        reader = csv.reader(file)
        # Skipping header in csv_file
        next(reader)
        for row in reader:
            if row:
                exchange_rate[row[0]] = float(row[1])
    # Checking if all currencies exist in dictionary
    for currency in ["GBP", "EUR", "INR"]:
        if currency not in exchange_rate:
            raise ValueError(f"Missing exchange rate for {currency}")

    # Converting values from string to numeric in dataframe
    df["MC_USD_Billion"] = pd.to_numeric(df["MC_USD_Billion"], errors="coerce")

    # Creating columns with converted values by currency
    df["MC_GBP_Billion"] = np.round(df["MC_USD_Billion"] * exchange_rate["GBP"], 2)
    df["MC_EUR_Billion"] = np.round(df["MC_USD_Billion"] * exchange_rate["EUR"], 2)
    df["MC_INR_Billion"] = np.round(df["MC_USD_Billion"] * exchange_rate["INR"], 2)
    return df


def load_to_csv(df: pd.DataFrame, csv_file):
    df.to_csv(csv_file, index=False)


def load_to_db(df: pd.DataFrame, table_name, connection):
    df.to_sql(table_name, connection, if_exists="replace", index=False)


def run_queries(query, connection):
    try:
        query_result = pd.read_sql(query, connection)
        print(query)
        print(f"\n{query_result.to_string(index=True)}")
        print(50 * "=")
    except Exception as e:
        print(f"Error while running query: {e}")
