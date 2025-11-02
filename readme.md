# Agentic AI Examples

Welcome to the **Agentic AI Examples** repository!  
This project demonstrates practical implementations and concepts of Agentic AI, providing a hands-on guide to building intelligent systems with modular, agent-based architectures.

---

## What is Agentic AI?

**Agentic AI** refers to artificial intelligence systems that operate as autonomous agents, capable of perceiving their environment, reasoning about tasks, making decisions, and taking actions to achieve specific goals. Unlike traditional, monolithic AI models, agentic systems are composed of interacting components—agents, tools, planners, executors, and more—each playing a distinct role.

Agentic AI is inspired by cognitive science and robotics, where autonomous agents exhibit behaviors such as planning, adaptation, and tool usage. These systems are designed for flexibility, modularity, and the ability to handle complex, multi-step tasks.

---

## Core Components

Below are the key building blocks commonly found in Agentic AI systems:

### 1. Agent

- **Description:** The agent is the central entity responsible for orchestrating actions towards the achievement of goals. It perceives inputs, maintains context, chooses tools, invokes planners, and manages execution.
- **Role:** Decision-maker and coordinator.

### 2. Tools

- **Description:** Tools are modular functions or APIs that the agent can use to perform specific operations (e.g., data retrieval, computation, communication).
- **Role:** Extend the agent’s capabilities, allowing it to interact with the external world or process information.

### 3. Planner

- **Description:** The planner is responsible for breaking down high-level goals into actionable steps. It creates plans or strategies based on the agent’s objectives and available tools.
- **Role:** Task decomposition and strategy formulation.

### 4. Executor

- **Description:** The executor carries out the steps outlined by the planner. It ensures actions are performed in the correct order, monitors progress, and handles failures or retries if necessary.
- **Role:** Plan execution and monitoring.

### 5. Memory (Optional)

- **Description:** Some agentic systems include a memory component to store past interactions, results, or world states. This enables learning, context retention, and more intelligent behaviors over time.
- **Role:** Context management and learning.

---

## Example Workflow

1. **Agent** receives a complex task or query.
2. **Planner** decomposes the task into steps.
3. **Agent** selects appropriate **tools** for each step.
4. **Executor** carries out the steps using the selected tools.
5. **Memory** (if present) retains context or results for future use.

---

## Component Example: `/crewai/crewai_helloworld.py`

This file demonstrates a simple, practical implementation of an agentic workflow using the [CrewAI](https://github.com/joaomdmoura/crewAI) framework.

**What it does:**
- Defines three agents: a researcher, a writer, and a planner/reviewer.
- The **researcher** agent gathers key data about electric vehicle (EV) adoption in India.
- The **writer** agent receives the research and writes a concise, readable report summarizing the findings.
- The **planner** agent coordinates the process, plans subtasks, reviews outputs, and retries if needed.
- The workflow is organized as a "crew" where agents collaborate sequentially: the planner assigns tasks, the researcher collects facts, and the writer produces a report.
- The script demonstrates task decomposition, role assignment, and team orchestration in an agentic AI system.

> **File:** [`/crewai/crewai_helloworld.py`](https://github.com/HimanshubhusanRath/agentic_ai_examples/blob/main/crewai/crewai_helloworld.py)  
> **Purpose:** Orchestrates a multi-agent workflow for researching and reporting on EV adoption in India, showcasing agent roles, planning, and sequential execution.

---

## Contributing

Contributions, issues, and feature requests are welcome!
Feel free to fork the repository and submit pull requests to help improve the examples or add new agentic AI modules.

---

## License

This repository is open source and available under the [MIT License](LICENSE).

---
