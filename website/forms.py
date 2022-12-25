from django import forms

from .models import *

subject_list = (
    ("message", "message"),
    ("bug", "bug"),
    ("idea", "idea"),
    ("criticism", "criticism"),
    ("questions", "questions"),
    ("other", "other"),
)


class ContactForm(forms.Form):
    title = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'title',
                'placeholder': 'Enter Message Title'
            }
        ),
        required=False,
        max_length=50,
        label='Title'
    )

    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'first_name',
                'placeholder': 'Enter Your First Name'
            }
        ),
        max_length=50,
        label='First Name',
        required=False
    )

    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'last_name',
                'placeholder': 'Enter Your Last Name'
            }
        ),
        max_length=50,
        label='Last Name',
        required=False
    )

    email = forms.CharField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'id': 'email',
                'placeholder': 'name@example.com'
            }
        ),
        required=False
    )

    phone = forms.CharField(
        widget=forms.NumberInput(
            attrs={
                'class': 'form-control',
                'id': 'phone',
                'placeholder': 'Enter Phone Number'
            }
        ),
        required=False,
        max_length=13,
        label='phone'
    )

    subject = forms.ChoiceField(
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'subject'
            }
        ),
        choices=subject_list,
        label='Subject'
    )

    message = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'class': 'form-control',
                'id': 'message',
                'placeholder': 'Leave a comment here'
            }
        ),
        label='Message'
    )

    def save(self):
        Contact.objects.create(
            title=self.cleaned_data.get('title'),
            first_name=self.cleaned_data.get('first_name'),
            last_name=self.cleaned_data.get('last_name'),
            email=self.cleaned_data.get('email'),
            phone=self.cleaned_data.get('phone'),
            subject=self.cleaned_data.get('subject'),
            message=self.cleaned_data.get('message')
        )


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'username',
                'autocomplete': 'off',
            }
        ),
        max_length=50,
        label='Username',
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'password',
                'data-validate-field': 'loginPassword'
            }
        ),
        max_length=50,
        label='Password',
    )


class RegisterForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'username',
                'autocomplete': 'off',
            }
        ),
        max_length=50,
        label='Username',
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'id': 'email',
                'autocomplete': 'off',
            }
        ),
        max_length=50,
        label='Email',
    )

    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'password',
                'data-validate-field': 'loginPassword'
            }
        ),
        max_length=50,
        label='Password',
    )


class ForgetForm(forms.Form):
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'id': 'email',
                'autocomplete': 'off',
            }
        ),
        max_length=50,
        label='Email',
    )