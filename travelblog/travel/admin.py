from django.contrib import admin
from .models import (
    UserProfile,
    Category,
    Tag,
    Travel,
    WellnessCategory,
    WellnessTags,
    Wellness,
    GearCategory,
    GearTags,
    Gear,
)


admin.site.register(Category),
admin.site.register(Tag),
admin.site.register(Travel),

admin.site.register(Wellness),
admin.site.register(WellnessTags),
admin.site.register(WellnessCategory),

admin.site.register(Gear),
admin.site.register(GearTags),
admin.site.register(GearCategory)