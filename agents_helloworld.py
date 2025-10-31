from langchain_community.tools import tool, DuckDuckGoSearchResults
from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent, AgentType
import sqlite3
from dotenv import load_dotenv

load_dotenv()

### Define Tools
# Tool-1: Calculator
@tool
def tool_calculator(expression: str) -> str:
    """Evaluates a math expression and return the result"""
    try:
        return str(eval(expression))
    except Exception as ex:
        return f"Error String : {str(ex)}"
    
# Tool-2: Web Search Engine
tool_web_search = DuckDuckGoSearchResults()

## Initialize sqlite db
conn = sqlite3.connect("students.db")
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS marks(name TEXT, score INTEGER)")
cursor.executemany("INSERT INTO marks VALUES (?, ?)", [("Alice", 78), ("Bob", 82), ("Charlie", 91)])
conn.commit()

# Tool-3: Database Query Tool
@tool
def tool_get_avg_marks(query : str) -> str:
    """Fetches the average student marks from the database"""
    conn = sqlite3.connect("students.db")
    cursor = conn.cursor()
    cursor.execute("SELECT AVG(score) FROM marks")
    avg_marks = cursor.fetchone()[0]
    conn.close()
    return f"Average mark : {avg_marks}"


### AGENT SETUP

# Define LLM
llm = ChatOpenAI(model="gpt-4o-mini")
# Register Tools
tools = [tool_calculator, tool_web_search, tool_get_avg_marks] 
# Create Agent
agent = initialize_agent(
    tools = tools,
    llm = llm,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose = True
)


# Query the agent
query = "Find the average marks of students and add a 10% bonus. Then tell me the current year."
response = agent.run(query)
print("\nFinal Response:\n", response)






