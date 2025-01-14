
# Chatbot Application

## Easy Steps to Run the Chatbot

### 1. **Setup the Environment**
   - Install dependencies by running:
     ```bash
     pip install -r requirements.txt
     ```
   - Make sure you have the required environment variables:
     - **GEMINI_API_KEY**: API key for Google Generative AI.
     - Set it in a `.env` file:
       ```plaintext
       GEMINI_API_KEY=your_api_key_here
       ```

### 2. **Run the Application**
   - Start the chatbot by executing the main script:
     ```bash
     python main.py
     ```

---

## How the Budget is Calculated

1. **Data Collection**:
   - The `financial_data_collector` agent collects data about income, expenses, and financial goals from the user.

2. **Calculation Process**:
   - The `budget_calculator` agent uses the collected data to calculate the budget, determining how much can be allocated for savings, investments, and other expenses.

3. **Savings Tips**:
   - The `savings_advisor` agent generates practical tips to improve savings based on the budget calculation and user-specific details.

---

## Tools and Agents

### Tools
- **Calculator**:
  - A simple mathematical calculator to handle operations like addition, subtraction, multiplication, and division.

### Agents
- **Financial Data Collector**:
  - Collects necessary financial information from the user.
- **Budget Calculator**:
  - Processes user data to create a budget plan.
- **Savings Advisor**:
  - Suggests actionable tips to improve savings.


I would like to clarify the current state of the project. I am aware that it is not fully completed because I did not instantiate the calculation task in the main file. When I attempted to do so, I encountered several errors, including version-related issues.

Given these challenges, I decided to present the work with only one functioning agent to ensure a smoother demonstration.#   F i n a n c e _ C h a t b o t 
 
 git branch -m master main

#   F i n a n c e _ C h a t b o t  
 