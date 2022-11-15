from django import forms


class entry_form(forms.Form):
    title = forms.CharField(
        label="Title:",
        min_length=1,
    )
    body = forms.CharField(
        label="Body contents:",
        min_length=1,
    )
