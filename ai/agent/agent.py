import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory
from .tools.controls import get_controls
from .tools.evidences import get_evidences
from .tools.policies import get_policies
from .tools.users import get_users

load_dotenv() 

groq_api_key = os.getenv("GROQ_API_KEY")

llm = ChatGroq(
    api_key=groq_api_key,
    model="llama-3.1-8b-instant",
    temperature=0
)

tools = [get_controls, get_policies, get_evidences, get_users]

def get_prompt():
    return ChatPromptTemplate.from_messages([
        ("system", "You are a helpful GRC analyst assistant. Use the available tools to answer questions."),
        MessagesPlaceholder(variable_name="chat_history"),
        ("human", "{input}"),
        MessagesPlaceholder(variable_name="agent_scratchpad")
    ])

agent = create_tool_calling_agent(llm=llm, tools=tools, prompt=get_prompt())

executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    max_iterations=5,
    handle_parsing_errors=True
)

session_store = {}

def get_session_history(session_id: str) -> ChatMessageHistory:
    if session_id not in session_store:
        session_store[session_id] = ChatMessageHistory()
    return session_store[session_id]

agent_with_history = RunnableWithMessageHistory(
    executor,
    get_session_history,
    input_messages_key="input",
    history_messages_key="chat_history"
)

def run_agent(user_message: str, session_id: str = "default") -> str:
    try:
        response = agent_with_history.invoke(
            {"input": user_message},
            config={"configurable": {"session_id": session_id}}
        )
        return response["output"]
    except Exception as e:
        import traceback
        traceback.print_exc()
        return f"Error: {str(e)}"