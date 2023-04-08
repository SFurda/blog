from django import forms
from .models import Travel

class TravelForm(forms.ModelForm):
    class Meta:
        model = Travel
        fields = ['title', 'description', 'youtube_url', 'image_url', 'category', 'tags']