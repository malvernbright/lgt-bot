from django import forms
from .models import NewQuestions


class QuestionsForm(forms.ModelForm):
    class Meta:
        model = NewQuestions
        fields = ["title"]