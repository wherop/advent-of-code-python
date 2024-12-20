import argparse
import importlib.util
import sys
from pathlib import Path
from utils.generate_day import create_day
from utils import date


def load_day(year: int, day: int):
    # Construct the filename based on year and day
    file_name = f"year{year}_day{day}.py"
    day_path = Path("days") / file_name

    # Check if the file exists
    if not day_path.is_file():
        print(f"Error: No day found for year {year} and day {day}.")
        create_day(year, day)
        sys.exit(1)

    # Dynamically load the day
    spec = importlib.util.spec_from_file_location(f"module_{year}_{day}", day_path)
    if spec is None:  # Check if spec creation failed
        raise ImportError(f"Could not create a module spec for {day_path}")
    module = importlib.util.module_from_spec(spec)
    if module is None:  # Check if module creation failed
        raise ImportError(f"Failed to create module object for {day_path}")
    if spec.loader is None:  # Ensure the loader exists before attempting to load
        raise ImportError(f"No loader found for module {day_path}")
    spec.loader.exec_module(module)
    return module


def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(
        description="Run a specific day based on year and day."
    )
    parser.add_argument(
        "-y",
        "--year",
        default=date.get_year(),
        type=int,
        help="Year of the day (e.g., 2024)",
    )
    parser.add_argument(
        "-d",
        "--day",
        default=date.get_day(),
        type=int,
        choices=range(1, 26),
        help="Day of the challenge (1-25)",
    )

    # Parse arguments
    args = parser.parse_args()
    year: int = args.year
    day: int = args.day

    day_module = None
    try:
        # Load the day
        day_module = load_day(year, day)
    except ImportError as e:
        print(f"Failed to load module: {e}")

    if day_module is None:
        print("Module could not be loaded. Exiting.")
        sys.exit(1)

    # Check for required attributes in the module
    if not hasattr(day_module, "parameters") or not hasattr(day_module, "run"):
        print(
            f"Error: The module for year {year} and day {day} must contain 'parameters' and 'run'."
        )
        sys.exit(1)

    # Retrieve parameters and execute the run function
    parameters = day_module.parameters
    run_function = day_module.run

    # Call the run function
    print(f"Running year {year}, day {day}...")
    run_function(parameters)


if __name__ == "__main__":
    main()
