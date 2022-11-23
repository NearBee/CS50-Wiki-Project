from django import forms


class entry_form(forms.Form):
    title = forms.CharField(
        label="Title",
        min_length=1,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Entry Title",
                "class": "form-control",
            }
        ),
    )
    body = forms.CharField(
        label="Body contents",
        min_length=1,
        widget=forms.Textarea(
            attrs={
                "placeholder": "#Title"
                + "\n\n\n"
                + "Information about the Title goes here.",
                "class": "form-control col-lg-10",
            }
        ),
    )


class edit_form(forms.Form):
    title = forms.CharField(
        label="Title",
        min_length=1,
        widget=forms.TextInput(
            attrs={
                "readonly": "readonly",
                "placeholder": "#Title",
                "class": "form-control",
            }
        ),
    )
    body = forms.CharField(
        label="Body Content",
        min_length=1,
        widget=forms.Textarea(
            attrs={
                "placeholder": "#Title"
                + "\n\n\n"
                + "Information about the Title goes here.",
                "class": "form-control",
            }
        ),
    )
