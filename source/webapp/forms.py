from django import forms
from django.forms import widgets


class TaskForm(forms.Form):
    title = forms.CharField(max_length=50, required=True, label='Title')
    description = forms.CharField(max_length=200, required=False, label='Description',
                                  widget=widgets.Textarea(attrs={'cols': 40, 'rows': 3}))
    execution_date = forms.DateField(required=False, label='Execution date')
