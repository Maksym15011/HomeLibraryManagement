from django.shortcuts import render
from .models import Author, Book, Genre, Note, Publisher, Series
from django.forms import modelform_factory
from django.shortcuts import (
    render,
    get_object_or_404,
    redirect
)

from django.contrib.auth.decorators import login_required

from .models import (
    Author,
    Book,
    Genre,
    Note,
    Publisher,
    Series,
    Topic,
)


def index(request):

    books = Book.objects.all()

    authors = Author.objects.all()
    genres = Genre.objects.all()

    search = request.GET.get("search")

    if search:
        books = books.filter(
            title__icontains=search
        )

    author = request.GET.get("author")

    if author:
        books = books.filter(
            authors__id=author
        )

    genre = request.GET.get("genre")

    if genre:
        books = books.filter(
            genres__id=genre
        )

    return render(
        request,
        "manage_books/index.html.jinja",
        {
            "books": books.distinct(),
            "authors": authors,
            "genres": genres,
        }
    )


def book(request, book_id):
    return render(request, "manage_books/book.html", {"book_id": book_id})


def author(request, author_id):
    return render(request, "manage_books/author.html", {"author_id": author_id})


def publisher(request, publisher_id):
    return render(request, "manage_books/publisher.html", {"publisher_id": publisher_id})


def series(request, series_id):
    return render(request, "manage_books/series.html", {"series_id": series_id})


def note(request, note_id):
    return render(request, "manage_books/note.html", {"note_id": note_id})

def authors(request):
    authors = Author.objects.all()
    return render(request, 'manage_books/authors.html.jinja', {'authors': authors})

def publishers(request):
    publishers = Publisher.objects.all()
    return render(request, 'manage_books/publisher.html.jinja', {'publishers': publishers})

def series_list(request):
    series = Series.objects.all()
    return render(request, 'manage_books/series_list.html.jinja', {'series': series})

def notes(request):
    notes = Note.objects.all()
    return render(request, 'manage_books/notes.html.jinja', {'notes': notes})



def book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    return render(
        request,
        "manage_books/book.html.jinja",
        {
            "book": book,
        }
    )

def authors(request):
    authors = Author.objects.all()

    return render(
        request,
        "manage_books/authors.html.jinja",
        {
            "authors": authors,
        }
    )

def author(request, author_id):
    author = get_object_or_404(
        Author,
        pk=author_id
    )

    return render(
        request,
        "manage_books/author.html.jinja",
        {
            "author": author,
        }
    )

def publishers(request):
    publishers = Publisher.objects.all()

    return render(
        request,
        "manage_books/publishers.html.jinja",
        {
            "publishers": publishers,
        }
    )

def publisher(request, publisher_id):
    publisher = get_object_or_404(
        Publisher,
        pk=publisher_id
    )

    return render(
        request,
        "manage_books/publisher.html.jinja",
        {
            "publisher": publisher,
        }
    )

def series_list(request):
    series = Series.objects.all()

    return render(
        request,
        "manage_books/series_list.html.jinja",
        {
            "series": series,
        }
    )

def series(request, series_id):
    series = get_object_or_404(
        Series,
        pk=series_id
    )

    return render(
        request,
        "manage_books/series.html.jinja",
        {
            "series": series,
        }
    )

def genres(request):
    genres = Genre.objects.all()

    return render(
        request,
        "manage_books/genres.html.jinja",
        {
            "genres": genres,
        }
    )

def topics(request):
    topics = Topic.objects.all()

    return render(
        request,
        "manage_books/topics.html.jinja",
        {
            "topics": topics,
        }
    )

def notes(request):
    notes = Note.objects.all()

    return render(
        request,
        "manage_books/notes.html.jinja",
        {
            "notes": notes,
        }
    )

def note(request, note_id):
    note = get_object_or_404(
        Note,
        pk=note_id
    )

    return render(
        request,
        "manage_books/note.html.jinja",
        {
            "note": note,
        }
    )

@login_required
def add_note(request, book_id):

    book = get_object_or_404(
        Book,
        pk=book_id
    )

    if request.method == "POST":

        content = request.POST.get(
            "content"
        )

        if content:

            Note.objects.create(
                content=content,
                book=book,
                user=request.user
            )

    return redirect(
        "book",
        book_id=book.id
    )


@login_required
def toggle_favorite(request, book_id):

    book = get_object_or_404(
        Book,
        pk=book_id
    )

    book.is_favorite = (
        not book.is_favorite
    )

    book.save()

    return redirect(
        "book",
        book_id=book.id
    )


@login_required
def toggle_read(request, book_id):

    book = get_object_or_404(
        Book,
        pk=book_id
    )

    book.is_read = (
        not book.is_read
    )

    book.save()

    return redirect(
        "book",
        book_id=book.id
    )

@login_required
def add_book(request):

    BookForm = modelform_factory(
        Book,
        exclude=[]
    )

    if request.method == "POST":

        form = BookForm(request.POST)

        if form.is_valid():

            book = form.save()

            return redirect(
                "book",
                book_id=book.id
            )

    else:

        form = BookForm()

    return render(
        request,
        "manage_books/book_form.html.jinja",
        {
            "form": form,
            "title": "Dodaj książkę"
        }
    )

@login_required
def edit_book(request, book_id):

    book = get_object_or_404(
        Book,
        pk=book_id
    )

    BookForm = modelform_factory(
        Book,
        exclude=[]
    )

    if request.method == "POST":

        form = BookForm(
            request.POST,
            instance=book
        )

        if form.is_valid():

            form.save()

            return redirect(
                "book",
                book_id=book.id
            )

    else:

        form = BookForm(
            instance=book
        )

    return render(
        request,
        "manage_books/book_form.html.jinja",
        {
            "form": form,
            "title": "Edytuj książkę"
        }
    )

@login_required
def delete_book(request, book_id):

    book = get_object_or_404(
        Book,
        pk=book_id
    )

    if request.method == "POST":
        book.delete()

    return redirect("index")