from django.db import models
from django.contrib.auth.models import User

class Team(models.Model):
    team_pk = models.AutoField(primary_key=True)
    team_name = models.CharField(max_length=20)
    team_member = models.ManyToManyField(User, related_name='team_user')

class SubmitResult(models.Model):
    submit_pk = models.AutoField(primary_key=True)
    submit_file = models.FileField(upload_to="submits/")
    submit_team_pk = models.ForeignKey(Team, on_delete=models.CASCADE, related_name="submit_team")
    submit_score = models.DecimalField(decimal_places=4, max_digits=6)
    submit_create = models.DateTimeField(auto_now_add=True)

class LeaderBoard(models.Model):
    leader_pk = models.AutoField(primary_key=True)
    leader_submit_pk = models.OneToOneField(SubmitResult, related_name='leader_submit', on_delete=models.CASCADE)