from django.db import models
from django.contrib.auth.models import User


TIME_PERIODS = (
    (1, '16:00-18:00'),
    (2, '18:00-20:00'),
    (3, '20:00-22:00'),
    (4, '22:00-00:00'),
    (5, '00:00-02:00'),
)


TABLES = (
    (1, '1'),
    (2, '2'),
    (3, '3'),
    (4, '4'),
    (5, '5'),
    (6, '6'),
)


class Booking(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    full_name = models.CharField(max_length=100)
    date = models.DateField()
    time = models.IntegerField(choices=TIME_PERIODS, default=0)
    table = models.IntegerField(choices=TABLES, default=0)
    phone_number = models.CharField(null=True, blank=True, max_length=15)
    questions = models.TextField(max_length=1000,null=True, blank=True)
    

    def __str__(self):
        return f'{self.user} {self.date}' 


class Review(models.Model):
    booking = models.ForeignKey(Booking, on_delete=models.CASCADE, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    review = models.TextField(max_length=1000)
