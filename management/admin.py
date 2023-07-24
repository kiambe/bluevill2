from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Project)
admin.site.register(Report)
admin.site.register(Client)
admin.site.register(Personell)
admin.site.register(Management)
admin.site.register(ProjectDocument)