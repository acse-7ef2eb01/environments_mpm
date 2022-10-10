from envtest import last_of_series
import pandas as pd

s = pd.Series([1, 3, 5, 6, 8])
print(last_of_series(s))