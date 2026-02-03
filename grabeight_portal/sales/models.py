from django.db import models

# Represents the POS "sales" table
# Used only for reading transaction totals and dates
class Sale(models.Model):
    id = models.IntegerField(primary_key=True) # Primary key from POS DB
    # Total amount of the sale
    total_amount = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    # ✅ REAL column name from MySQL
    sale_date = models.DateField()

    is_voided = models.BooleanField()

    class Meta:
        # 🔒 READ-ONLY
        managed = False

        # Exact POS table name
        db_table = 'sales'

# Represents the POS "sale_items" table
# Used for analytics like Top Selling Products
class SaleItem(models.Model):
    id = models.IntegerField(primary_key=True) # Primary key (if exists in POS DB)

     # Foreign key IDs (kept as IntegerField for safety)
    sale_id = models.IntegerField()
    product_name = models.CharField(max_length=255)
    quantity = models.IntegerField() # Quantity sold
    price = models.DecimalField(max_digits=10, decimal_places=2)

    created_at = models.DateTimeField()
    
    
    class Meta:
    # 🔒 READ-ONLY
        managed = False
        # Exact POS table name
        db_table = 'sale_items'
    
