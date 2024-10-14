import pandas as pd
import matplotlib.pyplot as plt

# Charger le fichier CSV
data = pd.read_csv('C:/Users/DeLL/Documents/ProductVendorr.csv', sep=';')

# Analyse des données par fournisseur
supplier_stats = data.groupby('VendorID').agg(
    orders_count=('Product_ID', 'count'),
    total_quantity=('Quantity', 'sum'),
    total_price=('Price', 'sum')
).reset_index()

# Ajouter une colonne pour le chiffre d'affaires total (revenu)
supplier_stats['total_revenue'] = data.groupby('VendorID').apply(lambda x: (x['Price'] * x['Quantity']).sum()).values

# Visualisation 1 : Nombre de fois qu'un fournisseur a fourni un produit
plt.figure(figsize=(10,6))
plt.bar(supplier_stats['VendorID'], supplier_stats['orders_count'], color='skyblue')
plt.xlabel('Vendor ID')
plt.ylabel('Number of Orders')
plt.title('Number of Orders by Supplier')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Visualisation 2 : Quantité totale commandée par fournisseur
plt.figure(figsize=(10,6))
plt.bar(supplier_stats['VendorID'], supplier_stats['total_quantity'], color='lightgreen')
plt.xlabel('Vendor ID')
plt.ylabel('Total Quantity Ordered')
plt.title('Total Quantity Ordered by Supplier')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Visualisation 3 : Prix total par fournisseur
plt.figure(figsize=(10,6))
plt.bar(supplier_stats['VendorID'], supplier_stats['total_price'], color='salmon')
plt.xlabel('Vendor ID')
plt.ylabel('Total Price')
plt.title('Total Price by Supplier')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Visualisation 4 : Chiffre d'affaires par fournisseur
plt.figure(figsize=(10,6))
plt.bar(supplier_stats['VendorID'], supplier_stats['total_revenue'], color='gold')
plt.xlabel('Vendor ID')
plt.ylabel('Total Revenue')
plt.title('Total Revenue by Supplier')
plt.xticks(rotation=90)
plt.tight_layout()
plt.show()

# Fournisseur le plus utilisé
most_used_supplier = supplier_stats.loc[supplier_stats['orders_count'].idxmax()]
print("Fournisseur le plus utilisé :")
print(most_used_supplier)
