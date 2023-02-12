from django.contrib import admin
from .models import (
    Team,
    SubmitResult,
    LeaderTime,
    Explain,
    Image,
    Config
)

class TeamAdmin(admin.ModelAdmin):
    search_fields = ['team_name']
    list_display = ['team_name']

class SubmitResultAdmin(admin.ModelAdmin):
    search_fields = ['submit_team_pk__submit_team__team_name']
    list_display = ['submit_team_pk', 'submit_score', 'submit_create', 'submit_leader']

class ConfigAdmin(admin.ModelAdmin):
    search_fields = ['config_name']
    list_display = ['config_pk', 'config_name', 'config_value']

admin.site.register(Team, TeamAdmin)
admin.site.register(SubmitResult, SubmitResultAdmin)
admin.site.register(LeaderTime)
admin.site.register(Explain)
admin.site.register(Image)
admin.site.register(Config, ConfigAdmin)
