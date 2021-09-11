from django.contrib import admin
from .models import internshala, iimjobs, talentrack, interesting_urls, non_interesting_urls

# Register your models here.
admin.site.register(internshala)
admin.site.register(iimjobs)
admin.site.register(talentrack)
admin.site.register(interesting_urls)
admin.site.register(non_interesting_urls)
