from django.contrib import admin
from blog.models import Post



class PostAdmin(admin.ModelAdmin):
	list_display = ("title", "pub_date",)
	ordering = ("-pub_date",) #TODO: order by display=False



admin.site.register(Post, PostAdmin)