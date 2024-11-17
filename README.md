AI Agent for Data Processing and Information Retrieval
Project Summary
This project is a streamlined AI agent that processes datasets and retrieves relevant web-based information for entities listed in a chosen column. Users can:

Upload a CSV or connect to Google Sheets for data input.
Define dynamic search queries with customizable templates.
Retrieve structured information using web scraping or APIs.
Process the retrieved results with an LLM for actionable insights.
Download the results as a CSV.

Features
User-friendly dashboard for file uploads and data previews.
Dynamic query input with placeholders for flexibility.
Web search capabilities using APIs or scraping.
Robust integration with an LLM for parsing results.
Error handling for all critical stages of the pipeline.
Export results in CSV format.

Setup Instructions
1. Prerequisites
Python 3.8+
Access to:
Search API (e.g., SerpAPI) for web searches (optional if using scraping).
LLM API (e.g., OpenAI GPT) for result processing.
Optional: A Google Service Account JSON file for Google Sheets integration.

2. Installation
Clone the repository:
Install dependencies:
Set up environment variables: Create a .env file in the project directory:


Usage Guide
Step 1: Run the Dashboard
Start the Streamlit dashboard:

Step 2: Upload Data
Upload a CSV file or connect a Google Sheet.
Preview and select the column for entity processing.

Step 3: Define Queries
Enter a dynamic query with placeholders, e.g.,:

Step 4: Execute Workflow
Perform web searches using APIs or scraping.
Process results with the integrated LLM.
View and download the extracted information.

Third-Party APIs and Tools
1. APIs
SerpAPI: For structured web searches.
OpenAI GPT: For advanced result parsing.
2. Tools
Streamlit: Dashboard for user interaction.
BeautifulSoup: For web scraping.
Google Sheets API: For real-time Google Sheets integration.

Error Handling
Web Search:
Handles failed API requests, rate limits, and timeouts.
LLM Processing:
Retries failed queries and notifies users of invalid responses.
General:
Displays clear feedback for data upload errors or invalid inputs.

