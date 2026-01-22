# 🏥 CareTrail  
**A Multi-Agent Healthcare Memory & Retrieval System using Qdrant**

---

## Overview

CareTrail is a multi-agent AI system that addresses the problem of fragmented healthcare information. Patients often lose medical context across time as reports, symptoms, and advice are scattered across visits. Existing AI assistants lack long-term memory, resulting in repeated questions and inconsistent support.

CareTrail solves this by combining **Qdrant as a persistent vector memory** with **LLaMA-3.1 (via Groq Cloud)** for **evidence-based reasoning**, enabling continuity of care across interactions.

> ⚠️ This system is for informational support only and does **not** provide medical diagnosis or treatment.

---

## Problem Statement

Healthcare data such as lab reports, symptoms, and prior advice is often fragmented across time and systems. This leads to:
- Loss of historical context  
- Repeated medical tests  
- Inconsistent guidance  

Stateless AI chatbots fail to maintain continuity, limiting their usefulness in real-world healthcare scenarios.

---

## Proposed Solution

CareTrail introduces a **multi-agent architecture with shared long-term memory**, where:
- Medical information is stored as vector embeddings in Qdrant
- Relevant context is retrieved using semantic search
- Responses are generated strictly from retrieved evidence

This ensures **traceable, grounded, and non-hallucinated outputs**.

---

## Multi-Agent Architecture

CareTrail consists of three specialized agents:

### 1. Ingestion Agent
- Accepts medical notes, reports, and symptom logs
- Chunks text and generates embeddings
- Stores vectors and metadata in Qdrant

### 2. Memory (Retrieval) Agent
- Performs semantic similarity search using Qdrant
- Retrieves the most relevant historical records
- Acts as the system’s long-term memory controller

### 3. Reasoning Agent
- Uses LLaMA-3.1 via Groq Cloud
- Generates responses only from retrieved memory
- Explains which information was used

Qdrant serves as the **shared memory layer** across all agents.

---

## Role of Qdrant

Qdrant is the core component of CareTrail:
- Stores long-term healthcare memory as vector embeddings
- Enables semantic search across past records
- Allows memory reuse across sessions
- Prevents hallucination via retrieval-first reasoning

The system cannot function without Qdrant.

---

## Tech Stack

- Vector Database: Qdrant  
- LLM: LLaMA-3.1 (Groq Cloud)  
- Embeddings: Sentence Transformers (MiniLM)  
- Backend: Python  
- Interface: Command Line (CLI)  
- Deployment: Local (Docker)

---

## Project Structure

caretrail-qdrant/
├── main.py
├── README.md
├── requirements.txt
├── .env
├── agents/
│   ├── ingestion_agent.py
│   ├── memory_agent.py
│   └── reasoning_agent.py
├── qdrant/
│   ├── client.py
│   └── schema.py
├── embeddings/
│   └── embedder.py
└── utils/
    └── chunker.py

---

## Example Interaction

### Stored information
- Blood report shows hemoglobin level of 9.5 g/dL.
- Patient reports fatigue and dizziness.

### User query
Why do I feel tired?

### System response
Based on the retrieved blood report indicating low hemoglobin  
and the recorded symptoms of fatigue and dizziness,  
these symptoms may be related.

---

## How to Run

1. **Start Qdrant**

   Run the following command:

   ```bash
   docker run -p 6333:6333 qdrant/qdrant
   ```

2. **Install Dependencies**

   Install required packages using:

   ```bash
   pip install -r requirements.txt
   ```

3. **Configure Environment Variables**

   Create a `.env` file and add the following values:

   ```env
   GROQ_API_KEY=your_api_key_here
   QDRANT_URL=http://localhost:6333
   ```

4. **Run the Application**

   Start the application using:

   ```bash
   python main.py
   ```

---

## Ethics & Safety

- No diagnosis or treatment suggestions  
- Informational assistance only  
- Responses grounded strictly in stored memory  
- Acknowledged limitations for incomplete data  
- Privacy considerations noted for real deployments  

---

## Evaluation Alignment

CareTrail aligns with the Qdrant hackathon criteria:

- Meaningful vector search usage  
- Persistent long-term memory  
- Evidence-based reasoning  
- Societal relevance (healthcare continuity)  
- Clear and modular system design  

---

## Conclusion

CareTrail demonstrates how multi-agent AI systems with vector memory can solve real-world societal challenges. By combining Qdrant’s retrieval capabilities with LLaMA-based reasoning, the system delivers transparent, grounded, and reliable healthcare support over time.
