import string
import random
from django.utils.text import slugify
from django.db import models


# Create your models here.


def rand_slug():
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(6))


asd = {
    ('Yes', 'Yes'),
    ('NO', 'No'),
}


class IdType(models.Model):
    id_type = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(rand_slug() + "-" + self.id_type)
        super(IdType, self).save(*args, **kwargs)

    def __str__(self, *args, **kwargs):
        return self.id_type


class Education(models.Model):
    edu_level = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(rand_slug() + "-" + self.edu_level)
        super(Education, self).save(*args, **kwargs)

    def __str__(self):
        return self.edu_level


class Stage(models.Model):
    start_up_stage = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(rand_slug() + "-" + self.start_up_stage)
        super(Stage, self).save(*args, **kwargs)

    def __str__(self):
        return self.start_up_stage


class Applicant(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    email_address = models.EmailField(unique=True, max_length=254)
    region = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    level_of_education = models.ForeignKey(Education, on_delete=models.CASCADE)
    id_type = models.ForeignKey(IdType, on_delete=models.CASCADE)
    id_number = models.CharField(max_length=30, blank=True)
    are_you_employed = models.CharField(max_length=5, choices=asd, default='Yes')
    start_up_stages = models.ForeignKey(Stage, on_delete=models.CASCADE)
    start_up_name = models.CharField(max_length=100, blank=True)
    number_of_founders = models.IntegerField()
    about_the_owner = models.TextField()
    full_month_dedication = models.CharField(max_length=5, choices=asd, default='Yes')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.last_name + ' - ' + self.first_name

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(rand_slug() + "-" + self.last_name)
        super(Applicant, self).save(*args, **kwargs)
