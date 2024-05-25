from django import forms
 
# creating a form 
class InputForm(forms.Form):
 
    location = forms.CharField(max_length = 200, help_text="Enter location")
    disaster = forms.CharField(max_length = 200, help_text="Enter cause of damage")
    image = forms.ImageField(help_text = "Enter an image for severity analysis")