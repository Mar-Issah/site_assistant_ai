from langchain_core.prompts import ChatPromptTemplate

template = """
Based on the table schema below, write a SQL query that would answer the users's question: {schema}

Question: {question}
SQL Query
"""
prompt = ChatPromptTemplate.from_template(template)
print(prompt.format(schema="users", question="What is the name of the user with the id 1?"))