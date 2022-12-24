from django import forms

from apps.scan.lib import create_address
from apps.scan.models import Website


class WebsiteForm(forms.Form):
    address = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'address',
                'autocomplete': 'off',
                'placeholder': 'test.com',
            }
        ),
        max_length=50,
        label='Address',
    )

    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'id': 'description',
                'row': '3',
            }
        ),
        label='Description',
    )

    def save(self, request):
        Website.objects.create(
            user=request.user,
            address=create_address(self.cleaned_data.get('address')),
            description=self.cleaned_data.get('description'),
            status='new',
        )
