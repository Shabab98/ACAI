from django.db import models
from faker import Faker
import random

fake = Faker()

# Create your models here.
# myapp/models.py
from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    USER_ROLE_CHOICES = [
        ('admin', 'Admin'),
        ('user', 'User'),
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=10, choices=USER_ROLE_CHOICES)

class Library(models.Model):
    publisher = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    page_count = models.PositiveIntegerField()
    category = models.CharField(max_length=50)
    shelf_location = models.CharField(max_length=50)
    published_date = models.DateField()
    is_in_stock = models.BooleanField(default=True)
    date_checked_out = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title

    @classmethod
    def create_simulated_data(cls, num_entries=200):
        for _ in range(num_entries):
            Library.objects.create(
                publisher=fake.company(),
                author=fake.name(),
                title=fake.catch_phrase(),
                page_count=random.randint(50, 500),
                category=fake.word(),
                shelf_location=fake.random_element(elements=('A1', 'B2', 'C3')),
                published_date=fake.date_this_decade(),
                is_in_stock=fake.boolean(),
                date_checked_out=fake.date_this_decade() if fake.boolean(chance_of_getting_true=30) else None
            )