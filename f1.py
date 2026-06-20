import pandas as pd
provider=pd.read_csv("providers.csv")
print(provider)
receivers=pd.read_csv("receivers.csv")
print(receivers)
claims=pd.read_csv("claims.csv")
print(claims)
food=pd.read_csv("food_list.csv")
print(food)
# 1. Provider Types Distribution
import matplotlib.pyplot as plt
provider['Type'].value_counts().plot(kind='bar')
plt.title("Provider by Type")
plt.show()
# 2. Count receiver types
receivers['Type'].value_counts().plot(kind='bar')
plt.title("Receivers by Type")
plt.show()

# 3. Provider type counts (ordered)
provider['Type'].value_counts().sort_index().plot(kind='bar')
plt.title("Provider Types (Alphabetical)")
plt.show()

# 4. Providers in Saraland
saraland_provider = provider[provider['City'] == "Saraland"]
print(saraland_provider)

# 5. Claims per receiver (JOIN equivalent)
claims_per_receiver = claims.groupby('Receiver_ID')['Claim_ID'].count()
claims_per_receiver.plot(kind='bar')
plt.title("Claims per Receiver")
plt.show()

# 6. Food counts by location
food.groupby('Location')['Food_Name'].count().sort_values(ascending=False).plot(kind='bar')
plt.title("Food Count by Location")
plt.show()

# 7. Total quantity of food
print("Total Quantity:", food['Quantity'].sum())

# 8. Food types distribution
food['Food_Type'].value_counts().plot(kind='pie', autopct='%1.1f%%')
plt.title("Food Types Distribution")
plt.show()

# 9. Claims per food item (JOIN equivalent)
claims_food = pd.merge(claims, food, on="Food_ID")
claims_food.groupby('Food_Name')['Claim_ID'].count().sort_values(ascending=False).plot(kind='bar')
plt.title("Claims per Food Item")
plt.show()

# 10. Successful claims per provider (JOIN equivalent)
claims_provider = pd.merge(claims, food, on="Food_ID")
claims_provider = pd.merge(claims_provider, provider, on="Provider_ID")
claims_provider.groupby('Name')['Claim_ID'].count().sort_values(ascending=False).plot(kind='bar')
plt.title("Successful Claims per Provider")
plt.show()

# 11. Average Claim_ID by Status
claims.groupby('Status')['Claim_ID'].mean().plot(kind='bar')
plt.title("Average Claim ID by Status")
plt.show()

# 12. Meal types claimed
food['Meal_Type'].value_counts().plot(kind='bar')
plt.title("Meal Types Claimed")
plt.show()

# 13. Quantity donated per provider (JOIN equivalent)
provider_food = pd.merge(food, provider, on="Provider_ID")
provider_food.groupby('Name')['Quantity'].sum().sort_values(ascending=False).plot(kind='bar')
plt.title("Total Quantity Donated per Provider")
plt.show()

# 14. Average food quantity claimed per receiver (JOIN equivalent)
claims_food_receiver = pd.merge(claims, food, on="Food_ID")
claims_food_receiver = pd.merge(claims_food_receiver, receivers, on="Receiver_ID")
claims_food_receiver.groupby('Name')['Quantity'].mean().sort_values(ascending=False).plot(kind='bar')
plt.title("Average Food Quantity Claimed per Receiver")
plt.show()
