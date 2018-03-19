import os

from django.core.exceptions import ValidationError
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.db.models.fields.related import ManyToManyField, OneToOneField
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.template.defaultfilters import slugify, default
from django.utils import timezone

import numpy as np


# default values
phone_len = 20
standard_char_len = 200
extended_char_len = 500
difficulty_validators = [MinValueValidator(0), MaxValueValidator(5)]

class AbstractUser(models.Model):
    username = models.CharField(max_length = 128, primary_key = True)
    fullname = models.CharField(max_length = standard_char_len) # name and surname
    email = models.EmailField(unique = True)
    phone_contact = models.CharField(max_length = phone_len, unique = True, blank = "True", null = True)

    #is_manager = models.BooleanField()

    def user_image_path(self, filename):
        return (os.path.join("user_profile_images", filename))

    profile_picture = models.ImageField(upload_to=user_image_path, blank="True")

    class Meta:
        abstract = True;

    def __str__(self):
        return self.fullname


class StandardUser(AbstractUser):
    pass

class ShelterManagerUser(AbstractUser):
    pass

class Shelter(models.Model):
    # relationships
    manager = OneToOneField(ShelterManagerUser)

    name = models.CharField(max_length = 128, primary_key = True) # name and surname
    bio = models.CharField(max_length = extended_char_len)
    webpage = models.URLField(blank = "True")
    phone_contact = models.CharField(max_length = phone_len, unique = True)
    availability_info = models.CharField(max_length = extended_char_len)
    location = models.CharField(max_length = standard_char_len)
    avg_difficulty_rating = models.IntegerField(default = 5, validators = difficulty_validators)

    slug = models.SlugField(unique = True)


    def shelter_image_path(self, filename):
        return (os.path.join("shelters_profile_images", filename))

    profile_picture = models.ImageField(upload_to=shelter_image_path, blank="True")



    def save(self, *args, **kwargs):
        """

        :rtype: object
        """
        self.slug = slugify(self.name)

        sum = 0
        count = 0

        shelter_dogs = Dog.objects.all().filter(dog_shelter = self)

        for dog in shelter_dogs:
            reviews = Review.objects.all().filter(reviewed_dog = dog)
            sum += np.sum([review.difficulty_rating for review in reviews])
            count += len(reviews)

        if (count):
            self.avg_difficulty_rating = int(sum/count)
        else:
            self.avg_difficulty_rating = 0

        super(Shelter, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Dog(models.Model):
    # relationships
    dog_shelter = models.ForeignKey(Shelter)

    # ID (or pk) is implicitly made by Django
    # id = models.AutoField(primary_key=True)

    name = models.CharField(max_length = standard_char_len)
    bio = models.CharField(max_length = extended_char_len)
    breed = models.CharField(max_length = standard_char_len)

    difficulty = models.IntegerField(default = 0, validators = difficulty_validators)

    size = models.CharField(max_length = 1, choices = (("S", "Small"),
                                       ("M", "Medium"),
                                       ("L", "Large")))
    gender = models.CharField(max_length = 1, choices = (("M", "Male"),
                                                         ("F", "Female")))

    is_puppy = models.BooleanField(default = "False")
    is_childfriendly = models.BooleanField(default = "False")

    slug = models.SlugField(unique = True)

    def dog_image_path(self, filename):
        return (os.path.join("dogs_profile_images", filename))

    profile_picture = models.ImageField(upload_to=dog_image_path, blank="True")


    def save(self, *args, **kwargs):

        """

        :rtype: object
        """
        reviews = Review.objects.all().filter(reviewed_dog = self)

        if reviews:
            avg_difficulty = 0

            for review in reviews:
                avg_difficulty += review.difficulty_rating

            avg_difficulty = avg_difficulty/len(reviews)
        else:
            avg_difficulty = 3;

        self.difficulty = avg_difficulty


       # if not(self.profile_picture):


        # if called upon object creation, save first, so pk is created and slug in not None
        if not(self.pk):
            super().save(*args, **kwargs)
        else:
            self.slug = slugify(self.name + "-" + str(self.pk))
            super(Dog,self).save(*args, **kwargs)


    def clean(self):

        same_name = Dog.objects.all().filter(name=self.name, dog_shelter = self.dog_shelter).count()

        if same_name > 1:
            raise ValidationError("Dog of this name is already in the shelter.")

    def __str__(self):
        return self.name

# Sets up slug upon creation. This workaround deserves cookies and praise.
@receiver(post_save, sender = Dog)
def update_slug(sender, instance, created, *args, **kwargs):
    if created:
        instance.slug = slugify(instance.name + "-" + str(instance.pk))
        instance.save()

class Request(models.Model):
    # relationships
    requesting_user = models.ForeignKey(StandardUser)
    request_manager = models.ForeignKey(ShelterManagerUser)
    requested_dog = models.ForeignKey(Dog)

    date = models.DateTimeField(default = timezone.now())
    status = models.CharField(max_length = 1, choices = (("A", "Accepted"),
                                                      ("D", "Denied"),
                                                      ("P", "Pending"),
                                                      ("C", "Completed"),
                                                      ("R", "Reviewed")))
    message = models.CharField(max_length = extended_char_len, blank = True)

    def __str__(self):
        dog_name = str(self.requested_dog)
        user_name = str(self.requesting_user)
        manger_name = str(self.request_manager)

        return (dog_name  + " - by " + user_name + " (" + self.date.strftime("%B %d, %Y") + ")")

    def save(self, *args, **kwargs):

        """

        :rtype: object
        """
        if (Review.objects.all().filter(request = self)) and not(self.status.__eq__("R")):
            self.status = "R"

        super(Request, self).save(*args, **kwargs)

    def clean(self):

        managed_shelter = Shelter.objects.all().filter(manager = self.request_manager)
        managed_dogs = Dog.objects.all().filter(dog_shelter = managed_shelter)

        if self.requested_dog not in managed_dogs:
            raise ValidationError("Dog does not belong to shelter managed by given shelter manager.")

class Review(models.Model):
    # relationships
    reviewing_user = models.ForeignKey(StandardUser)
    reviewed_dog = models.ForeignKey(Dog)
    request = models.OneToOneField(Request)


    difficulty_rating = models.IntegerField(default = 3, validators = difficulty_validators)
    comment = models.CharField(max_length = extended_char_len)
    date = models.DateTimeField()

    def save(self, *args, **kwargs):

        # update dog upon creating/changing review
        """

        :rtype: object
        """
        super(Review, self).save(*args, **kwargs)

        # change request to "Reviewed"
        self.request.status = "R"

        # self.reviewed_dog.
        self.reviewed_dog.save()
        self.reviewed_dog.dog_shelter.save()

    def clean(self):
        # User can only review dog if their request was completed
        # User can only make as many reviews as completed requests
        reviews_num = Review.objects.all().filter(reviewing_user = self.reviewing_user, reviewed_dog = self.reviewed_dog).count()
        requests = Request.objects.all().filter(requesting_user = self.reviewing_user,
                                                    requested_dog = self.reviewed_dog)
        complete_requests_num = requests.filter(status = "C").count()
        reviewed_requests_num = requests.filter(status = "R").count()

        # Request must be completed (adding review) or reviewed (editing review)
        if (self.request.status != "C") or (self.request.status != "R"):
            raise ValidationError("Cannot review dog which request has not been completed.")


    def __str__(self):
        dog_name = str(self.reviewed_dog)
        user_name = str(self.reviewing_user)

        return (dog_name  + " (" + self.date.strftime("%B %d, %Y") + ")")
