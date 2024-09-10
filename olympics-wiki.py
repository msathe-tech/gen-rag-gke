import wikipedia
from google.cloud import storage

# 1. Install Necessary Libraries (if you haven't already)
# pip install wikipedia google-cloud-storage

# 2. Set up Google Cloud Storage Authentication
storage_client = storage.Client.from_service_account_json('path/to/your/service_account_key.json')
bucket_name = 'your-bucket-name'
bucket = storage_client.bucket(bucket_name)

# 3. Search Wikipedia
search_results = wikipedia.search("Paris 2024 Olympics")

for result in search_results:
    try:
        # 4. Fetch Article Content
        page = wikipedia.page(result)
        article_content = page.content

        # 5. Store in Google Cloud Storage
        blob_name = f"paris_olympics_{result.replace(' ', '_')}.txt"
        blob = bucket.blob(blob_name)
        blob.upload_from_string(article_content)

        print(f"Stored article '{result}' in Google Cloud Storage.")

    except wikipedia.exceptions.DisambiguationError as e:
        print(f"DisambiguationError for '{result}': {e.options}")
    except wikipedia.exceptions.PageError:
        print(f"Page not found for '{result}'.")
