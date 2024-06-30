from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=90)
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=17, decimal_places=2)

    @staticmethod
    def get_first_five():
        query = "SELECT * FROM product_product LIMIT 5"
        all_products = Product.objects.all()
        print(all_products.query)
        return Product.objects.raw(query)


class Order(models.Model):
    number = models.CharField(unique=True, max_length=30)
    created = models.DateTimeField()
    operator_id = models.IntegerField()
    customer_id = models.IntegerField()


class OrderItem(models.Model):
    quantity = models.DecimalField(max_digits=19, decimal_places=3)
    price = models.DecimalField(max_digits=17, decimal_places=2)
    discount = models.DecimalField(
        max_digits=17, decimal_places=2, blank=True, null=True
    )

    order = models.ForeignKey(Order, related_name="items", on_delete=models.CASCADE)
    product = models.ForeignKey(
        Product, related_name="orders", on_delete=models.CASCADE
    )
