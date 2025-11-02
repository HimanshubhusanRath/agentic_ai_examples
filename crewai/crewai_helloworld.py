import os
from typing import List, Optional
from crewai import Agent, Task, Crew, Process
from dotenv import load_dotenv
from pathlib import Path

parent_dir = Path(__file__).parent.parent
ENV_FILE_PATH = os.path.join(parent_dir, '.env')

# load properties
load_dotenv(ENV_FILE_PATH)

#
# 1. Define Worker Agents
#
researcher = Agent(
    role="EV Researcher",
    goal ="Gather latest data and status about EV adoption in India",
    backstory = "You are a seasoned researcher specialising in Indian EV market trends.",
    verbose=True
)

writer = Agent(
    role = "Report Writer",
    goal = "Write a conside report summarising EV adoption in India",
    backstory = "You are a technical writer with experience in summarising market trends into readable reports.",
    verbose = True
)

#
# 2. Define a planner / coordinator agent
#   
planner = Agent(
    role = "Planner and reviewer",
    goal = "Plan subtasks for the crew, review results & retry if needed",
    backstory = "You design the workflow, assign tasks to the researcher and writer, and review their work for quality",
    tools=[],  # planner may use no external tools or optionally tools
    verbose = True
)


# 
# 3. Methods for defining tasks, review mechanism and retries
#  
def make_tasks(topic:str) -> List[Task]:
    tasks : List[Task] = []
    # Task for researcher
    tasks.append(
        Task(
            description = f"Collect a list of 5-10 key facts about the {topic} in India",
            agent = researcher,
            expected_output = "A bulleted list of key facts and trends"
        )
    )

    # Task for writer
    tasks.append(
        Task(
            description = f"Write a concise report on the {topic} based on the researcher's output",
            agent = writer,
            expected_output = "A readable report (150-200 words) summarising the facts and insights"
        )
    )
    return tasks



# 
# Main method
# 
def main():
    topic = "EV adoption in India"
    tasks = make_tasks(topic)

    print(f"Tasks are : {tasks}")


    crew = Crew(
        agents = [planner, researcher, writer],
        tasks = tasks,
        process = Process.sequential,
        verbose = True
    )

    result = crew.kickoff()
    print(result)

if __name__ == "__main__":
    main()





