# Objectives
## Amol 
1. Demonstrate how app that uses GPU can be deployed on K8s
2. Demonstrate how AI/ML app can be deployed on K8s

## Jiten 
1. Demonstrate how app that uses GPU can be deployed on K8s
2. Demonstrate how AI/ML app can be deployed on K8s
3. How the platform can be deployed on K8s

## Madhav 
1. Showcase open source PaaS for RAG on K8s
  a. Explore Canopy as a RAG platform that helps automate some of the RAG tasks such as chunking, retrieval, etc
  b. Showcase integration with Pinecone vector DB either as a SaaS or GCP marketplace 
2. Demonstrate using accelerators on K8s for embedings
  a. Use accelerator with GKE to demonstrate performance gaps between regular compute and GPU for embedings.
  b. Cost optimization to save money since GPU is an expensive resource
  c. Differentiate between VMs and K8s 
  d. Securely accessing the LLM from the application
3. Demonstrate best practices for enteprise prompt engineering
  a. Showcase building app that is agnostic of LLM so that there is no lock-in
  b. Highlight the challenges for prompt engineering
  c. Demonstrate managing prompts at scale

# Anti-objectives 

# High level use case
Use Olympics 2024 articles and videos for RAG use case, will help demonstarte multi-modal use case. 

# Program plan 
1. Install Canopy on K8s - (Canopy)[https://github.com/pinecone-io/canopy/blob/main/docs/deployment-gcp.md]
2. Integrate Canopy with Pinecone VectorDB service
3. Run the Canopy sample code from [[here](https://github.com/pinecone-io/canopy/blob/main/examples/canopy-lib-quickstart.ipynb)]
4. Data collection for Paris olympics articles from Wikipedia, Youtube

