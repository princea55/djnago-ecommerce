from django import forms
from .models import Teacher
from django.core.validators import validate_email


class TeacherForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Enter your name...', 'required': True}))

    class Meta:
        model = Teacher
        fields = ['name', 'email', 'city', 'age', 'gender', 'dob', 'join_date', 'phone', 'user_id', 'skil']

    # def validate(self, value):
    #     super().validate(value)
    #     for email in value:
    #         validate_email(email)

    def clean(self):
        age = self.cleaned_data['age']
        if age > 18:  # order can be fulfilled
            print("Order placed!")
        else:
            raise forms.ValidationError({'age': "Age must be greater than 18."})
