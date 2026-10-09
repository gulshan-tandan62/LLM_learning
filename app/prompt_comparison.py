
from langchain_core.prompts import ChatPromptTemplate


# Common inputs for both approaches
role = "Python Teacher"
level = "beginner"
question = "What is a Python decorator?"


# Method 1: Manual Python formatting
system_template = """You are a {role}.
Explain concepts at a {level} level.
Use practical examples."""

manual_system = system_template.format(
    role=role,
    level=level
)

manual_user = question


# Method 2: LangChain formatting
langchain_template = ChatPromptTemplate.from_messages([
    ("system", system_template),
    ("human", "{question}")
])

messages = langchain_template.format_messages(
    role=role,
    level=level,
    question=question
)

langchain_system = messages[0].content
langchain_user = messages[1].content


# Compare results
print("----- MANUAL PYTHON -----")
print("System:", manual_system)
print("User:", manual_user)

print("\n----- LANGCHAIN -----")
print("System:", langchain_system)
print("User:", langchain_user)

print("\n----- COMPARISON -----")
print("System instructions match:", manual_system == langchain_system)
print("User messages match:", manual_user == langchain_user)

print("LangChain variables:", langchain_template.input_variables)
