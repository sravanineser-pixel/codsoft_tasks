# Task 3 – AI Book Recommendation System

## 📌 Project Overview

This project is an AI-based Book Recommendation System developed using Python as part of the CodSoft internship.

The system recommends books similar to a book entered by the user. It uses a content-based filtering approach by analyzing the author, genre, keywords, and description of books.

## 🎯 Objective

The main objective of this project is to build a book recommendation system that:

- Accepts a book name from the user
- Finds the selected book in the dataset
- Compares books based on their features
- Recommends five similar books
- Displays similarity scores for the recommendations

## 🛠️ Technologies Used

- Python
- Pandas
- Scikit-learn
- TF-IDF Vectorization
- Cosine Similarity
- Gradio

## 🧠 Recommendation Technique

This project uses **Content-Based Filtering**.

The following book features are combined:

- Author
- Genre
- Keywords
- Description

### TF-IDF Vectorization

TF-IDF (Term Frequency–Inverse Document Frequency) converts the text information into numerical vectors.

It helps identify important words in the book information.

### Cosine Similarity

Cosine similarity is used to calculate how similar two books are based on their feature vectors.

Books with higher similarity scores are considered more similar.

## 🔄 How the System Works

1. The `books.csv` dataset is loaded using Pandas.
2. Book features such as author, genre, keywords, and description are combined.
3. The combined text is converted into numerical vectors using TF-IDF.
4. Cosine similarity is calculated between all books.
5. The user enters a book title.
6. The system searches for the selected book.
7. Similarity scores are sorted from highest to lowest.
8. The five most similar books are displayed.

## 🎨 User Interface

The application uses **Gradio** to provide a simple web-based interface.

The user enters the name of a book, and the system displays five recommended books with their authors and similarity scores.

## 📁 Project Structure

```text
Task3/
│
├── task3.py
├── books.csv
├── requirements.txt
└── README.md
