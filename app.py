import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import gradio as gr


# -----------------------------------
# 1. Load the book dataset
# -----------------------------------

books = pd.read_csv("books.csv")


# -----------------------------------
# 2. Combine book features
# -----------------------------------

books["features"] = (
    books["author"] + " "
    + books["genre"] + " "
    + books["keywords"] + " "
    + books["description"]
)


# -----------------------------------
# 3. Convert text into numerical data
# -----------------------------------

vectorizer = TfidfVectorizer(
    stop_words="english"
)

feature_matrix = vectorizer.fit_transform(
    books["features"]
)


# -----------------------------------
# 4. Calculate similarity
# -----------------------------------

similarity_matrix = cosine_similarity(
    feature_matrix
)


# -----------------------------------
# 5. Recommendation function
# -----------------------------------

def recommend_books(book_name):

    book_name = book_name.strip().lower()

    # Find the selected book
    matches = books[
        books["title"].str.lower() == book_name
    ]

    if matches.empty:
        return (
            "Book not found.\n\n"
            "Please enter a book from the available list."
        )

    # Get the index of selected book
    book_index = matches.index[0]

    # Get similarity scores
    similarity_scores = list(
        enumerate(
            similarity_matrix[book_index]
        )
    )

    # Sort from highest to lowest
    similarity_scores = sorted(
        similarity_scores,
        key=lambda x: x[1],
        reverse=True
    )

    # Generate recommendations
    recommendations = []

    for index, score in similarity_scores[1:6]:

        title = books.iloc[index]["title"]
        author = books.iloc[index]["author"]

        recommendations.append(
            f"📚 {title} — {author}\n"
            f"   Similarity Score: {score:.2f}"
        )

    return "\n\n".join(recommendations)


# -----------------------------------
# 6. Create Gradio interface
# -----------------------------------

interface = gr.Interface(
    fn=recommend_books,

    inputs=gr.Textbox(
        label="Enter a Book You Like",
        placeholder="Example: The Hobbit"
    ),

    outputs=gr.Textbox(
        label="Recommended Books"
    ),

    title="📚 AI Book Recommendation System",

    description=(
        "Enter the name of a book and the system "
        "will recommend five similar books using "
        "content-based filtering."
    )
)


# -----------------------------------
# 7. Start application
# -----------------------------------

if __name__ == "__main__":
    interface.launch()