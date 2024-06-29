# TopBookAgent
To develop a simple LLM-based autonomous agent for the specified workflow, we will proceed through the following steps:

1. **Setting up the Environment**: We'll choose appropriate tools and frameworks for developing our agent.
2. **Developing the Agent**: We'll create the agent to handle user requests and interact with the workflow.
3. **Building the REST API**: We'll use FastAPI to expose the agent's functionality through a REST API.
4. **Testing**: We'll develop a simple application to test our agent.
5. **Documentation and Demo**: We'll document our approach and create a demo video.

### Step 1: Setting up the Environment

We'll use the following tools:
- **Hugging Face Transformers**: For accessing pre-trained language models.
- **FastAPI**: For creating the REST API.
- **Python**: As the primary programming language.
- **GitHub**: For version control and sharing the solution.

### Step 2: Developing the Agent

We'll develop the agent to handle the following tasks:
- Find the top 100 books in a given genre.
- Filter the top 10 books from the 100.
- Select 1 book from the top 10 based on user input.
- Conclude the workflow with a thank you message.

Here's a sample implementation:

#### Agent Logic

```python
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
```

### Step 3: Building the REST API

We will use FastAPI to expose our agent's functionality.

#### FastAPI Application

```python
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
```

### Step 4: Testing

To test our API, we will create a simple Streamlit application. This application will interact with our FastAPI endpoints.

#### Streamlit Application

```python
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
```

### Step 5: Documentation and Demo

We will document the design choices and create a demo video.

#### Design Document

- **Why Hugging Face Transformers**: Provides pre-trained models and an easy-to-use pipeline.
- **Why FastAPI**: Fast and easy-to-use framework for building RESTful APIs.
- **Why Streamlit**: Simplifies the creation of interactive web applications for testing.

#### Demo Video

A demo video will show the interaction with the Streamlit application, demonstrating each step of the workflow.

### GitHub Repository

We will create a GitHub repository and include:
- All source code
- The design document
- The demo video

The repository will be shared in read mode as requested.

### Final Steps

1. Create a GitHub repository.
2. Add all the code, documentation, and video to the repository.
3. Share the repository link.

Let me know if you need any specific details on any part of this process.
