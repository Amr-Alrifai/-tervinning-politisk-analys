
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Läs in data från CSV
df = pd.read_csv("recycling_parties.csv")

# Visualisera återvinning per stadsdel och dominerande parti
plt.figure(figsize=(10, 6))
sns.barplot(x="Stadsdel", y="Återvinning_kg_per_person", hue="Dominerande_parti", data=df)
plt.title("Återvinning per stadsdel och politisk dominans")
plt.ylabel("Återvinning (kg per person)")
plt.xlabel("Stadsdel")
plt.xticks(rotation=45)
plt.legend(title="Dominerande parti")
plt.tight_layout()
plt.savefig("figures/återvinning_visualisering.png")
plt.show()

# Visa genomsnittlig återvinning per parti
print("\nGenomsnittlig återvinning per parti:")
print(df.groupby("Dominerande_parti")["Återvinning_kg_per_person"].mean().sort_values(ascending=False))
