from django import forms


class ScanForm(forms.Form):
    plan_list = (
        ('manual', 'manual'),
        ('auto', 'auto'),
        ('both', 'both'),
    )
    address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'address',
                'autocomplete': 'off',
                'placeholder': 'xyz.com',
            }
        ),
        max_length=50,
        label='Address',
    )

    plan = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'plan'
            }
        ),
        choices=plan_list,
        label='Plan'
    )