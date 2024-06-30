from django.shortcuts import render

from ..models import Employee


def all_employees(request):
    employees = __fetch_employees()
    select_related_employees = __fetch_select_related_employees()
    prefetch_related_employees = __fetch_prefetch_related_employees()

    return render(
        request,
        "relationship/all_employees.html",
        {"employees": select_related_employees},
    )


def __fetch_employees():
    """
    Use separate queries to fetch related objects.
    Will be 7 sql queries.

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


def __fetch_select_related_employees():
    """
    Use JOIN to fetch related objects in one query.
    Will be 1 sql query.

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


def __fetch_prefetch_related_employees():
    """
    Use two queries to fetch related objects.
    Will be 2 sql queries.

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
        "relationship_city"."id" IN (8, 1)
    """

    return Employee.objects.prefetch_related("city").all()
