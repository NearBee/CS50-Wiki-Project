from django import forms


class entry_form(forms.Form):
    title = forms.CharField(
        label="Title: ",
        min_length=1,
    )
    body = forms.CharField(
        label="Body contents: ",
        min_length=1,
        help_text="Please begin with '# ', then another space '_' and the rest of the body contents.",
    )


class edit_form(forms.Form):
    title = forms.CharField(
        label="Title",
        min_length=1,
        widget=forms.TextInput(attrs={"readonly": "readonly"}),
    )
    body = forms.CharField(
        label="Body Content",
        min_length=1,
        help_text="Please begin with '# ', then another space '_' and the rest of the body contents.",
    )
