from django.db import models

# represents a List, will have a
# relationship with Item objects
class List(models.Model):
    pass

# represents a List Item, each Item
# is associated with a list as a ForeignKey
# to separate items by their respective list
class Item(models.Model):
    text = models.TextField(default='')
    # by setting on_delete to models.CASCADE, if a given List is deleted
    # all Item objects which contain that List as a ForeignKey will
    # be deleted
    list = models.ForeignKey(List, default=None, on_delete=models.CASCADE)