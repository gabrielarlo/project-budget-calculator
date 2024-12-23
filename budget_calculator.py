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
    # This is a placeholder. In a real implementation, you would call the GPT API here.
    # For example, using OpenAI's API client:
    # response = openai.Completion.create(
    #     model="gpt-4o-mini",
    #     prompt=f"Generate a budget for a {project_type} project.",
    #     max_tokens=150
    # )
    # Parse the response to extract modules, phases, and costs.
    
    # Simulated response
    if project_type == "pos for restaurant":
        modules = ["POS Module", "Inventory Module", "Billing Module"]
        phases = ["Design", "Development", "Testing"]
        costs = {
            ("POS Module", "Design"): 2000,
            ("POS Module", "Development"): 5000,
            ("POS Module", "Testing"): 2500,
            ("Inventory Module", "Design"): 1500,
            ("Inventory Module", "Development"): 4000,
            ("Inventory Module", "Testing"): 2000,
            ("Billing Module", "Design"): 1000,
            ("Billing Module", "Development"): 3000,
            ("Billing Module", "Testing"): 1500,
        }
    else:
        print("Unknown project type. Using default example project.")
        modules = ["Module1", "Module2"]
        phases = ["Design", "Development", "Testing"]
        costs = {
            ("Module1", "Design"): 1000,
            ("Module1", "Development"): 3000,
            ("Module1", "Testing"): 1500,
            ("Module2", "Design"): 1200,
            ("Module2", "Development"): 3500,
            ("Module2", "Testing"): 1800,
        }
    return modules, phases, costs


def get_project_budget(project_type):
    modules, phases, costs = call_gpt_for_budget(project_type)
    return DevelopmentProjectBudget(modules, phases, costs)


if __name__ == "__main__":
    project_type = input("Enter the project type (e.g., 'pos for restaurant'): ").strip().lower()
    budget_calculator = get_project_budget(project_type)
    budget_calculator.display_budget_summary()
