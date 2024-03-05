import logging
from datetime import datetime

dt=datetime.now()
def custom_log():
    logging.basicConfig(handlers=[logging.FileHandler(filename=fr'.\Logs\test_{dt.strftime("%d%b%Y_%H%M%S")}.txt', mode='w'),
                              logging.StreamHandler()
                              ],
                        level=logging.INFO,
                        format='%(asctime)s %(levelname)s %(message)s',
                        force=True)
    return logging