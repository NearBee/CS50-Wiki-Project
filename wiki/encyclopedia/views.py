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
        form = forms.entry_form(request.POST)
        if form.is_valid():
            title = form.cleaned_data["title"]
            if not title in util.list_entries():
                body = form.cleaned_data["body"]
                util.save_entry(title, body)

                return redirect("entry", title=title)

            form.add_error("title", "This entry already exists.")

        else:
            if not form.cleaned_data["title"]:
                form.add_error("title", "Title is required.")

            if not form.cleaned_data["body"]:
                form.add_error("body", "Body is required.")

        return render(
            request,
            "encyclopedia/new_page.html",
            {"form": form},
        )

    else:
        form = forms.entry_form()

        return render(
            request,
            "encyclopedia/new_page.html",
            {"form": form},
        )


def edit_page(request, title):
    page_contents = util.get_entry(title)
    form = forms.entry_form(initial={"title": title, "body": page_contents})

    if not page_contents:
        return render(
            request,
            "encyclopedia/entry_error.html",
            {"title": title},
        )

    else:
        if request.method == "POST":
            print("We are POST")
            form = forms.entry_form(request.POST)

            if form.is_valid():
                page_title = form.cleaned_data["title"]
                body = form.cleaned_data["body"]
                util.save_entry(page_title, body)

                return redirect("entry", title=title)

            else:
                # blows up
                pass
    return render(request, "encyclopedia/edit_page.html", {"form": form})
