from django.urls import path

from .views import create_product, index

app_name = "products"

urlpatterns = [
    path("", index, name="index"),
    path("create/", create_product, name="create"),
]
