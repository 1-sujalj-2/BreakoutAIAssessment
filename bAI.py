import streamlit as st
import pandas as pd
import requests
from bs4 import BeautifulSoup
from transformers import pipeline

# Initialize local model pipeline
st.sidebar.title("Configuration")
use_model = st.sidebar.checkbox("Load Local Language Model", value=True)
model = pipeline("text-generation", model="gpt2") if use_model else None

# Title
st.title("AI Agent: Web Scraping and Local Processing")

# Step 1: File Upload
st.header("Upload Data")
uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])
if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)
        st.write("Preview of Uploaded Data:")
        st.write(df.head())

        # Step 2: Select Column
        column = st.selectbox("Select a column for entities:", df.columns)
        entities = df[column].dropna().tolist()
    except Exception as e:
        st.error(f"Error loading CSV file: {e}")

# Step 3: Define Query Template
if uploaded_file:
    st.header("Define Query Template")
    query_template = st.text_input("Enter query template (e.g., 'Get contact for {company}')")
    if query_template:
        queries = [query_template.format(company=entity) for entity in entities]
        st.write("Generated Queries:")
        st.write(queries)

# Step 4: Perform Web Search
st.header("Web Search")
if uploaded_file and st.button("Search the Web"):
    results = []
    for query in queries:
        try:
            # Perform Google search using BeautifulSoup
            url = f"https://www.google.com/search?q={query.replace(' ', '+')}"
            headers = {"User-Agent": "Mozilla/5.0"}
            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                soup = BeautifulSoup(response.content, "html.parser")
                snippets = [result.text for result in soup.find_all("h3")]
                results.append({"query": query, "snippets": snippets})
            else:
                st.warning(f"Failed to retrieve results for '{query}' with status code {response.status_code}")
        except Exception as e:
            st.error(f"Error processing query '{query}': {e}")

    if results:
        st.success("Search completed successfully!")
        st.write("Search Results:")
        for result in results:
            st.write(f"Query: {result['query']}")
            st.write(f"Snippets: {result['snippets']}")
    else:
        st.error("No search results retrieved. Check your queries or network connection.")

# Step 5: Process Results Locally
st.header("Process Results Locally")
if uploaded_file and st.button("Process Results"):
    if not model:
        st.error("Local language model is not loaded.")
    else:
        processed_data = []
        for result in results:
            try:
                # Use local model to process snippets
                context = "\n".join(result["snippets"])
                prompt = f"Extract relevant information from the following text:\n{context}"
                response = model(prompt, max_length=150, num_return_sequences=1)
                extracted_info = response[0]["generated_text"]
                processed_data.append({"Query": result["query"], "Extracted Info": extracted_info})
            except Exception as e:
                st.error(f"Error processing query '{result['query']}': {e}")

        if processed_data:
            st.success("Data processed successfully!")
            st.write("Processed Data:")
            st.write(pd.DataFrame(processed_data))
        else:
            st.error("No data processed. Ensure valid input and try again.")

# Step 6: Export Results
if uploaded_file and st.button("Download Processed Data"):
    if 'processed_data' in locals() and processed_data:
        csv = pd.DataFrame(processed_data).to_csv(index=False)
        st.download_button(
            label="Download CSV",
            data=csv,
            file_name="processed_data.csv",
            mime="text/csv"
        )
    else:
        st.warning("No processed data to download.")
