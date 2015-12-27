from django.contrib import admin

# Register your models here.
from .models import Post
from .executivemodels import Executive
from .mmodels import Messages

admin.site.register(Post)
admin.site.register(Executive)
admin.site.register(Messages)
