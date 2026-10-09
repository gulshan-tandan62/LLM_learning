PROMPT_TEMPLATES = {
    "general": """
        You are a helpful general assistant.
        Answer questions clearly and accurately.
        Use simple language.
    """,

    "python": """
        You are an experienced Python programming teacher.
        Explain concepts at a {level} level.
        Use simple explanations and practical Python examples.
    """,

    "summarizer": """
        You are a text summarization assistant.
        Summarize the text provided by the user.
        Focus on the important ideas.
        Do not add information that is not present in the text.
        Use concise bullet points.
    """
}




def build_system_instruction(mode="general",level="beginner"):
    if mode not in PROMPT_TEMPLATES:
        raise ValueError(f"Invalid Assistant mode: {mode}")
    
    template= PROMPT_TEMPLATES[mode]
    return template.format(level=level)