from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Team(models.Model):
    team_pk = models.AutoField(primary_key=True)
    team_name = models.CharField(max_length=20)
    team_member = models.ManyToManyField(User, related_name='team_user')

class SubmitResult(models.Model):
    submit_pk = models.AutoField(primary_key=True)
    submit_file = models.FileField(upload_to="submits/")
    submit_name = models.CharField(max_length=256)
    submit_team_pk = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="submit_team")
    submit_user_pk = models.ForeignKey(User, on_delete=models.CASCADE, related_name="submit_user", null=True)
    submit_score = models.DecimalField(decimal_places=4, max_digits=6)
    submit_create = models.DateTimeField(auto_now_add=True)
    submit_leader = models.BooleanField(default=False)

class LeaderTime(models.Model):
    leader_pk = models.AutoField(primary_key=True)
    leader_team = models.OneToOneField(Team, related_name='leader_team', on_delete=models.CASCADE)
    leader_create = models.DateTimeField(auto_now=True)

class Explain(models.Model):
    explain_pk = models.AutoField(primary_key=True)
    explain_id = models.CharField(max_length=10)
    explain_text = models.TextField()

class Image(models.Model):
    image_pk = models.AutoField(primary_key=True)
    image_data = models.ImageField(upload_to='')
