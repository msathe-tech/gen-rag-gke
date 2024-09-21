## Steps

### 1. Clone the Canopy Repository
First, clone the Canopy repository from GitHub:

```bash
git clone https://github.com/pinecone-io/canopy
cd canopy
```

### 2. Build the Canopy Docker Image

Create the Docker image for Canopy by running the following command:

```bash
docker build -t canopy:1 .
```

### 3. Set Required Environment Variables

You will need to set the following environment variables:

- **PINECONE_API_KEY**: Create a Pinecone account [here](https://www.pinecone.io) and generate your API key.
- **OPENAI_API_KEY**: Get your OpenAI API key [here](https://beta.openai.com/signup/).
- **INDEX_NAME**: Create an index in Pinecone. The index name should follow this format: `canopy--<name>`.

```bash
export PINECONE_API_KEY=<your_pinecone_api_key>
export OPENAI_API_KEY=<your_openai_api_key>
export INDEX_NAME=canopy--<name>
```

### 4. Run the Scrape Script

To scrape data, run the `scrape.py` script from the main branch:

```bash
python3 scrape.py
```

### 5. Clone the Chatbot UI Repository

Next, clone the repository for the chatbot UI:

```bash
git clone git@github.com:msathe-tech/gen-rag-gke.git
cd gen-rag-gke
git checkout chatbot-ui
```

### 6. Build the Chatbot UI Docker Image

Create the Docker image for the chatbot UI:

```bash
docker build -t chatbotui:1 .
```

### 7. Set Additional Environment Variables

Set the following environment variable for the chatbot UI:

```bash
export CUSTOM_API_URL=http://localhost:8000/v1/<namespace>/chat/completions
```

Replace `<namespace>` with the appropriate value for your setup.

---

