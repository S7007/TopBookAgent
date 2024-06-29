from transformers import pipeline

class BookAgent:
    def __init__(self):
        self.genre = None
        self.top_100_books = None
        self.top_10_books = None
        self.selected_book = None
    
    def find_top_100_books(self, genre):
        self.genre = genre
        # Placeholder for actual book retrieval logic
        self.top_100_books = [f"Book {i}" for i in range(1, 101)]
        return self.top_100_books

    def find_top_10_books(self):
        if self.top_100_books:
            self.top_10_books = self.top_100_books[:10]
            return self.top_10_books
        return []

    def select_book(self, book_name):
        if self.top_10_books and book_name in self.top_10_books:
            self.selected_book = book_name
            return self.selected_book
        return None

    def conclude(self):
        return f"Thank you! You selected '{self.selected_book}'. Have a great day!"

# Initialize the agent
agent = BookAgent()
