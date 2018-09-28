from django import forms

class ProjectForm(forms.ModelForm):
    '''ElectroporationConditionsForm.  Used to size the text input boxes'''

    class Meta:
        widgets = { 'project_key': forms.TextInput(attrs={'size': 60}),
                    'project_name': forms.TextInput(attrs={'size': 60}),
                    }