from django import forms

from hh.models import Resume, Vacancy


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ('name', 'surname', 'otchestvo', 'vac_name', 'date_of_birth', 'email', 'skills', 'experience',
                  'education')
        widgets = {
            'date_of_birth': forms.DateInput(attrs={
                'placeholder': 'дд.мм.гггг',
                'type': 'date'
            }),
        }


class VacancyForm(forms.ModelForm):
    class Meta:
        model = Vacancy
        fields = 'profession', 'company', 'salary', 'skills', 'res', 'address'
