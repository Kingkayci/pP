from django import forms
from .models import ContactForm

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = ContactForm
        fields = ['contact_name', 'contact_email', 'contact_subject', 'contact_message']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["contact_name"].widget.attrs.update({
            "type":"text", 
            "placeholder": "Name", 
            "maxlength":"40", 
            "minlength":"5",
        })

        self.fields["contact_email"].widget.attrs.update({
            "type":"email", 
            "placeholder":"Email",  
            "maxlength":"40", 
            "minlength":"5",
        })
        
        self.fields["contact_subject"].widget.attrs.update({
            "type":"text",
            "placeholder": "Subject",  
            "maxlength":"40", 
            "minlength":"5",
        })

        self.fields["contact_message"].widget.attrs.update({
            "type":"text",
            "placeholder": "Your Message",  
            "maxlength":"999", 
            "minlength":"5",
            "row": "4"
        })


