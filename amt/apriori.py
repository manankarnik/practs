import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from mlxtend.preprocessing import TransactionEncoder
from mlxtend.frequent_patterns import association_rules, apriori

data = pd.read_csv("groceries.csv").drop(columns=["Item(s)"])

transactions = data.apply(lambda x: x.dropna().tolist(), axis=1).tolist()
print(transactions[:5])


te = TransactionEncoder()
te_arr = te.fit_transform(transactions)
df = pd.DataFrame(te_arr, columns=te.columns_)

frequent_itemsets = apriori(df, min_support=0.01, use_colnames=True)
print(frequent_itemsets)

plt.xticks(rotation="vertical")
sns.barplot(x="itemsets", hue="itemsets", legend=False, y="support", palette="mako", data=frequent_itemsets.nlargest(20, columns="support"))
plt.show()

rules = association_rules(frequent_itemsets, metric="lift", min_threshold=1)
rules_df = rules[["antecedents", "consequents", "support", "confidence", "lift", "zhangs_metric"]].copy()
rules_df["antecedents"] = rules_df["antecedents"].apply(lambda x: ", ".join(x))
rules_df["consequents"] = rules_df["consequents"].apply(lambda x: ", ".join(x))
rules_df = rules_df.sort_values(by="support", ascending=False)
rules_df.head()
