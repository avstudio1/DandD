from django import forms

class ContactForm(forms.Form):
    contact_name = forms.CharField(required=True, label="Name (*required)")
    contact_email = forms.EmailField(required=True, label="Email (*required)")
    contact_phone = forms.CharField(required=False, label="Telephone (*required)")
    content = forms.CharField(
        required=True,
        widget=forms.Textarea,
        label="Message"
    )