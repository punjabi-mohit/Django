from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.db.models.signals import m2m_changed

# Create your models here.

class Notes(models.Model):
    label = models.CharField(max_length=200)
    body = models.TextField(max_length=20000)
    timestamp = models.DateTimeField(auto_now_add=True)
    # tags = models.ManyToManyField('Tag', related_name='notes', blank=True)
    owner = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    active=models.BooleanField(default=True)


    def __str__(self):
        return str(self.id)

# def m2m_changed_note_count(sender,instance,*args,**kwargs):
#     if instance.products.all.count==0:
#         return


class Tag(models.Model):
    label = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)