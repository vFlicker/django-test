import time

from django.db import connection
from django.shortcuts import render

from .models import Product


def index(request):
    products = Product.get_first_five()
    all_products = Product.objects.all()

    print(all_products.query)

    print("__________________________________________")

    list(all_products)
    for query in connection.queries:
        print(query["sql"])

    return render(request, "product/index.html", {"products": products})


def create_product(request):
    timestamp = time.time()

    Product.objects.create(
        name=f"Product {timestamp}",
        category="Category 1",
        price=100.00,
    )

    return render(request, "product/create.html")
