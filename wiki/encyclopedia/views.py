from django.shortcuts import redirect, render

from . import forms, util


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


def new_page(request):
    if request.method == "POST":
        title_form = forms.new_page_form(request.POST)
        if title_form.is_valid():
            title = title_form.cleaned_data["title"]
            body = title_form.cleaned_data["body"]
            if title in util.list_entries():
                title_form.add_error("title", "This entry already exists.")
                return render(
                    request,
                    "encyclopedia/new_page.html",
                    {"title": title_form},
                )
            else:
                util.save_entry(title, body)
                return redirect("entry", title=title)

    else:
        title_form = forms.new_page_form()
        return render(
            request,
            "encyclopedia/new_page.html",
            {"title": title_form},
        )


def edit_page(request):
    return NotImplemented
