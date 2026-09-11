from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):

    class Meta:
        model = Profile
        fields = [
            'full_name',
            'email',
            'phone_number',
            'dob',
        ]


    def clean_full_name(self):
        full_name = self.cleaned_data['full_name'].strip()

        if len(full_name) < 6:
            raise forms.ValidationError(
                'Full name must contain at least 6 characters.'
            )

        return full_name

    def clean_phone_number(self):
        phone = self.cleaned_data['phone_number'].strip()

        if not phone.startswith('0'):
            raise forms.ValidationError(
                'Phone number must start with 0.'
            )
        if len(phone) != 10:
            raise forms.ValidationError(
                'Rwandan phone number must be in the format 07XXXXXXXX.'
            )
        return phone

    def clean_email(self):
        email = self.cleaned_data['email'].lower().strip()

        if Profile.objects.filter(email=email).exclude(
            pk=self.instance.pk
        ).exists():
            raise forms.ValidationError(
                'This email is already registered.'
            )

        return email
    