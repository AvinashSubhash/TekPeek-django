from django.contrib import admin
from tekpeek.models import Data,News
admin.site.site_header = "TekPeek Admin Page"
admin.site.index_title = "TekPeek Admin"
admin.site.site_title = "Avinash"

# Register your models here.


@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    pass

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    pass