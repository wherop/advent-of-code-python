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