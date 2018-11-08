from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(
        label='お名前',
        max_length=20,
        required=True,
    )

    email = forms.EmailField(
        label='メールアドレス',
        required=True,
    )

    message = forms.CharField(
        label='お問い合わせ内容',
        max_length=1000,
        required=True,
        widget=forms.Textarea
    )
