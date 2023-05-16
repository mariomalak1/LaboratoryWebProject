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
    date = forms.DateField(label='Select Date Of Problem', widget=forms.DateInput(attrs={'type': 'date'}))
    lab_disapled = forms.CharField(required=False, max_length=150, min_length=1, widget=forms.TextInput(attrs={'disabled': True}))

    class Meta:
        model = Report
        exclude = ["reportId", "lab"]

    def __init__(self, *args, **kwargs):
        # get lab from the form dict
        lab = kwargs.pop('lab', None)

        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'inputsyle'

        if lab:
            self.fields["lab_disapled"].initial = lab
            self.fields["pcNumber"].queryset = Pc.objects.filter(lab = lab)

    def save(self, commit=True, lab = None):
        if lab:
            self.instance.lab = lab
        super(ReportForm, self).save()

class AddPC_Form(forms.ModelForm):
    status = forms.ChoiceField(widget= forms.RadioSelect, choices=Pc.STATUS)
    class Meta:
        model = Pc
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'inputsyle'
        self.fields['status'].widget.attrs['class'] = 'no-label'
