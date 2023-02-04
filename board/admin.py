from django.contrib import admin
from .models import (
    Team,
    SubmitResult,
    LeaderBoard
)

admin.site.register(Team)
admin.site.register(SubmitResult)
admin.site.register(LeaderBoard)
