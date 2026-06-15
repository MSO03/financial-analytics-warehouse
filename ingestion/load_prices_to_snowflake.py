import os
import pandas as pd
import snowflake.connector
from dotenv import load_dotenv
from snowflake.connector.pandas_tools import write_pandas

from ingest_prices import fetch_data

load_dotenv()
 
def get_connection(): 
	return snowflake.connector.connect(
		account=os.getenv("SNOWFLAKE_ACCOUNT"),
		user=os.getenv("SNOWFLAKE_USER"),
		password=os.getenv("SNOWFLAKE_PASSWORD"),
		warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
		database=os.getenv("SNOWFLAKE_DATABASE"),
		schema=os.getenv("SNOWFLAKE_SCHEMA")
	)

def main():
	df = fetch_data ()

	df["TRADE_DATE"] = pd.to_datetime(df["TRADE_DATE"]).dt.date 

	conn = get_connection()
	success, chunks, rows, output = write_pandas(
		conn,
		df,
		table_name="PRICES",
		database="FINANCIAL_ANALYTICS",
		schema="RAW"
	)

	print(f"success = {success}, chunks={chunks}, rows={rows}, output={output}")
	print(chunks)
	print(rows)
	print(output)

	conn.close()

if __name__ == '__main__':
	main()
	
