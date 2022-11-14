from django import forms

from .models import Task, Tag


class DateTimeInput(forms.DateTimeInput):
    input_type = "datetime-local"


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False,
    )
    deadline = forms.DateTimeField(widget=DateTimeInput)

    class Meta:
        model = Task
        fields = "__all__"
