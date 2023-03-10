from django import forms

from django.contrib.auth.hashers import make_password, check_password
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

    remember_me = forms.BooleanField(
        widget=forms.CheckboxInput(
            attrs={
                'class': 'form-check-input',
                'id': 'remember_me',
            }
        ),
        label='Remember Me On This Device',
        required=False,
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

    referral = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'referral',
            }
        ),
        max_length=50,
        label='Referral',
        required=False,
    )

    def save(self, request):
        user = User.objects.create(
            username=self.cleaned_data.get('username'),
            password=make_password(self.cleaned_data.get('password'))
        )
        if self.cleaned_data.get('referral'):
            referral = User.objects.get(username=self.cleaned_data.get('referral'))
            Profile.objects.create(
                user=user,
                referral=referral,
            )
        else:
            Profile.objects.create(
                user=user,
            )
        return user


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


class TicketForm(forms.Form):
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

    def save(self, request):
        Ticket.objects.create(
            title=self.cleaned_data.get('title'),
            user=request.user,
            subject=self.cleaned_data.get('subject'),
            message=self.cleaned_data.get('message')
        )


class ProfileForm(forms.Form):
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

    referral = forms.CharField(
        widget=forms.TextInput(
            attrs={
                'class': 'form-control',
                'id': 'referral',
            }
        ),
        max_length=50,
        label='Referral',
        required=False,
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

    new_password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
                'id': 'new_password',
                'data-validate-field': 'loginPassword'
            }
        ),
        max_length=50,
        required=False,
        label='New Password',
    )

    def update(self, request):
        email = self.cleaned_data.get('email')
        first_name = self.cleaned_data.get('first_name')
        last_name = self.cleaned_data.get('last_name')
        phone = self.cleaned_data.get('phone')
        new_password = self.cleaned_data.get('new_password')

        if check_password(self.cleaned_data.get('password'), request.user.password):

            user = User.objects.get(id=request.user.id)
            profile = User.objects.get(id=request.user.id)

            if email:
                user.email = email

            if first_name:
                user.first_name = first_name

            if last_name:
                user.last_name = last_name

            if phone:
                user.phone = phone

            if new_password:
                user.password = make_password(new_password)

            profile.save()
            user.save()
