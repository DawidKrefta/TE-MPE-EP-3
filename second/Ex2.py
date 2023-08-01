import json

file_path = "C:\\Users\\dawid\\OneDrive\\Pulpit\\Dawid\\Stypendia\\CERN_2023\\TE-MPE-EP-3\\second\\deps.json"


def make_graph(filename: str) -> dict:
    """
    Create a graph from a JSON file containing package dependencies.
    Args:
        filename (str): The name of the JSON file to read.
    Returns:
        dict: A dictionary representing the package dependency graph, where the keys are
              package names, and the values are lists of their dependencies.
    Raises:
        FileNotFoundError: If the specified file is not found.
        json.JSONDecodeError: If there is an error decoding the JSON data in the file.
        TypeError: If the filename is not a string.
    """

    if not isinstance(filename, str):
        raise TypeError("Filename must be a string.")

    try:
        with open(filename, "r") as file:
            data = json.load(file)
        graph = {}
        for package, dependecies in data.items():
            graph[package] = dependecies
        return graph
    except FileNotFoundError:
        print(f"ERROR: File '{filename}' not found.")
    except json.JSONDecodeError:
        print(f"ERROR: Invalid JSON format in the file '{filename}'.")
    except Exception as e:
        print(f"ERROR: An unexpected error occurred: {e}")


def print_graph(graph: dict) -> None:
    for package, dependencies in graph.items():
        print(f"- {package}")
        for i, dependency in enumerate(dependencies):
            spaces = "  " * (i + 1)
            print(f"{spaces}- {dependency}")


graph = make_graph(file_path)
print_graph(graph)
