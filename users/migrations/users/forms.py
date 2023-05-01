forms django imort forms



class RegisterForm(forms.Form):
    username = forms.CharField(max_length=32)
    password1 = forms.CharField(widget=forms.PasswordInput(),
                                min_lengt=3)
    password1 = forms.CharField(widget=forms.PasswordInput(),
                                min_lengt=3)