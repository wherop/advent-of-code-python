import argparse
from pathlib import Path
from constants import APP_DIR

TEMPLATE_PATH = APP_DIR + "template"
DAYS_PATH = APP_DIR + "days"

template_dir = Path(TEMPLATE_PATH)
template_name = "year0000_day00.py"
template_path = template_dir / template_name
with open(template_path, "r") as file:
    template = file.read()

def create_day(year, day):
    # Construct the file path
    days_dir = Path(DAYS_PATH)
    days_dir.mkdir(exist_ok=True)
    file_name = f"year{year}_day{day}.py"
    file_path = days_dir / file_name

    # Check if the file already exists
    if file_path.exists():
        print(f"Day {file_name} already exists.")
        return
    
    # Write the template to the file
    with open(file_path, "w") as file:
        file.write(template.format(year=year, day=day))

    print(f"Day {file_name} created at {file_path}")

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description="Generate a day for a specific year and day.")
    parser.add_argument("year", type=int, help="Year of the day (e.g., 2024)")
    parser.add_argument("day", type=int, choices=range(1, 26), help="Day of the challenge (1-25)")

    # Parse arguments
    args = parser.parse_args()
    year, day = args.year, args.day

    # Create day
    create_day(year, day)

if __name__ == "__main__":
    main()