# Agent Architecture & Orchestration Platform


┌────────────────────────────────────────────┐
│ Block 4 — Product Console                  │
│ Evidence UI, trace viewer, approvals        │
└────────────────────────────────────────────┘
                    ↓
┌────────────────────────────────────────────┐
│ Block 3 — Agent Architecture               │
│ state machine, policy, isolation, evals     │
└────────────────────────────────────────────┘
                    ↓
┌────────────────────────────────────────────┐
│ Block 2 — RAG + MCP Context Layer          │
│ retrieval, citations, tools, memory         │
└────────────────────────────────────────────┘
                    ↓
┌────────────────────────────────────────────┐
│ Block 1 — Inference Runtime                │
│ SGLang, vLLM, structured outputs            │
└────────────────────────────────────────────┘
                    ↓
┌────────────────────────────────────────────┐
│ Block 5 — Cloud Platform                   │
│ Kubernetes, GPU, tracing, metrics           │
└────────────────────────────────────────────┘
