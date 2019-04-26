from django import forms

from .models import Contact, FreeQuote, Newletter


class PostForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = '__all__'


class FreequoteForm(forms.ModelForm):

	class Meta:
		model = FreeQuote
		fields = '__all__'


class NewletterForm(forms.ModelForm):

	class Meta:
		model = Newletter
		fields = '__all__'