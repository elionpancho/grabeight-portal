from django.db.models import Sum
from django.utils.timezone import now
from .models import Sale
from .models import SaleItem
# -----------------------------
# DAILY SALES
# -----------------------------

def get_daily_sales(date=None):
    """
    Returns total sales for a specific day.
    READ-ONLY query to POS DB.
    """

    if date is None:
        date = now().date()

    return (
        Sale.objects.using('pos') # 🔒 use POS database
        .filter(sale_date=date, is_voided=False)
        .aggregate(total=Sum('total_amount'))
    )


# -----------------------------
# MONTHLY SALES
# -----------------------------

def get_montly_sales(year, month):
       
    """
    Returns total sales for a given month.
    """
    return (
            Sale.objects.using('pos')
            .filter(
                sale_date__year=year,
                sale_date__month=month,
                is_voided=False
            )
            .aggregate(total=Sum('total_amount'))
        )

# -----------------------------
# YEARLY SALES
# -----------------------------

def get_yearly_sales(year):
    """
    Returns total sales for a given year.
    """

    return (
            Sale.objects.using('pos')
            .filter(
                sale_date__year=year,
                is_voided=False
            )
            .aggregate(total=Sum('total_amount'))
        )

# -----------------------------
# TOP SELLING PRODUCTS 
# -----------------------------

def get_top_selling_products(limit=10):
    """
    Returns top selling products by quantity.
    READ-ONLY aggregation.
    """
    return (
        SaleItem.objects.using('pos')
        .using('pos')
        .values('product_name')
        .annotate(total_qty=Sum('quantity'))
        .order_by('-total_qty')[limit]
    )