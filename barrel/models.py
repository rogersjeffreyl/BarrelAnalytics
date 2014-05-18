from django.db import models
from django.contrib.auth.models import User
from django import forms

class BUser(models.Model):
    buser_name = models.CharField(max_length=128, unique=True)

    def __unicode__(self):
        return self.buser_name

class Link(models.Model):
    buser = models.ForeignKey(BUser)
    url = models.URLField()
    title = models.TextField()

    def __unicode__(self):
        return self.url

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'password')

