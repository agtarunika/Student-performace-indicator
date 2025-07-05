import os
import logging
from datetime import datetime

# Step 1: Generate log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Step 2: Create logs directory (in current working directory)
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

# Step 3: Full path to log file
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Step 4: Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
