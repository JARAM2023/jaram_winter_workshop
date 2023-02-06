from django.contrib import admin
from .models import (
    Team,
    SubmitResult,
    LeaderBoard,
    Explain,
    Image
)

admin.site.register(Team)
admin.site.register(SubmitResult)
admin.site.register(LeaderBoard)
admin.site.register(Explain)
admin.site.register(Image)
