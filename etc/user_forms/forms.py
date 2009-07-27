from django import forms
from django.contrib.localflavor.us import forms as lfus
#from etcetera.structure import models as structure

class ServiceForm(forms.Form):
	name = forms.CharField(max_length=200)
	department = forms.CharField(max_length=100)
	phone = lfus.USPhoneNumberField()
	email = forms.EmailField()
	building = forms.CharField(max_length=25)
	#building = forms.ModelChoiceField(queryset=structure.Building.objects.all(), required=True)
	room = forms.CharField(max_length=15)
	equipment_text = forms.CharField(max_length=75)
	barcode = forms.CharField(max_length=6, required=False)
	description = forms.CharField(widget=forms.Textarea)