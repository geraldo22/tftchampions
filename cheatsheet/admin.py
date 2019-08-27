from django.contrib import admin

# Register your models here.
from .models import Champion
from .models import Origin
from .models import ChampionOrigin
from .models import Class
from .models import ChampionClass

admin.site.register(Champion)
admin.site.register(Origin)
admin.site.register(ChampionOrigin)
admin.site.register(Class)
admin.site.register(ChampionClass)

