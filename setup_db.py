import sys
import os
import logging

# Set up basic configuration for logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Ensure the current working directory is the project root and add StayFit to the path
project_path = os.path.join(os.path.dirname(__file__), 'StayFit')
sys.path.insert(0, project_path)
logging.info(f"Added {project_path} to sys.path.")

try:
    from models import create_tables

    if __name__ == '__main__':
        logging.info("Starting to create tables...")
        create_tables()
        logging.info("Database tables created successfully.")
except Exception as e:
    logging.error("Failed to create tables due to an error: %s", e)
    sys.exit(1)  # Exit script with an error status
