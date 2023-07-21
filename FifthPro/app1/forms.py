

from django import forms

from django.core import validators

class contactForm(forms.Form):
    name = forms.CharField(label= "Name", help_text="Must be in 30 charecters", required=True, disabled=False, widget=forms.Textarea(attrs={'id':'text_area', 'placeholder': 'Enter your name' }) )
    file = forms.FileField()
    
    email = forms.EmailField(label= "Useremail")
    age =  forms.IntegerField()
    weight = forms.FloatField()
    DOB = forms.DateField(widget=forms.DateInput(attrs={'type':'date'}))    # suggeition diba widget use korar karone
    CHOICES = [('S', 'Small'), ('L', 'Large'), ('M', 'Medium')]
    size = forms.ChoiceField(choices=CHOICES, widget = forms.RadioSelect)
    meal = [('P','Peparony'), ('M','Mashroom'), ('B', 'Beef')]
    pizza =  forms.MultipleChoiceField(choices=meal)
    
    
class studentdata(forms.Form):
        name = forms.CharField(widget=forms.TextInput, validators=[validators.MaxLengthValidator(10 ,message='Enter the correct size name')] )
        email = forms.CharField(widget=forms.EmailInput)
        age = forms.CharField()
        
        file = forms.FileField(validators=[validators.FileExtensionValidator(allowed_extensions=['pdf'], message= ' File should be in .pdf formated' )])
        # def clean_name(self):
        #     valname = self.cleaned_data['name']
        #     if len(valname) < 10:
        #         raise forms.ValidationError("Enter a name at least 10 characters")
        #     return valname
        
        
        # def clean_email(self):
        #     valmail = self.cleaned_data['email']
        #     if '.com' not in valmail:
        #         raise forms.ValidationError("Invalid formate")
        #     return valmail
        
        # def clean(self):
        #     cleaned_data = super().clean()
        #     valname = self.cleaned_data['name']
        #     valmail = self.cleaned_data['email']
            
        #     if len(valname) < 10:
        #         raise forms.ValidationError("Enter a name at least 10 characters")
            
            
        #     if '.com' not in valmail:
        #         raise forms.ValidationError("Invalid formate")
            
    
    
    
    
class passwordValidationProject(forms.Form):
    
    name = forms.CharField(widget=forms.TextInput)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_pass = forms.CharField(widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()
        val_pass = self.cleaned_data['password']
        val_compass = self.cleaned_data['confirm_pass']
        val_name = self.cleaned_data['name']
        if val_compass != val_pass:
            raise forms.ValidationError("Password doesn't match")
        
        if len(val_name) < 10:
            raise forms.ValidationError("Name must be is 10 charactes")
        
     
        
        
        