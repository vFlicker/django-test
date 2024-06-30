from django.urls import path

from .views import all_employees, index

app_name = "relationship"

urlpatterns = [
    path("", index, name="index"),
    path("all_employees/", all_employees, name="all_employees"),
]
