# LangGraph Research and Summarization Agent

## Architecture
This system uses a LangGraph-based workflow with four agents:
1. **Router Agent** – Determines query type.
2. **Web Research Agent** – Uses SerpAPI for real-time search.
3. **RAG Agent** – Retrieves from a local dataset via FAISS.
4. **Summarization Agent** – Synthesizes a coherent answer.

## Flow
1. Query enters through the router.
2. It’s routed to Web or RAG agent.
3. The result is summarized via OpenAI LLM.

## Example Queries
- "What is the latest AI news?" → Web Agent
- "Explain LangChain agents." → RAG Agent

## Setup
- Set environment variables: `GOOGLE_API_KEY`, `SERPAPI_API_KEY`
- Prebuild `faiss_index.pkl` using SentenceTransformer.
"""