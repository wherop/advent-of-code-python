def read_input(path:str):
    with open(path, 'r') as file:
        return file.read()
    
def parse_input(data:str):
    result = data.splitlines()
    # Optional: Remove any empty lines if needed
    return [line for line in result if line.strip()]