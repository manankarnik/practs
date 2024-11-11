from pyfpgrowth import find_frequent_patterns, generate_association_rules
import pandas as pd

data = pd.read_csv("groceries.csv").drop(columns="Item(s)").apply(lambda x: x.dropna().tolist(), axis=1).to_list()
print(data)

fp = find_frequent_patterns(data[:5000], 10)
print(fp)
rules = generate_association_rules(fp, 0.9)
print(rules)
