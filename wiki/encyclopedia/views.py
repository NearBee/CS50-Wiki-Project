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


def new_page(request):
    return render(request, "encyclopedia/new_page.html")
