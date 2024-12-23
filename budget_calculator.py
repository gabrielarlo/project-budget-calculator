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


if __name__ == "__main__":
    # Example usage
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

    budget_calculator = DevelopmentProjectBudget(modules, phases, costs)
    budget_calculator.display_budget_summary()
