# Overview 

Organizations can drive differentiating value by powering their business critical application using LLMs, RAG and CI/CD across all the stages of RAG.
We will focus on cloud portable RAG application that can scale well with managed Kuberenetes service.
We will use PostgreSQL as a OSS Vector DB and deploy it on GKE for scalability. 
We will use Gemini's embedings API to build vector embedings and then store in the PostgreSQL. 
Follow the docs here - https://cloud.google.com/kubernetes-engine/docs/tutorials/deploy-pgvector. 
The PostgreSQL offers compatibility with managed services on GCP. 
We will use the Langchain deployed on GKE with  to build a solution to chunk the PDFs and extract text. 

We will build a DevOps pipeline to deploy the code and build the GKE based platform using Terraform. 



