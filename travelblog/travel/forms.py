from django import forms
from .models import Travel, Tag, Category, WellnessTags, Wellness

class TravelForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    class Meta:
        model = Travel
        fields = ['title', 'description', 'youtube_url', 'image_url', 'category', 'tags']

class WellnessForm(forms.ModelForm):
     tags = forms.ModelMultipleChoiceField(
        queryset=WellnessTags.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
     
     class Meta:
        model = Wellness
        fields = ['title', 'description', 'youtube_url', 'image_url', 'category', 'tags']