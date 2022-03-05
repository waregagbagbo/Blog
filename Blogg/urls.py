from django.urls import path
from .import views
app_name='Blogg'


urlpatterns=[
    path('',views.index,name='index'),
    path('upload',views.upload, name='upload'),
    path('update/<int:book_id>',views.updateBook, name= 'update'),
    path('delete/<int:book_id>', views.delete_book, name='delete'),    
]