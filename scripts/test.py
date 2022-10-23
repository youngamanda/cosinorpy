from CosinorPy import file_parser, cosinor, cosinor1
import numpy as np
import pandas as pd
import os

df = file_parser.read_csv(os.path.join("data","test.csv"))
tests = df.test.unique()
cosinor.periodogram_df(df)