parameters = {
    "arg1": "Hello",
    "arg2": 42
}

def run(parameters):
    print(f"Run function called with arg1: {parameters.get("arg1")}, arg2: {parameters.get("arg2")}")
