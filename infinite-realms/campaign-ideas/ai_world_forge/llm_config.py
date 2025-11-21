import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_litellm import ChatLiteLLM

def get_gemini_llm():
    """
    Returns a configured ChatGoogleGenerativeAI instance.
    """
    return ChatGoogleGenerativeAI(
        model="gemini-pro",
        verbose=True,
        temperature=0.7,
        google_api_key=os.getenv("GEMINI_API_KEY")
    )

def get_openrouter_llm(model_name: str):
    """
    Returns a configured ChatLiteLLM instance for OpenRouter with a specific model.
    """
    # Ensure the model name is prefixed with 'openrouter/' as required by ChatLiteLLM for OpenRouter models
    if not model_name.startswith("openrouter/"):
        model_name = f"openrouter/{model_name}"

    return ChatLiteLLM(
        model=model_name,
        api_key=os.getenv("OPENROUTER_API_KEY"),
        # base_url is not needed here as ChatLiteLLM handles it internally for 'openrouter/' prefixed models
        verbose=True,
        temperature=0.7,
    )