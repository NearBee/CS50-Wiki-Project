from django import forms
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {"entries": util.list_entries()})


def entry(request, title):
    page_contents = util.get_entry(title)
    if not page_contents:
        template = "encyclopedia/entry_error.html"
    else:
        template = "encyclopedia/entry.html"
    return render(
        request,
        template,
        {"title": title, "contents": page_contents},
    )


def search(request):
    keyword = request.GET.get("q")
    if keyword in util.list_entries():
        return redirect("entry", title=keyword)

    entries = []
    for entry in util.list_entries():
        if keyword in entry:
            entries.append(entry)
    return render(request, "encyclopedia/search.html", {"entries": entries})


class new_page_title_form(forms.Form):
    title = forms.CharField(
        label="Title:",
        min_length=1,
    )


class new_page_body_form(forms.Form):
    body = forms.CharField(
        label="Body contents:",
        min_length=1,
    )


def new_page(request):
    if request.method == "POST":
        title_form = new_page_title_form(request.POST)
        body_form = new_page_body_form(request.POST)
        if title_form.is_valid() and body_form.is_valid():
            title = title_form.cleaned_data["title"]
            body = body_form.cleaned_data["body"]
            util.save_entry(title, body)
            if title in util.list_entries():
                return redirect("entry", title=title)

    else:
        title_form = new_page_title_form()
        body_form = new_page_body_form()
        return render(
            request,
            "encyclopedia/new_page.html",
            {"title": title_form, "body": body_form},
        )
