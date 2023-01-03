from django.contrib import admin
from .models import Literarysource
from .models import Textesource
# Register your models here.
admin.site.register(Literarysource)
# Register your models here.
admin.site.register(Textesource)



admin.site.site_header = 'Literary Program'
