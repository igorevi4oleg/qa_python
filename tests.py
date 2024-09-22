from main import BooksCollector

from main import BooksCollector

class TestBooksCollector:

    # Тест для метода add_new_book
    def test_add_new_book(self):
        collector = BooksCollector()
        collector.add_new_book("Граф Монте-Кристо")
        assert "Граф Монте-Кристо" in collector.get_books_genre(), "Ошибка: Книга не добавлена"

    # Тест для метода add_new_book 40+
    def test_add_new_book_name_too_long(self):
        collector = BooksCollector()
        long_name = "Г" * 41  # Длиннее 40 символов
        collector.add_new_book(long_name)
        assert long_name not in collector.get_books_genre(), "Ошибка: Книга с длинным именем добавлена"

    # Тест для метода set_book_genre
    def test_set_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Граф Монте-Кристо")
        collector.set_book_genre("Граф Монте-Кристо", "Фантастика")
        assert collector.get_book_genre("Граф Монте-Кристо") == "Фантастика", "Ошибка: Жанр книги не установлен"

    # Тест для метода set_book_genre с несуществующим жанром
    def test_set_invalid_book_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Граф Монте-Кристо")
        collector.set_book_genre("Граф Монте-Кристо", "Триллер")
        assert collector.get_book_genre("Граф Монте-Кристо") != "Триллер", "Ошибка: Неверный жанр установлен"

    # Тест для метода get_books_with_specific_genre
    def test_get_books_with_specific_genre(self):
        collector = BooksCollector()
        collector.add_new_book("Граф Монте-Кристо")
        collector.set_book_genre("Граф Монте-Кристо", "Фантастика")
        collector.add_new_book("Вождь краснокожих")
        collector.set_book_genre("Вождь краснокожих", "Комедии")
        assert "Граф Монте-Кристо" in collector.get_books_with_specific_genre("Фантастика"), "Ошибка: Книга с жанром не найдена"
        assert "Граф Монте-Кристо" not in collector.get_books_with_specific_genre("Комедии"), "Ошибка: Неверная книга в списке"

    # Тест для метода get_books_for_children
    def test_get_books_for_children(self):
        collector = BooksCollector()
        collector.add_new_book("Граф Монте-Кристо")
        collector.set_book_genre("Граф Монте-Кристо", "Фантастика")
        collector.add_new_book("Вождь краснокожих")
        collector.set_book_genre("Вождь краснокожих", "Ужасы")
        assert "Граф Монте-Кристо" in collector.get_books_for_children(), "Ошибка: Детская книга не найдена"
        assert "Вождь краснокожих" not in collector.get_books_for_children(), "Ошибка: Книга для взрослых в списке"

    # Тест для метода add_book_in_favorites
    def test_add_book_in_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Граф Монте-Кристо")
        collector.add_book_in_favorites("Граф Монте-Кристо")
        assert "Граф Монте-Кристо" in collector.get_list_of_favorites_books(), "Ошибка: Книга не добавлена в избранное"

    # Тест для метода delete_book_from_favorites
    def test_delete_book_from_favorites(self):
        collector = BooksCollector()
        collector.add_new_book("Граф Монте-Кристо")
        collector.add_book_in_favorites("Граф Монте-Кристо")
        collector.delete_book_from_favorites("Граф Монте-Кристо")
        assert "Граф Монте-Кристо" not in collector.get_list_of_favorites_books(), "Ошибка: Книга не удалена из избранного"

    # Тест для метода get_list_of_favorites_books
    def test_get_list_of_favorites_books(self):
        collector = BooksCollector()
        collector.add_new_book("Граф Монте-Кристо")
        collector.add_book_in_favorites("Граф Монте-Кристо")
        collector.add_new_book("Вождь краснокожих")
        collector.add_book_in_favorites("Вождь краснокожих")
        favorites = collector.get_list_of_favorites_books()
        assert favorites == ["Граф Монте-Кристо", "Вождь краснокожих"], "Ошибка: Список избранных книг некорректен"


# Запуск тестов вручную
if __name__ == "__main__":
    tests = TestBooksCollector()
    tests.test_add_new_book()
    tests.test_add_new_book_name_too_long()
    tests.test_set_book_genre()
    tests.test_set_invalid_book_genre()
    tests.test_get_books_with_specific_genre()
    tests.test_get_books_for_children()
    tests.test_add_book_in_favorites()
    tests.test_delete_book_from_favorites()
    tests.test_get_list_of_favorites_books()

    print("Все тесты успешно пройдены!")