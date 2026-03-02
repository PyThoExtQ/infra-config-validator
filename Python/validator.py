import yaml

def validate(file):
    with open(file) as f:
        yaml.safe_load(f)
    print("Config valid")
