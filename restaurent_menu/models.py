from django.contrib.auth.models import User
from django.db import models

MEAL_TYPE = (
    ("starters", "Starters"),
    ("salads", "Salads"),
    ("main_dishes", "Main dishes"),
    ("desserts", "Desserts")
)
STATUS = (
    (0, "Unavailable"),
    (1, "Available")
)

class Items(models.Model):
    meal = models.CharField(max_length=1000, unique=True)  # unique since each meal is unique
    description = models.CharField(max_length=2000)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    meal_type = models.CharField(max_length=200, choices=MEAL_TYPE)
    author = models.ForeignKey(User, on_delete=models.PROTECT)
    # (models.CASCADE : delets everything with the user, models.SET_NULL: just delets the user not items)
    status = models.IntegerField(choices=STATUS, default=1)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.meal
