from django.db import models

# This model REPRESENTS the existing POS "products" table
# ❗ This does NOT create a table
# ❗ This does NOT modify a table
class Product(models.Model):
    id  = models.IntegerField(primary_key=True) # Primary key from POS DB
    name = models.CharField(max_length=255)  # Product name column
    price = models.DecimalField(max_digits=10,decimal_places=2)
    stock = models.IntegerField()
    cost = models.DecimalField(max_digits=10, decimal_places=2)
    profit_margin = models.DecimalField(max_digits=10, decimal_places=2)
    barcode = models.CharField(max_length=255)

    
    # 🔒 VERY IMPORTANT
        # Tells Django: "This table already exists. DO NOT manage it."
    class Meta:
        managed = False
        db_table = 'products'  # Exact table name from POS database

        