from django.urls import path

from notes.views import todo, edit, delete ##This is optimized


urlpatterns = [
    path('', todo, name='todo'),# Home page route
    path('edit/<int:id>/',edit,name='edit'),
    path('delete/<int:id>/', delete, name='delete'),

]