from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item

# there are now 2 views that are responsible
# for adding a new item to the table, and for
# redirecting to the table view, there are
# new_list and view_list respectively
def home_page(request):
    return render(request, 'home.html')

# this view will be the redirected to after
# the user has created a new Item, to view
# the current list
def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {
        'items': items
    })

def new_list(request):
    # create an Instance of the Item class defined in models
    # this is equivalent to creating a new entry in the Item
    # table, set the text value equal to the input from the user
    # which will be part of the POST request
    # then redirect to the view_list view
    Item.objects.create(text=request.POST['item_text'])
    return redirect('/lists/the-only-list-in-the-world/')