from django.db import models
import re, time

# Create your models here.
class UserManager(models.Manager):
    def user_validator(self, post_data):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')
        if len(post_data['fname']) < 2:
            errors['fname_error'] = "First name has to be at least 2 characters!"
        if len(post_data['lname']) < 2:
            errors['lname_error'] = "Last name has to be at least 2 characters!"
        if  post_data['lname'] == " ":
            errors['lname_error_2'] ="Last name has to be more than just a space!"
        if not EMAIL_REGEX.match(post_data['email']):
            errors['email_error'] = "Email is invalid"
        return errors 

class User(models.Model):
    fname = models.CharField(max_length=656)
    lname = models.CharField(max_length=656)
    email = models.CharField(max_length=656)
    password = models.CharField(max_length=656)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class CourseManager(models.Manager):
    def course_validator(self, post_data):
        errors = {}
        if len(post_data['name']) < 2:
            errors['name_error'] = 'Course name has to be more than two characters!'
        if len(post_data['city']) < 1:
            errors['city_error'] = 'City name has to be more than one character!'
        if len(post_data['state']) < 1:
            errors['state_error'] = 'State name has to be more than one character!'
        if int(post_data['number_of_holes']) < 0:
            errors['number_of_holes_error'] = 'Your hole numbers cant be negative! And must be more than 0!'
        if int(post_data['par']) < 0:
            errors['par_error'] = 'par cant be negative or one!'
        return errors
        

class Course(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    number_of_holes = models.IntegerField()
    par = models.IntegerField()
    liked_by = models.ManyToManyField(User, related_name="liked_courses")
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = CourseManager()


# class Game(models.Model):
#     course = models.ForeignKey(Course, related_name="course_name", on_delete=models.CASCADE )
#     date_time = models.DateTimeField()
#     hole = models.ForeignKey(Course, related_name="hole_number", on_delete=models.CASCADE )
#     par = models.ForeignKey(Course, related_name="par_number", on_delete=models.CASCADE )
#     creator = models.ForeignKey(User, on_delete=models.CASCADE)
#     create_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


class Review(models.Model):
    content = models.CharField(max_length=255)
    rating = models.IntegerField()
    author = models.ForeignKey(User, related_name="reviews_left", on_delete=models.CASCADE)
    course_for = models.ForeignKey(Course, related_name="reviews", on_delete=models.CASCADE)
    create_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
