import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class DevelopmentProjectBudget:
    def __init__(self, modules, phases, costs):
        """
        Initialize the budget calculator with modules, phases, and costs.
        :param modules: List of module names.
        :param phases: List of phase names.
        :param costs: Dictionary with keys as (module, phase) tuples and values as costs.
        """
        self.modules = modules
        self.phases = phases
        self.costs = costs

    def calculate_total_cost(self):
        """
        Calculate the total cost of the project.
        :return: Total cost as a float.
        """
        return sum(self.costs.values())

    def get_cost_breakdown(self):
        """
        Get a detailed breakdown of costs by module and phase.
        :return: Dictionary with module names as keys and phase cost breakdowns as values.
        """
        breakdown = {module: {phase: self.costs.get((module, phase), 0) for phase in self.phases} for module in self.modules}
        return breakdown

    def display_budget_summary(self):
        """
        Display the budget summary including total cost and breakdown.
        """
        print("Development Project Budget Summary")
        print("=================================")
        for module, phase_costs in self.get_cost_breakdown().items():
            print(f"Module: {module}")
            for phase, cost in phase_costs.items():
                print(f"  Phase: {phase}, Cost: ${cost:.2f}")
            print()
        print(f"Total Project Cost: ${self.calculate_total_cost():.2f}")


def call_gpt_for_budget(project_type):
    """
    Placeholder for calling GPT API to generate a budget based on project type.
    :param project_type: The type of project.
    :return: A tuple of modules, phases, and costs.
    """
    client = OpenAI(api_key=os.getenv("OPENAI_KEY"))

    response = client.chat.completions.create(
        model="gpt-4",
        messages=[
            {
                "role": "user",
                "content": f"Generate a budget for a {project_type} project."
            }
        ],
        max_tokens=150
    )

    # Parse the response from the GPT model
    response_content = response.choices[0].message.content.strip()
    try:
        budget_data = json.loads(response_content)
    except json.JSONDecodeError:
        raise ValueError("The response from the GPT model is not valid JSON.")

    # Adjust these keys based on the actual response format
    # Adjust these keys based on the actual response format
    modules = budget_data.get("modules", ["Module1", "Module2"])
    phases = budget_data.get("phases", ["Design", "Development", "Testing"])
    costs = budget_data.get("costs", {
        ("Module1", "Design"): 1000,
        ("Module1", "Development"): 3000,
        ("Module1", "Testing"): 500,
        ("Module2", "Design"): 1200,
        ("Module2", "Development"): 2500,
        ("Module2", "Testing"): 600,
        ("Module1", "Development"): 2000,
        ("Module1", "Testing"): 500,
        ("Module2", "Design"): 1200,
        ("Module2", "Development"): 2500,
        ("Module2", "Testing"): 600,
    })

    # Example: If the response format is different, adjust the keys accordingly
    # modules = budget_data.get("project_modules", [])
    # phases = budget_data.get("project_phases", [])
    # costs = budget_data.get("project_costs", {})

    # Example: If the response format is different, adjust the keys accordingly
    # modules = budget_data.get("project_modules", [])
    # phases = budget_data.get("project_phases", [])
    # costs = budget_data.get("project_costs", {})

    return modules, phases, costs


def get_project_budget(project_type):
    modules, phases, costs = call_gpt_for_budget(project_type)
    return DevelopmentProjectBudget(modules, phases, costs)


if __name__ == "__main__":
    project_type = input("Enter the project type (e.g., 'pos for restaurant'): ").strip().lower()
    budget_calculator = get_project_budget(project_type)
    budget_calculator.display_budget_summary()
