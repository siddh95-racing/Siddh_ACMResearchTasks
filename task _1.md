# **SUMMARY OF PROMPT ENGINEERING VLOG BY GAURI SHIRKE**



Prompt engineering is presenting your ideas in most appropriate manner so that they are easily understandable to AI. A good prompt is breakable into clear ideas and elements and hence conveying the message in the best possible way. A good prompt can make results of the same task better than just a normal prompt and could also get more personalized results rather than generic answers.

With AI, every part of your prompt helps guide your agent, so it understands not just what you want, but how to deliver a response that’s genuinely helpful and relevant to your assignment.

The process is outlined as follows:

Role- You need to mention AI the perspective of the person who is specialized to perform that task.

Task- you need to tell AI agent the workflow and sturdy framework to do the task, this will reduce the chances of it getting side-tracked and will act more focused.

Instructions- these provide detailed information about the constrains and requirements of the task.

Context- Means providing accurate background to the agent.

Input- raw data provided for the task.

Langchain is framework for building own AI prompts with reusable templates.

## ***TYPES OF PROMPTING TECHNIQUES***

* **Zero-shot**: its asking the AI agents for response without giving it any hints or data examples. useful for quick responses and accurate for generic questions. For eg:-"Roadmap to become a quant-engineer."
* **One-shot:** its asking the AI agents for response with one exapmle or detailed description of an example. Helps model to respond in desiredstyle and format. For eg:-" Roadmap to become a quant-engineer with daily targets to fulfill, best free resources to be referred and useful projects to be made during journey."
* **Few-shot**: its asking the AI agent for a response by giving it multiple examples, so that the AI can understand the pattern, logic, style or format for the final answer. It is useful when we want more consistent and customized responses, especially when the required output follows a specific pattern. For eg:- "Example 1: Create a roadmap to become a Data Scientist with sections for Mathematics, Programming, Statistics, Machine Learning and Projects. Example 2: Create a roadmap to become a Software Engineer with sections for Programming, Data Structures, Algorithms, System Design and Projects. Now create a roadmap to become a Quant Engineer using a similar structure."

## **Prompting Technique Selection Process**



• **Defining Task** - Identify what do we want from task - is it high accuracy, faster response or balance of both.



• **Checking Task Definition** - Determine whether task clearly fulfills what we want.



• **Zero-shot Prompting** - Attempt to perform the task without examples.



• **Evaluate Zero-shot** - check whether the response from zero-shot fulfills the task in desired way.



• **One-shot prompting** - If need a more accurate response then we should



* **Evaluate One Shot** - checking whether the response is upto the mark.



* **Few-shot prompting** - If we need more accurate response from it, we need to provide few more examples.



* **Evaluate Few-shot prompt** - Assess the performance of few shot prompting.



* **Refining Examples/shot** = For customized responses, we can just make few adjustments in examples given in prompt.



* **End Process** - conclude the process.

## 

## **Chain Of Thought prompting**



This method prompting is used when we need step-by-step visualization of problem. This feels like how AI than agent thinks to get us the answer and we could also control it.

##### **process of chain prompting**

* **direct prompting-** to check whether we get desired result via just simple prompt.
* **designing chain of thought prompting-**so to get desired results we will use few-shot examples or a detailed zero-shot prompt.
* **evaluating the prompt-**we check whether all the logical workflows required for AI agent to reach desired outcome are explained clearly and written carefully.
* **evaluating answers-** WE CHECK HOW EFFECIENTLY DOES OUR RESPONSE COMPLETES THE TASK.

Prompt Example:Prompt Example:

“It’s the last week of the semester, you have three assignments due, and you’re feeling overwhelmed. Suggest an action plan that helps manage the workload and reduces stress.”

“Walk me through, step by step, how you would approach and complete a challenging university assignment from start to finish.”

the prompt in this case takes the task to get completed but it cannot think blindly and its logical decision has be in accordance mentioned by the user and hence defining the logical workflow for the task.

## **Role-Based Prompting**

this is the type of prompting in which we want the specific task to be performed by expert of the field.By this you can assign AI agent the persona of the person who would be really most useful for you in the task completion with real-world exxperiences and solutions.

#### **Process of role-based prompting:**

* **Defining the task-**Establish the objective for interaction.
* **Identifying the desired persona-** finding the best type of persona that could provide most efficient solution.
* **Craft the prompt-**create a prompt that includes that persona and his role.
* **AI RESPONSE-**AI will respond according to the persona of that was mentioned in the prompt.
* **Evaluate the response quality-**check the accuracy of desired output and whether does it really fulfill the required task .
* **Refine the prompt-**to get the desired output change the persona and find the best persona that can fulfill the task.

eg:- “You are a senior student who always finishes assignments early. Share your strategy for staying on top of deadlines and producing high-quality work.”

### **Contextual Prompting**

In this prompting technique we provide the background of the task along with it and response is generated keeping in mind the background we provided.It will also understand subtle clues and emotional tone(if mentioned).

#### **Process of Contextual prompting:**

* **User Input-** we first provide the generic prompt.
* **Background-**to adjust the tone and get output connected to the context we then provide it with background of the task.
* **Response-**we then check whether the response fulfills the needs with accuracy.
* **Refinement-**we then refine our prompt by giving it more background and information to get desired prompt.

Prompt Example:

“It’s the last week of the semester, you have three assignments due, and you’re feeling overwhelmed. Suggest an action plan that helps manage the workload and reduces stress.”

### **Retrieval-Augmented Prompting**

Retrieval-Augmented Prompting allows the AI to use information from external sources such as research papers, textbooks or databases instead of depending only on the information it already knows. This helps make the response more accurate, better and up-to-date.

#### **Process of Retrieval-Augmented prompting:**

* **User input**-defining the objective for interaction.**Prompt Example:**
* **Database Search-** finding the best type data that could provide most efficient solution.
* **Relevant Document Retrieval-**to generate a better response the agent will also refer to the data outside its database from  its retrieval document.
* **Contextualization-**AI will search outside the database in accordance with the prompt.
* **Augmented Prompt creation-**agent will generate the best response combining the resources of database and its retrieval document .

Prompt Example:

“Based on proven university study tips, list three effective techniques for improving concentration while working on assignments. Include references or short summaries from reliable sources.”

### **Tree Of Thought Prompting**

Tree-of-Thought prompting allows AI to explore multiple possible approaches to a problem instead of following only one line of reasoning. It considers different strategies, compares their advantages and disadvantages, and then selects the most suitable approach.

#### **Process of Tree Of Thought prompting:**

* **Decomposition**-Breaking down main problems into sub--problems.
* **Thought Generation-** finding  multiple solutions for each subproblem.
* **State Evaluation-**to evaluate the potential for each thought.
* **Search Algorithm-to find the most feasible, efficient and accurate solution.**  

Prompt Example:

“Consider different strategies for organizing tasks in a busy week with multiple assignments. For each method — using a planner, digital tools, or prioritizing deadlines — explain the steps, pros and cons, and recommend which strategy is most effective for staying on track.”























