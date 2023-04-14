from django.contrib import admin
from .models import Category, Tag, Travel, Wellness, WellnessCategory, WellnessTags

admin.site.register(Category),
admin.site.register(Tag),
admin.site.register(Travel),

admin.site.register(Wellness),
admin.site.register(WellnessTags),
admin.site.register(WellnessCategory)