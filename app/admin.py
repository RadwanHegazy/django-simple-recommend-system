from django.contrib import admin
from django.contrib.auth.models import Group
from .models import Video, Recommend_Video

admin.site.unregister(Group)
admin.site.register(Video)
admin.site.register(Recommend_Video)

