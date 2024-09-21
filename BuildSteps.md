1. Go to https://github.com/pinecone-io/canopy and clone the repo
2. Create the docker image
         docker build -t canopy:1 .
3. These env variables needs to set
   # Create a pinecone account  and generate api key
    PINECONE_API_KEY=
   # Get an OPEN AI API KEY
   OPENAI_API_KEY=
   # Create an INDEX in pinecone starting canopy--<ame>
   INDEX_NAME=

4. Run the scrape.py from main branch
     python3 scrape.py
   
6. Clone git@github.com:msathe-tech/gen-rag-gke.git branch chatbot-ui
7. Create the docker image 
    docker build -t chatbotui:1 .
8. These env variables needs to set
     export CUSTOM_API_URL=http://localhost:8000/v1/<namespace>/chat/completions
