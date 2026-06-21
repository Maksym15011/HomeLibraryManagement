from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),

    path('book/<int:book_id>/', views.book, name='book'),

    path('book/<int:book_id>/add-note/',views.add_note,name='add_note'),

    path('book/<int:book_id>/favorite/',views.toggle_favorite,name='toggle_favorite'),

    path('book/<int:book_id>/read/',views.toggle_read,name='toggle_read'),

    path("book/add/",views.add_book,name="add_book"),

    path("book/<int:book_id>/edit/",views.edit_book,name="edit_book"),

    path("book/<int:book_id>/delete/",views.delete_book,name="delete_book"),

    path('authors/', views.authors, name='authors'),
    path('author/<int:author_id>/', views.author, name='author'),

    path('publishers/', views.publishers, name='publishers'),
    path('publisher/<int:publisher_id>/', views.publisher, name='publisher'),

    path('series/', views.series_list, name='series_list'),
    path('series/<int:series_id>/', views.series, name='series'),

    path('genres/', views.genres, name='genres'),
    path('topics/', views.topics, name='topics'),

    path('notes/', views.notes, name='notes'),
    path('note/<int:note_id>/', views.note, name='note'),

    

    
]