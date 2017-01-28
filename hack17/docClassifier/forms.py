from django import forms

class UploadFileForm(forms.Form):
	file = forms.FileField(label="File");

class DocumentURIForm(forms.Form):
	uri = forms.CharField(label='uri')