from django.db import models

class User(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    full_name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email_address = models.EmailField()
    avatar_url = models.CharField(max_length=255)
    description = models.TextField()
    date_of_birth = models.DateField()
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    occupation = models.CharField(max_length=255)
    experience = models.IntegerField()
    postal_code = models.CharField(max_length=10)

    def __str__(self):
        return self.full_name



class ResidentialAddress(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='residential_addresses')
    address_name = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    zip_code = models.CharField(max_length=10)

    def __str__(self):
        return self.address_name




    


