from django.db import models


class Department(models.Model):
    name = models.CharField(max_length=64)
    description = models.TextField()

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class City(models.Model):
    name = models.CharField(max_length=64)
    country = models.ForeignKey(
        Country, on_delete=models.CASCADE, related_name="cities"
    )

    def __str__(self):
        return self.name


class Employee(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="employees"
    )
    email = models.EmailField()
    city = models.ForeignKey(City, on_delete=models.CASCADE, related_name="employees")
    projects = models.ManyToManyField("Project", related_name="employees")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Project(models.Model):
    name = models.CharField(max_length=128)
    deadline = models.DateField()

    def __str__(self):
        return self.name


class Profile(models.Model):
    employee = models.OneToOneField(
        Employee, on_delete=models.CASCADE, related_name="profile"
    )
    bio = models.TextField()
    birth_date = models.DateField()

    def __str__(self):
        return f"profile {self.employee.first_name}"
