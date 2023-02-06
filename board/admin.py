from django.contrib import admin
from .models import (
    Team,
    SubmitResult,
    LeaderTime,
    Explain,
    Image
)

admin.site.register(Team)
admin.site.register(SubmitResult)
admin.site.register(LeaderTime)
admin.site.register(Explain)
admin.site.register(Image)
