from django import forms


EMPTY_CHOICES = (
    ('', '-'*10),
)

NUM_CHOICES = (
    ('2', '2名'),
    ('3', '3名'),
    ('4', '4名'),
)

COURSE_CHOICES = (
    ('courseA', 'Aコース'),
    ('courseB', 'Bコース'),
    ('tables', '席のみ'),
)


class ResForm(forms.Form):
    name = forms.CharField(
        label='名前',
        max_length=20,
        required=True,
        widget=forms.TextInput()
    )

    datetime = forms.DateTimeField(
        label='日時',
        required=True,
        widget=forms.DateTimeInput(attrs={"type": "datetime-local"}),
        input_formats=['%Y-%m-%dT%H:%M']
    )

    num = forms.ChoiceField(
        label='人数',
        widget=forms.Select,
        choices=EMPTY_CHOICES + NUM_CHOICES,
        required=True,
    )

    course = forms.ChoiceField(
        label='コース',
        widget=forms.RadioSelect,
        choices=COURSE_CHOICES,
        required=True,
    )

    comment = forms.CharField(
        label='備考',
        max_length=1000,
        required=False,
        widget=forms.TextInput()
    )
