from django import forms
from  .mmodels import Messages

class MForm(forms.ModelForm):
    class Meta:
         model = Messages
         fields = "__all__"
