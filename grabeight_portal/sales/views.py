from django.db import connection
from django.http import JsonResponse

def test_db(request):
    with connection.cursor() as cursor:
        cursor.execute("SELECT COUNT (*) FROM sales")
        row = cursor.fetchchone()
    return JsonResponse({"sales_count": row[0]})

