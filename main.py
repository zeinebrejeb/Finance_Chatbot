import os
from crewai import Agent, Task, Crew, Process
from decouple import config
from dotenv import load_dotenv
from textwrap import dedent
from agents import CustomAgents
from tasks import FinancialTasks

load_dotenv()

api_key = config("GEMINI_API_KEY")
os.environ["GEMINI_API_KEY"] = api_key

class FinanceCrew:
    def __init__(self, monthly_income, fixed_expenses, discretionary_expenses, savings_goal=None):
        self.monthly_income = monthly_income
        self.fixed_expenses = fixed_expenses
        self.discretionary_expenses = discretionary_expenses
        self.savings_goal = savings_goal

    
    def run(self):
        agents = CustomAgents()
        
        financial_data_collector = agents.financial_data_collector()
        budget_calculator = agents.budget_calculator()
        savings_advisor = agents.savings_advisor()

        response = financial_data_collector.predict("Collect financial data for the user.")
        print("Financial Data Collected:", response)
        
        budget_response = budget_calculator.predict("Calculate budget based on collected financial data.")
        print("Budget Calculated:", budget_response)

        savings_response = savings_advisor.predict("Provide savings tips based on budget.")
        print("Savings Tips:", savings_response)

        return budget_response, savings_response


if __name__ == "__main__":
    print("## Welcome to Your Finance Chatbot")
    print("----------------------------------")

    monthly_income = float(input(dedent("Enter your monthly income: ")))
    fixed_expenses = float(input(dedent("Enter your fixed expenses (e.g., rent, bills): ")))
    discretionary_expenses = float(input(dedent("Enter your discretionary expenses (e.g., hobbies, dining): ")))
    savings_goal = input(dedent("Enter your savings goal (optional, press Enter to skip): "))

    savings_goal = float(savings_goal) 
    if savings_goal else None
    finance_crew = FinanceCrew(monthly_income, fixed_expenses, discretionary_expenses, savings_goal)
    result = finance_crew.run()

    print("\n\n########################")
    print("## Here's the result of your Finance Chatbot:")
    print("########################\n")
    print(result)