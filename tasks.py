# To know more about the Task class, visit: https://docs.crewai.com/concepts/tasks
from crewai import Task
from textwrap import dedent

class FinancialTasks:
    def collect_financial_information(self, agent,monthly_income, fixed_expenses, discretionary_expenses, savings_goal):
        return Task(
            description=dedent(f"""
            **Task**: Collect financial information
            **Description** :Engage with the user to collect the following financial information:
                - Monthly income.
                - Fixed expenses (e.g., rent, bills).
                - Discretionary expenses (e.g., dining, hobbies).
                - Savings goal.

                Ensure the data is correctly categorized and validated. 
                Provide clarifying prompts if necessary to get accurate inputs.
                The final output should be a summary of the user's financial details.

            **Parameters** 
                - monthly_income: The user's total income per month (numeric).
                - fixed_expenses: Recurring fixed costs like rent, utilities (numeric).
                - discretionary_expenses: Costs for hobbies, dining, and non-essentials (numeric).
                - savings_goal (optional): The amount the user wishes to save monthly (numeric or None).
                Your final answer must be a detailed

                monthly_income: {monthly_income}
                fixed_expenses: {fixed_expenses}
                discretionary_expenses: {discretionary_expenses}
                savings_goal: {savings_goal}
                
            """),
            agent=agent,
            expected_output="A summary of the user's financial data."
        )

    def calculate_budget(self, agent,monthly_income, fixed_expenses, discretionary_expenses, savings_goal):
        return Task(
            description=dedent(f"""
                **Task**: Calculate user's budget
                **Description**: Using the user's financial information, calculate their budget based on the 50/30/20 rule:
                    - Allocate 50% of income to needs (fixed expenses).
                    - Allocate 30% of income to wants (discretionary expenses).
                    - Allocate 20% of income to savings.

                    Adjust allocations if necessary based on the user's financial details and provide clear explanations for any changes. 
                    Ensure transparency and clarity in the calculations.

                **Parameters**:
                    - monthly_income: The user's total income per month (numeric).
                    - fixed_expenses: Recurring fixed costs like rent, utilities (numeric).
                    - discretionary_expenses: Costs for hobbies, dining, and non-essentials (numeric).
                    - savings_goal (optional): The amount the user wishes to save monthly (numeric or None).

                **User Input**:
                monthly_income: {monthly_income}
                fixed_expenses: {fixed_expenses}
                discretionary_expenses: {discretionary_expenses}
                savings_goal: {savings_goal}

                Calculate and return the following:
                - Allocation for fixed expenses (50% or adjusted based on input).
                - Allocation for discretionary expenses (30% or adjusted based on input).
                - Allocation for savings (20% or adjusted based on input).
                - Explanation of any adjustments made to the allocation.
                    
            """),
            agent=agent,
            expected_output="A detailed budget breakdown."
        )

    def provide_savings_tips(self, agent):
        return Task(
            description=dedent(f"""
                Based on the user's financial data and calculated budget, provide 1–2 personalized savings tips. 
                Ensure the tips are actionable, realistic, and tailored to the user's habits.
                
                - "Reduce discretionary spending on dining by 10%."
                - "Set up an emergency fund."
            """),
            agent=agent,
            expected_output="A list of personalized savings tips."
        )

