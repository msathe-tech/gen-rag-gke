import requests
from bs4 import BeautifulSoup

# Constants for Canopy API
CANOPY_API_URL = 'http://localhost:8000/v1/{namespace}/context/upsert'  # Use the upsert endpoint
NAMESPACE = 'test-1'  # Namespace to upload the data to

def scrape_wikipedia(url):
    """
    Scrapes the main content of a Wikipedia page and returns the text.
    """
    response = requests.get(url)
    if response.status_code != 200:
        print("Failed to retrieve the webpage")
        return None

    # Parse the HTML content
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the main content of the Wikipedia page
    content = soup.find('div', {'id': 'bodyContent'})
    paragraphs = content.find_all('p')

    # Combine all paragraph texts into one string
    scraped_text = "\n".join([para.get_text() for para in paragraphs])
    return scraped_text

def chunk_text(text, chunk_size=512):
    """
    Splits the text into chunks of a specified size (default 512 words).
    """
    words = text.split()
    for i in range(0, len(words), chunk_size):
        yield " ".join(words[i:i + chunk_size])

def upsert_to_canopy(text_chunks, source_url, namespace):
    """
    Upserts the text chunks to Canopy API within a specific namespace.
    """
    headers = {
        'Content-Type': 'application/json'
    }

    # Prepare the data for the upsert request
    documents = []
    for chunk in text_chunks:
        document = {
            'id': f"wiki_chunk_{hash(chunk)}",  # Generate a unique ID for the chunk
            'text': chunk,
            'source': source_url,  # Move the source to the top-level
            'metadata': {
                'source_url': source_url  # Keep only custom metadata here
            }
        }
        documents.append(document)
    
    # Upsert request payload
    data = {
        'documents': documents,
        'batch_size': 200  # Optional: Specify the batch size if needed
    }

    # Perform the upsert request
    response = requests.post(CANOPY_API_URL.format(namespace=namespace), headers=headers, json=data)
    if response.status_code == 200:
        print("Upsert successful")
    else:
        print(f"Failed to upsert: {response.status_code}, {response.text}")

def main():
    # Example Wikipedia URL
    url = 'https://en.wikipedia.org/wiki/2024_Summer_Olympics'  # Replace with your desired URL

    # Step 1: Scrape the Wikipedia page
    print("Scraping Wikipedia page...")
    page_content = scrape_wikipedia(url)

    if not page_content:
        print("Failed to scrape the content. Exiting.")
        return

    # Step 2: Split the content into chunks
    print("Splitting content into chunks...")
    text_chunks = list(chunk_text(page_content, chunk_size=512))

    # Step 3: Upsert the chunks to Canopy, specifying the namespace
    print(f"Upserting content to Canopy in namespace '{NAMESPACE}'...")
    upsert_to_canopy(text_chunks, url, NAMESPACE)
    print(page_content)
    print("All done!")

if __name__ == "__main__":
    main()
