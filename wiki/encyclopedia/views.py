from django.shortcuts import render

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
