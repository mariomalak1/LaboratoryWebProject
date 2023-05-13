from django import forms
from .models import Lab

class LabForm(forms.ModelForm):
    status = forms.ChoiceField(widget=forms.RadioSelect, choices=Lab.STATUS)
    class Meta:
        model = Lab
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name != "status":
                field.widget.attrs['class'] = 'inputsyle'
