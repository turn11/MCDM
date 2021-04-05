### Import libraries
import pandas as pd

#----------------------------------------------------------------------------------#

### Import data set with the following columns:
# Propierties
# Units
# Max or Min Criteria
# Next columns are for each material with its properties values

df = pd.read_excel("Materiales.xlsx", engine = "openpyxl")
