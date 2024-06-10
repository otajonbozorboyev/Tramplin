from django.contrib import admin
from apps.main.models import Tag, StaticData, Statistic

admin.site.register(Tag)
admin.site.register(StaticData)
admin.site.register(Statistic)
