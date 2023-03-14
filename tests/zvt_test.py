import os

os.environ["TESTING_ZVT"] = "1"
from zvt.api import *


df = get_kdata(entity_id='stock_sz_000338', provider='joinquant')
print(df.tail())
