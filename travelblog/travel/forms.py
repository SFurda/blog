from django import forms
from .models import Travel, Tag, Category, WellnessTags, Wellness, GearCategory, GearTags, Gear


class TravelForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Travel
        fields = ['title', 'description', 'youtube_url',
                  'image_url', 'category', 'tags']


class WellnessForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=WellnessTags.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Wellness
        fields = ['title', 'description', 'youtube_url',
                  'image_url', 'category', 'tags']


class GearForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=GearTags.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Gear
        fields = ['title', 'description', 'youtube_url',
                  'image_url_1', 'image_url_2', 'image_url_3', 'category', 'tags']
