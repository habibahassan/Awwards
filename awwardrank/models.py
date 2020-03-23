from django.db import models
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.


class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    description = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.description

class Projects(models.Model):
    project_name = models.CharField(max_length=50, blank=True)
    project_photo = models.ImageField(upload_to='projectpics/')
    description = models.TextField(max_length=600, blank=True)
    github_repo = models.CharField(max_length=200, blank=True)
    url = models.CharField(max_length=50, blank=True)
    owner = models.ForeignKey(User, null=True, on_delete=models.CASCADE)

    def average_design(self):
        design_ratings = list(map(lambda x: x.design_rating, self.reviews.all()))
        return np.mean(design_ratings)

    def average_usability(self):
        usability_ratings = list(map(lambda x: x.usability_rating, self.reviews.all()))
        return np.mean(usability_ratings)

    def average_content(self):
        content_ratings = list(map(lambda x: x.content_rating, self.reviews.all()))
        return np.mean(content_ratings)

    @classmethod
    def search_project(cls,name):
        project = Project.objects.filter(title__icontains = name)
        return project


    def save_project(self):
       """
       This is the function that we will use to save the instance of this class
       """
       self.save()

    def delete_project(self):
       """
       This is the function that we will use to delete the instance of this class
       """
       self.delete()

    def __str__(self):
       return self.title



class Comments(models.Model):
    text = models.CharField(max_length = 100, blank = True)
    projects = models.ForeignKey(Projects, related_name = "comments",on_delete=models.CASCADE)
    author = models.ForeignKey(User, related_name = "author",on_delete=models.CASCADE)
    created_date = models.DateTimeField(auto_now_add = True,null = True)


    def save_comment(self):
       """
       This is the function that we will use to save the instance of this class
       """
       self.save()

    def delete_comment(self):
        Comments.objects.get(id = self.id).delete()

    @classmethod
    def get_comments_by_projects(cls, id):
        comments = Comments.objects.filter(project__pk = id)
        return comments

    def __str__(self):
        return self.text

class Review(models.Model):
    RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),

    )
    projects = models.ForeignKey(Projects, null=True, blank=True, on_delete=models.CASCADE, related_name="reviews")
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE, related_name='reviews')
    comment = models.TextField()
    design_rating = models.IntegerField(choices=RATING_CHOICES, default=0)
    usability_rating = models.IntegerField(choices=RATING_CHOICES, default=0)
    content_rating = models.IntegerField(choices=RATING_CHOICES, default=0)
    created_date = models.DateTimeField(auto_now_add = True,null = True)

    def save_review(self):
        self.save()

    def delete_comment(self):
        Review.objects.get(id = self.id).delete()

    @classmethod
    def get_comment(cls, id):
        comments = Review.objects.filter(project__pk =id)
        return comments

    def delete_review(self):
        self.delete()

    def __str__(self):
        return self.comment

class Profile(models.Model):
    profile_photo = models.ImageField(upload_to='profpics/')
    bio = models.TextField(blank=True)
    user_id = models.OneToOneField(User, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.bio

    def save_user(self):
        self.save()

    @receiver(post_save, sender=User)
    def create_user_profile(sender, instance, created, **kwargs):
        if created:
            Profile.objects.create(user_id=instance)

    @receiver(post_save, sender=User)
    def save_profile(sender, instance, **kwargs):
        instance.profile.save()