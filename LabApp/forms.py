from django import forms
from .models import Lab, Report, Pc

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


class ReportForm(forms.ModelForm):
    problemType = forms.ChoiceField(widget=forms.RadioSelect, choices=Report.PROBLEM_TYPE)
    date = forms.DateField(label='Select a Date')
    pcNumber = forms.ModelChoiceField(queryset=Pc.objects.none())

    class Meta:
        model = Report
        exclude = ["reportId"]

    def __init__(self, lab = None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'inputsyle'
        if lab:
            self.fields["lab"].initial = lab
            self.fields["pcNumber"].queryset = Pc.objects.filter(lab = lab)
