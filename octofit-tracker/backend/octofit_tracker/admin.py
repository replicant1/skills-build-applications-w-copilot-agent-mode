from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, Team, Workout, Activity, Leaderboard

admin.site.register(User, UserAdmin)
admin.site.register(Team)
admin.site.register(Workout)
admin.site.register(Activity)
admin.site.register(Leaderboard)
