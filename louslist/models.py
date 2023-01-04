import datetime

from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.contrib.auth.models import User
from django.db.models import Q



from django.contrib.postgres.fields import ArrayField

class ProfileManager(models.Manager):

    def get_all_profiles(self, me):
        profiles = Profile.objects.all().exclude(user=me)
        return profiles

    def get_all_profiles_to_invite(self, sender):
        profiles = Profile.objects.all().exclude(user = sender)
        profile = Profile.objects.get(user=sender)
        qs = Relationship.objects.filter(Q(sender = profile) | Q(receiver = profile))
        print(qs)
        print('############')


        accepted = set([])
        for rel in qs:
            if rel.status == 'accepted':
                accepted.add(rel.receiver)
                accepted.add(rel.sender)
        print(accepted)
        print('############')

        available = [profile for profile in profiles if profile not in accepted]
        print(available)
        print('############')
        return available





class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()
    #id_num = models.IntegerField()
    #image = models.ImageField
    #email = models.CharField(max_length=30)
    #first_name = models.CharField(max_length=20)
    friends = models.ManyToManyField(User, related_name='friends', blank=True)
    #last_name = models.CharField(max_length=20)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    objects = ProfileManager()

    def get_friends(self):
        return self.friends.all()

    def get_friends_no(self):
        return self.friends.all().count()

    

    def __str__(self):
        return str(self.user)

STATUS_CHOICES = (
    ('send', 'send'),
    ('accepted', 'accepted'),

)

class RelationshipManager(models.Manager):
    def invitations_received(self, receiver):
        qs = Relationship.objects.filter(receiver=receiver, status='send')
        return qs

class Relationship(models.Model):
    sender = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='receiver')
    status = models.CharField(max_length=8, choices=STATUS_CHOICES)
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    objects = RelationshipManager()

    def __str__(self):
        return f"{self.sender} - {self.receiver} - {self.status}"



class Schedule(models.Model):
    userID = models.CharField(max_length=200)
    courses = models.ManyToManyField('Course', blank=True)
    def __str__(self):
        return self.userID

class Course(models.Model):
    title = models.CharField(max_length=200)
    subject = models.CharField(max_length=200)
    course_id = models.CharField(max_length=200)
    number = models.IntegerField()
    section = models.IntegerField()
    credits = models.IntegerField()
    instructor = models.CharField(max_length=200)
    days = models.CharField(max_length=200)
    time = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    def __str__(self):
        return self.subject + " " + str(self.number) + "Section: " + str(self.section)

class Comment(models.Model):
    schedule = models.ForeignKey(Schedule,on_delete=models.CASCADE,related_name='comments')
    name = models.CharField(max_length=80)
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)


# class ClassModel(models.Model):
#     id = models.UUIDField(primary_key=True)
#     instructorName = models.CharField(max_length=100)
#     subject = models.CharField(max_length=8)
#     courseCode = models.IntegerField(max_length=5)
#     component = models.CharField(max_length=5)
#     waitList = models.IntegerField(max_length=3)
#     waitListCap = models.IntegerField(max_length=3)
#     classCap = models.IntegerField(max_length=3)
#     seatsOpen = models.IntegerField(max_length=3)


