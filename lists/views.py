from django.shortcuts import render, redirect
from django.http import HttpResponse
from lists.models import Item

# Create your views here.
def home_page(request):
    # create an instance of the Item class (a record in the database)
    # set its text equal to the value passed by the POST request, or
    # empty if a normal GET request is made, and save the record
    if request.method == 'POST':
        Item.objects.create(text=request.POST['item_text'])
        # redirect, after adding a record to the database,
        # then the redirect will render the template below
        return redirect('/lists/the-only-list-in-the-world/')
    items = Item.objects.all()
    return render(request, 'home.html',{
        'items': items
    })

def view_list(request):
    items = Item.objects.all()
    return render(request, 'list.html', {
        'items': items
    })