import argparse
import importlib.util
import sys
from pathlib import Path
from generate_day import create_day

def load_day(year, day):
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
    day = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(day)
    return day

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Run a specific day based on year and day.")
    parser.add_argument("year", type=int, help="Year of the day (e.g., 2024)")
    parser.add_argument("day", type=int, choices=range(1,26), help="Day of the challenge (1-25)")

    # Parse arguments
    args = parser.parse_args()
    year, day = args.year, args.day

    # Load the day
    day = load_day(year, day)

    # Check for required attributes in the module
    if not hasattr(day, "parameters") or not hasattr(day, "run"):
        print(f"Error: The day for year {year} and day {day} must contain 'parameters' and 'run'.")
        sys.exit(1)

    # Retrieve parameters and execute the run function
    parameters = day.parameters
    run_function = day.run

    # Call the run function
    print(f"Running year {year}, day {day}...")
    run_function(parameters)

if __name__ == "__main__":
    main()