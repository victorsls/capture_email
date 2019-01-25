from django import forms


class CaptureEmailForm(forms.Form):
    email = forms.EmailField(
        max_length=100,
        widget=forms.TextInput(
            attrs={
                'class': 'form-control col-sm',
                'placeholder': 'Digite aqui o seu melhor e-mail',
            },
        )

    )
