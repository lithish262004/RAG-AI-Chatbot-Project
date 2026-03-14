import streamlit as st
from groq import Groq
from duckduckgo_search import DDGS
from pypdf import PdfReader
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# ----------------------------
# CONFIG
# ----------------------------

GROQ_API_KEY = "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"

client = Groq(api_key=GROQ_API_KEY)


# ----------------------------
# WEB SEARCH
# ----------------------------

def search_web(query):

    results = []

    with DDGS() as ddgs:
        for r in ddgs.text(query, max_results=3):
            results.append(r["body"])

    return "\n".join(results)


# ----------------------------
# PDF LOADER
# ----------------------------

def load_pdf(file):

    reader = PdfReader(file)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text

    return text


# ----------------------------
# SIMPLE VECTOR STORE
# ----------------------------

class VectorStore:

    def __init__(self):

        self.vectorizer = TfidfVectorizer()
        self.text_chunks = []
        self.vectors = None


    def add_text(self, text):

        chunks = []

        for i in range(0, len(text), 500):
            chunks.append(text[i:i+500])

        self.text_chunks = chunks

        self.vectors = self.vectorizer.fit_transform(chunks)


    def search(self, query):

        if self.vectors is None:
            return ""

        query_vec = self.vectorizer.transform([query])

        similarity = cosine_similarity(query_vec, self.vectors)

        index = similarity.argmax()

        return self.text_chunks[index]


vector_db = VectorStore()


# ----------------------------
# UI
# ----------------------------

st.title("AI Research Assistant")
st.caption("Chatbot with RAG + Web Search")


mode = st.radio(
    "Response Mode",
    ["Concise", "Detailed"]
)


uploaded_file = st.file_uploader(
    "Upload a PDF for RAG",
    type=["pdf"]
)


if uploaded_file:

    text = load_pdf(uploaded_file)

    vector_db.add_text(text)

    st.success("Document processed successfully")


query = st.text_input("Ask a question")


if st.button("Ask"):

    context = ""

    try:
        context = vector_db.search(query)
    except:
        pass


    if context == "":
        context = search_web(query)


    if mode == "Concise":

        prompt = f"""
        Answer briefly.

        Context:
        {context}

        Question:
        {query}
        """

    else:

        prompt = f"""
        Give a detailed explanation.

        Context:
        {context}

        Question:
        {query}
        """


    completion = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )


    answer = completion.choices[0].message.content

    st.write(answer)