from django.shortcuts import render
from .models import Books, BorrowingRecords


def books_list(request):
    books = Books.objects.all()
    borrowing_records = BorrowingRecords.objects.filter(return_date__isnull=True)

    books_with_status = []
    for book in books:
        current_borrowing = borrowing_records.filter(book=book).first()
        status = "Available"
        if current_borrowing:
            status = f"Borrowed by {current_borrowing.member.name}"
        books_with_status.append({
            'title': book.title,
            'author': book.author.name,
            'status': status,
        })

    context = {
        'books_with_status': books_with_status
    }
    return render(request, 'book_app/books_list.html', context)
