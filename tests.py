from main import BooksCollector
import pytest

class TestBooksCollector:
    book_name_list = [
        'Harry Porter and the Philosophers Stone',
        'Harry Porter and the Chamber of Secrets',
        'Harry Porter and the Prisoner of Azkaban',
        'Harry Porter and the Goblet of Fire',
        'Harry Potter and the Half-Blood Prince'
    ]
    genre_list = ['Фантастика', 'Ужасы', 'Детективы', 'Мультфильмы', 'Комедии']
    book_name_not_allowed_length = ['Harry Porter and the Order ot the Phoenix']

    @pytest.mark.parametrize('book_name_first, book_name_second', [[book_name_list[0], book_name_list[1]]])
    def test_add_new_book_add_two_books_added(self,book_name_first,book_name_second):
        collector = BooksCollector()
        collector.add_new_book(book_name_first)
        collector.add_new_book(book_name_second)
        assert len(collector.books_genre) == 2

    @pytest.mark.parametrize('book_name', book_name_list)
    def test_add_new_book_add_duplicate_name_not_added(self,book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.add_new_book(book_name)
        assert len(collector.books_genre) == 1

    @pytest.mark.parametrize('book_name', book_name_not_allowed_length)
    def test_add_new_book_add_more_than_the_allowed_length_name_not_added(self,book_name):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        assert len(collector.books_genre) == 0

    @pytest.mark.parametrize('book_name, genre', [[book_name_list[0], genre_list[1]]])
    def test_set_book_genre_add_existing_book_and_genre_added_genre(self,book_name,genre):
        collector = BooksCollector()
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.books_genre[book_name] == genre

    def test_get_book_genre_get_existing_book_genre(self):
        collector = BooksCollector()
        book_name = self.book_name_list[0]
        genre = self.genre_list[0]
        collector.add_new_book(book_name)
        collector.set_book_genre(book_name, genre)
        assert collector.get_book_genre(book_name) == genre

    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book(self.book_name_list[0])
        collector.set_book_genre(self.book_name_list[0], self.genre_list[0])
        collector.add_new_book(self.book_name_list[1])
        collector.set_book_genre(self.book_name_list[1], self.genre_list[0])
        collector.add_new_book(self.book_name_list[2])
        collector.set_book_genre(self.book_name_list[2], self.genre_list[1])
        assert len(collector.get_books_with_specific_genre(self.genre_list[0])) == 2

    def test_get_books_genre(self):
        collector = BooksCollector()
        collector.add_new_book(self.book_name_list[0])
        collector.set_book_genre(self.book_name_list[0], self.genre_list[0])
        assert len(collector.get_books_genre()) == 1

    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book(self.book_name_list[0])
        collector.set_book_genre(self.book_name_list[0], self.genre_list[3])
        assert len(collector.get_books_for_children()) == 1

    def test_add_book_in_favorites_added(self):
        collector = BooksCollector()
        collector.add_new_book(self.book_name_list[0])
        collector.add_book_in_favorites(self.book_name_list[0])
        assert len(collector.favorites) == 1

    def test_delete_book_from_favorites_deleted(self):
        collector = BooksCollector()
        collector.add_new_book(self.book_name_list[0])
        collector.add_book_in_favorites(self.book_name_list[0])
        collector.add_new_book(self.book_name_list[1])
        collector.add_book_in_favorites(self.book_name_list[1])
        collector.delete_book_from_favorites(self.book_name_list[0])
        assert len(collector.favorites) == 1

    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book(self.book_name_list[0])
        collector.add_book_in_favorites(self.book_name_list[0])
        assert len(collector.get_list_of_favorites_books()) == 1