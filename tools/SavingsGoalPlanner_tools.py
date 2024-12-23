from langchain.tools import tool

class SavingsGoalPlannerTool:
    @tool("Savings Goal Planner")
    def calculate_savings_goal(goal_amount, time_months):
        """
        Calculates the monthly savings required to reach a goal.
        Example: 'calculate_savings_goal(5000, 12)'
        """
        try:
            monthly_savings = goal_amount / time_months
            return f"To reach your goal of ${goal_amount}, you need to save ${monthly_savings:.2f} per month."
        except Exception as e:
            return f"Error: {str(e)}"
