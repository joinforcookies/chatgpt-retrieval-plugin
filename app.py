from langchain.document_loaders import PyPDFLoader
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from langchain.indexes import VectorstoreIndexCreator
import os
import getpass
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from typing import List
from langchain.docstore.document import Document
import json
from langchain.retrievers import ChatGPTPluginRetriever



os.environ["OPENAI_API_KEY"] = "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"


loader = PyPDFLoader("snacks.pdf")
pages = loader.load_and_split()


# faiss_index = FAISS.from_documents(pages, OpenAIEmbeddings())
# docs = faiss_index.similarity_search("How will the community be engaged?", k=2)
# for doc in docs:
#     print(str(doc.metadata["page"]) + ":", doc.page_content[:300])

# def write_json(path: str, documents: List[Document])-> None:
#     results = [{"text": doc.page_content} for doc in documents]
#     with open(path, "w") as f:
#         json.dump(results, f, indent=2)

# write_json("foo.json", pages)

retriever = ChatGPTPluginRetriever(url="https://oyster-app-hi9pi.ondigitalocean.app/", bearer_token="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIyMzg0IiwibmFtZSI6Ik5hc2ltIE9iZWlkIiwiaWF0IjoxNTE2MjM5MDIyfQ.YLbm1sP_xpPNDA9XGw4HDYd8UzwWeWJPWvkdFqcYbMg")
retriever.get_relevant_documents("Name of the author")