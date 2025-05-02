from time import time
from datetime import datetime

timestamp = time()
print("Seconds since January 1, 1970: " + str(timestamp) + f" or {timestamp:.2e} in scientific notation")
print(datetime.now().strftime("%b %d %Y"))