from django.contrib import admin
from .models import Profile, Image, Like,Follows,Comment

# Register your models here.
admin.site.register(Profile)
admin.site.register(Like)
admin.site.register(Follows)
admin.site.register(Comment)
admin.site.register(Image)


