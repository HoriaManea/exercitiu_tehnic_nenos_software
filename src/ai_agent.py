from langchain_ollama import OllamaLLM
import json

llm = OllamaLLM(
    model="mistral:latest",
    temperature=0
)

def ai_agent_batch(paragraphs: list[str], json_keys: list[str]) -> dict:
    prompt = f"""
You are a strict JSON generator.

Your task:
Match each paragraph with the MOST relevant key from the provided list.

Rules:
- You MUST return ONLY valid JSON.
- Do NOT explain anything.
- Do NOT write text before or after JSON.
- If no match exists, return "NONE".

Paragraphs:
{json.dumps(paragraphs, ensure_ascii=False)}

Available keys:
{json.dumps(json_keys, ensure_ascii=False)}

Return JSON in this exact format:
{{
  "0": "key_name_or_NONE",
  "1": "key_name_or_NONE"
}}
"""

   