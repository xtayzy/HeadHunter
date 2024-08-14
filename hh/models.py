from django.contrib.auth.models import User
from django.db import models

# Create your models here.


class Profession(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Resume(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    vac_name = models.ForeignKey(Profession, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    otchestvo = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    email = models.EmailField()
    skills = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    education = models.CharField(max_length=100)

    def __str__(self):
        return self.vac_name.name


class Vacancy(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    profession = models.ForeignKey(Profession, on_delete=models.SET_NULL, null=True, blank=True)
    company = models.CharField(max_length=100)
    salary = models.IntegerField(default=0)
    skills = models.CharField(max_length=100)
    res = models.CharField(max_length=100)
    address = models.CharField(max_length=100)

    def __str__(self):
        return self.profession.name




