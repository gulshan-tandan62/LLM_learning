from langchain_core.prompts import ChatPromptTemplate

prompt_template = ChatPromptTemplate.from_messages([
    ("system", "You are a {role}. Explain concepts at a {level} level."),
    ("human", "{question}")
])
messages = prompt_template.format_messages(
    role="Python Teacher",
    level="beginner",
    question="What is an API?"
)
for message in messages:
    print(f"Role: {message.type}")
    print(f"Content: {message.content}")
    print()
