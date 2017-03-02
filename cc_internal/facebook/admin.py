from django.contrib import admin

# Register your models here.

from .models import Issue
from .models import Subissue
from .models import FB_Post, Geography

admin.site.register(Issue)
admin.site.register(Subissue)
admin.site.register(Geography)
admin.site.register(FB_Post)