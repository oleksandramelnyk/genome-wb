#!/usr/bin/env python
# coding: utf-8

import numpy as np
import pandas as pd

df_wolbachia = pd.read_csv("phenot_patric_scholz_last.csv", sep=";")

pd.set_option("display.max_rows", 10)
df_wolbachia

rslt_df = df_wolbachia.loc[df_wolbachia['Host.Name'] == "Fruit fly, Drosophila melanogaster"]
pd.set_option("display.max_rows", 7)
rslt_df



