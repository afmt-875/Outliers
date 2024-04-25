import pandas as pd
import numpy as np

df['total_sat'].fillna(df['importe'] + df['iva'], inplace=True)