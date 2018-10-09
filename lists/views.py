from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item, List

# there are now 2 views that are responsible
# for adding a new item to the table, and for
# redirecting to the table view, there are
# new_list and view_list respectively
def home_page(request):
    return render(request, 'home.html')

# this view will be the redirected to after
# the user has created a new Item, to view
# view function that redirects to the current list
# for the specified list_id
def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    # we can pass only the list to the template
    # and use list.item_set.all to iterate through
    # the items
    return render(request, 'list.html', {
        'list' : list_,
    })

# view function for a new item creation (for a new list)
def new_list(request):
    # create an Instance of the Item class defined in models
    # this is equivalent to creating a new entry in the Item
    # table, set the text value equal to the input from the user
    # which will be part of the POST request
    # then redirect to the view_list view
    list_ = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')

# view function for a new item creation (for an existing list)
def new_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    # redirects to view_list function
    return redirect(f'/lists/{list_.id}/')