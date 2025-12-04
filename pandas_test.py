import pandas as pd

df = pd.read_csv("/Users/user/Documents/GitHub/wds25a/supermarket_sales.csv")

# Mittelwert aller numerischen Spalten
means = df.select_dtypes(include='number').mean()

# Anzahl Verkäufe pro Filiale (A, B, C)
sales_per_branch = df.groupby('Branch').size()

# Anzahl Verkäufe pro Geschlecht in jeder Filiale
sales_by_branch_gender = df.groupby(['Branch', 'Gender']).size().unstack(fill_value=0) #sieht besser aus

print(means)
print()
print(sales_per_branch)
print()
print(sales_by_branch_gender)


