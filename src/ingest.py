import pandas as pd
import logging

def load_data(filepath):
    try:
        if filepath.endswith(".csv"):
            data = pd.read_csv(filepath)

        elif filepath.endswith(".json"):
            data = pd.read_json(filepath)

        else:
            raise ValueError("Unsupported file format")

        logging.info(f"Loaded {len(data)} records")
        return data

    except Exception as error:
        logging.error(f"Data loading failed: {error}")
        raise
