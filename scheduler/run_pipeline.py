import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data, create_table
import time 
def run_pipeline():
    create_table()

    while True:
        print("Fetching crypto data...")

        raw_data = extract_data()
        if raw_data:
            transformed = transform_data(raw_data)
            load_data(transformed)
            print("Data stored successfully!")

        time.sleep(300)  # every 5 minutes

if __name__ == "__main__":
    run_pipeline()  