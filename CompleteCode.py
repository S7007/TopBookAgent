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



from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
agent = BookAgent()

class GenreRequest(BaseModel):
    genre: str

class BookSelectionRequest(BaseModel):
    book_name: str

@app.post("/top-100-books")
def get_top_100_books(request: GenreRequest):
    books = agent.find_top_100_books(request.genre)
    return {"top_100_books": books}

@app.get("/top-10-books")
def get_top_10_books():
    books = agent.find_top_10_books()
    return {"top_10_books": books}

@app.post("/select-book")
def select_book(request: BookSelectionRequest):
    selected_book = agent.select_book(request.book_name)
    if not selected_book:
        raise HTTPException(status_code=404, detail="Book not found in top 10")
    return {"selected_book": selected_book}

@app.get("/conclude")
def conclude():
    message = agent.conclude()
    return {"message": message}


import streamlit as st
import requests

st.title("Book Selection Agent")

base_url = "http://127.0.0.1:8000"

genre = st.text_input("Enter a genre")
if st.button("Get Top 100 Books"):
    response = requests.post(f"{base_url}/top-100-books", json={"genre": genre})
    st.write(response.json())

if st.button("Get Top 10 Books"):
    response = requests.get(f"{base_url}/top-10-books")
    st.write(response.json())

book_name = st.text_input("Enter the name of the book you want to select")
if st.button("Select Book"):
    response = requests.post(f"{base_url}/select-book", json={"book_name": book_name})
    st.write(response.json())

if st.button("Conclude"):
    response = requests.get(f"{base_url}/conclude")
    st.write(response.json())

