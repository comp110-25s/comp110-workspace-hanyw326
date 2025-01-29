"""My second exercise in COMP110!"""

__author__ = "730823094"


def tea_bags(people: int) -> int:
    """
    Calculate the number of tea bags required for a tea party.

    """
    return people * 2


def treats(people: int) -> int:
    """
    Calculate the number of treats needed based on the number of guests.

    """
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """
    Calculate the total cost of tea bags and treats combined.

    """
    return tea_count * 0.50 + treat_count * 0.75


def main_planner(guests: int) -> None:
    """
    Orchestrates the tea party planning by calculating tea bags, treats, and cost,
    then prints the details in a formatted output.

    """
    print(f"A Cozy Tea Party for {guests} People!")
    print(f"Tea Bags: {tea_bags(guests)}")
    print(f"Treats: {treats(guests)}")
    print(f"Cost: ${cost(tea_bags(guests), treats(guests))}")


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
