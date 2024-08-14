from django.contrib import admin

# Register your models here.


from hh.models import Resume, Vacancy, Profession

admin.site.register(Resume)
admin.site.register(Vacancy)
admin.site.register(Profession)

