import pandas as pd
import sys

path = sys.argv[1]

#use pandas to specify column widths
col_specification = [(0,1), (2,10), (11,35)]
data = pd.read_fwf(path, colspecs=col_specification)