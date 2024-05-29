from django import forms
from django.core.validators import *
from app.models import * 
def validate_for_a(value):
    if value[0]=='a':
        raise forms.ValidationError('Start with a')
    
def validate_for_len(value):
    if len(value)<5:
        raise forms.ValidationError("length must be greater than 5")

class Student_data(forms.Form):
    Student_Name=forms.CharField(max_length=50)
    Student_age=forms.IntegerField()
    Student_email=forms.EmailField()
    Student_url=forms.URLField()
    
    Student_password=forms.CharField(widget=forms.PasswordInput)
    g=[("MALE",'male'),('FEMALE','female')]
    gender=forms.ChoiceField(choices=g,widget=forms.RadioSelect)
    gender1=forms.ChoiceField(choices=g)
    
    c=[('PYTHON','python'),("HTML",'html'),("CSS",'css')]
    Scourse=forms.MultipleChoiceField(choices=c,widget=forms.CheckboxSelectMultiple)
    Scourse1=forms.MultipleChoiceField(choices=c,widget=forms.SelectMultiple)
    
    Sdetails=forms.CharField(widget=forms.Textarea(attrs={"cols":10,'rows':10}))


class TopicForm(forms.Form):
    topic_name=forms.CharField(validators=[validate_for_a,validate_for_len])
    mobile=forms.CharField(min_length=10,max_length=10,validators=[RegexValidator('[6-9]\d{9}')])
    
class WebpageForm(forms.Form):
    topic_name=forms.ModelChoiceField(queryset=Topic.objects.all())
    name=forms.CharField(validators=[validate_for_a],label='NAME',help_text='used validator')
    url=forms.URLField()
    email=forms.EmailField()
    re_email=forms.EmailField()
    botcatcher=forms.CharField(widget=forms.HiddenInput,required=False)
    
    
    def clean_botcatcher(self):
        cu=self.cleaned_data['botcatcher']
        if len(cu)>0:
            raise forms.ValidationError("Bot is Catched ")
        
        
    def clean(self):
        e=self.cleaned_data['email']
        re=self.cleaned_data['re_email']
        if e!=re:
            raise forms.ValidationError("Email is mismatched ")
     