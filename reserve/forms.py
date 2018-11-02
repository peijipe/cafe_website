from django import forms

from django.forms import ModelForm
from .models import Reserve


class ResForm(ModelForm):
    class Meta:
        model = Reserve
        fields = "__all__"


# EMPTY_CHOICES = (
#     ('', '-'*10),
# )
#
# NUM_CHOICES = (
#     ('2', '2名'),
#     ('3', '3名'),
#     ('4', '4名'),
# )
#
# COURSE_CHOICES = (
#     ('courseA', 'Aコース'),
#     ('courseB', 'Bコース'),
#     ('tables', '席のみ'),
# )
#
#
# class ReserveForm(forms.Form):
#     # date = forms.DateField(
#     #     label='日時',
#     #     required=True,
#     #     input_formats=[
#     #         '%Y-%m-%d',  # 2018-10-10
#     #     ]
#     # )
#
#     num = forms.ChoiceField(
#         label='人数',
#         widget=forms.Select,
#         choices=EMPTY_CHOICES + NUM_CHOICES,
#         required=True,
#     )
#
#     course = forms.ChoiceField(
#         label='コース',
#         widget=forms.RadioSelect,
#         choices=COURSE_CHOICES,
#         required=True,
#     )
#
#     comment = forms.CharField(
#         label='備考',
#         max_length=1000,
#         required=False,
#         widget=forms.TextInput()
#     )
