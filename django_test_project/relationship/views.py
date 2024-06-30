from django.shortcuts import render

from django_test_project.relationship.models import Employee


# Create your views here.
def index(request):
    return render(request, "relationship/index.html")


def all_employees(request):
    employees = __fetch_employees()
    select_related_employees = __fetch_related_employees()

    # will be 7 sql queries
    for employee in employees:
        print(employee.city.name)

    # will be 1 sql query
    for employee in select_related_employees:
        print(employee.city.name)

    return render(
        request,
        "relationship/all_employees.html",
        {"employees": select_related_employees},
    )


def __fetch_employees():
    """
    Use separate queries to fetch related objects.

    SELECT
        "relationship_employee"."id",
        "relationship_employee"."first_name",
        "relationship_employee"."last_name",
        "relationship_employee"."department_id",
        "relationship_employee"."email",
        "relationship_employee"."city_id"
    FROM
        "relationship_employee"

    SELECT
        "relationship_city"."id",
        "relationship_city"."name",
        "relationship_city"."country_id"
    FROM
        "relationship_city"
    WHERE
        "relationship_city"."id" = 8

    SELECT
        "relationship_city"."id",
        "relationship_city"."name",
        "relationship_city"."country_id"
    FROM
        "relationship_city"
    WHERE
        "relationship_city"."id" = 1
    """

    return Employee.objects.all()


def __fetch_related_employees():
    """
    Use JOIN to fetch related objects in one query.

    SELECT
        "relationship_employee"."id",
        "relationship_employee"."first_name",
        "relationship_employee"."last_name",
        "relationship_employee"."department_id",
        "relationship_employee"."email",
        "relationship_employee"."city_id",
        "relationship_city"."id",
        "relationship_city"."name",
        "relationship_city"."country_id"
    FROM
        "relationship_employee"
        INNER JOIN "relationship_city" ON (
            "relationship_employee"."city_id" = "relationship_city"."id"
        )
    """

    return Employee.objects.select_related("city").all()
