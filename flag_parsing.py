import argparse

def parse():
    parser = argparse.ArgumentParser(description="Current weather info in specified city")

    parser.add_argument("city", type=str, help="The city whose weather you want to see")

    args = parser.parse_args()

    return args