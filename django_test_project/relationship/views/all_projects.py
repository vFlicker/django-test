from django.shortcuts import render

from ..models import Project


def all_projects(request):
    # projects = __fetch_projects()
    projects = __fetch_prefetch_related_projects()

    return render(
        request,
        "relationship/all_projects.html",
        {"projects": projects},
    )


def __fetch_projects():
    """
        Use separate queries to fetch related objects.
        Will be 4 sql queries, 1 main and 3 for each project.

    SELECT
      "relationship_project"."id",
      "relationship_project"."name",
      "relationship_project"."deadline"
    FROM
      "relationship_project"

    SELECT
      "relationship_employee"."id",
      "relationship_employee"."first_name",
      "relationship_employee"."last_name",
      "relationship_employee"."department_id",
      "relationship_employee"."email",
      "relationship_employee"."city_id"
    FROM
      "relationship_employee"
      INNER JOIN "relationship_employee_projects" ON (
        "relationship_employee"."id" = "relationship_employee_projects"."employee_id"
      )
    WHERE
      "relationship_employee_projects"."project_id" = 1

    SELECT
      "relationship_employee"."id",
      "relationship_employee"."first_name",
      "relationship_employee"."last_name",
      "relationship_employee"."department_id",
      "relationship_employee"."email",
      "relationship_employee"."city_id"
    FROM
      "relationship_employee"
      INNER JOIN "relationship_employee_projects" ON (
        "relationship_employee"."id" = "relationship_employee_projects"."employee_id"
      )
    WHERE
      "relationship_employee_projects"."project_id" = 2

    SELECT
      "relationship_employee"."id",
      "relationship_employee"."first_name",
      "relationship_employee"."last_name",
      "relationship_employee"."department_id",
      "relationship_employee"."email",
      "relationship_employee"."city_id"
    FROM
      "relationship_employee"
      INNER JOIN "relationship_employee_projects" ON (
        "relationship_employee"."id" = "relationship_employee_projects"."employee_id"
      )
    WHERE
      "relationship_employee_projects"."project_id" = 3
    """

    return Project.objects.all()


def __fetch_prefetch_related_projects():
    """
    Use two queries to fetch related objects.
    Will be 2 sql queries.

    SELECT
      "relationship_project"."id",
      "relationship_project"."name",
      "relationship_project"."deadline"
    FROM
      "relationship_project"

    SELECT
      ("relationship_employee_projects"."project_id") AS "_prefetch_related_val_project_id",
      "relationship_employee"."id",
      "relationship_employee"."first_name",
      "relationship_employee"."last_name",
      "relationship_employee"."department_id",
      "relationship_employee"."email",
      "relationship_employee"."city_id"
    FROM
      "relationship_employee"
      INNER JOIN "relationship_employee_projects" ON (
        "relationship_employee"."id" = "relationship_employee_projects"."employee_id"
      )
    WHERE
      "relationship_employee_projects"."project_id" IN (1, 2, 3)
    """

    return Project.objects.prefetch_related("employees").all()
