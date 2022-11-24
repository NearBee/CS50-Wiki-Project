# CS50w Wiki

## Description:
For practice using HTML and CSS using Django, in the CS50w class we were assigned a project of creating a functional Wiki page where each entry would then have an entry page, as well as being able to create a new page or even edit an existing page. The user could also use a search function and finally use the "Random Page" button to be given a random page from the selection of entries.

---

### ***Index Page***:
The Index page is a page that contain links to each of the available entries that have already been created, by clicking a link at the center of the screen the user will be brought to the entries' page, there is also the sidebar (which is also present on every page of the wiki) that has a number of different links with functions that do many different things such as, creating a new page or even getting a random page from the selection of entries already created.

![Index Page](/Wiki_Webapp_Pictures/Index_page.png)

---

### ***Search Results***:
The Search Results page gives the user either the entry that they searched for if the query matches the entry exactly (Ex: searching 'Python' would return the Python entry page), or would gives entries if the query substring matches anything that would contain that substring (Ex: searching 'pyth' would return 'Python' as a suggested search). If neither of the previous two options would happen due to the query not matching anything in the currently existing entries the user is then prompted to either return to the index page or to be given the opportunity to create a new page.

![Search Results](/Wiki_Webapp_Pictures/Search_Results.png)

---

### ***Entry Page***:
Each entry will be shown on the entry page with title and body contents displayed to the user, there will also be an edit page button at the top-right of the screen that will allow the user to make edits to the page that they are on which will then be reflected onto the page once the "Submit" button is pressed.

![Entry Page](/Wiki_Webapp_Pictures/Entry_page.png)

---

### ***Edit Page***:
On the Edit Page it will show the contents of the page that you're trying to edit, while the Title is not possible to edit the body contents are free to be changed and are currently shown in a Markdown styling which is then converted using Markdown2 to convert the Markdown content to HTML to be read in a much more user-friendly way.

![Edit Page](/Wiki_Webapp_Pictures/Edit_page.png)

---

### ***Create New Page***:
In a similar fashion to the Edit Page there is an empty field for the Title (that is no longer just a readable field) as well as an empty Body Content textfield with a placeholder instructing the user on how to use some very simple Markdown to create an entry to be displayed when clicking "Create Page" at the bottom of the fields.

![Create New Page](/Wiki_Webapp_Pictures/Create_new_page.png)

Thank you for taking time to read the README!
