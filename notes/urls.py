from django.urls import path,include
from .views import show_notes,create_note

urlpatterns = [
        path("addnote/",create_note,name='addnote'),
        path("",show_notes,name='view'),
]