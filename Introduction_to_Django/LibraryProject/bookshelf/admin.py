from django.contrib import admin
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "publication_year")
admin.site.register(Book, BookAdmin)
