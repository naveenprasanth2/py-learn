import argparse

parser = argparse.ArgumentParser(description="Simple Calculator")

parser.add_argument("num1", type=float, help="Please enter the first argument")
parser.add_argument("num2", type=float, help="Please enter the second argument")
parser.add_argument("operation", choices=["add", "sub", "mul", "div"], help="Operation to perform")

args = parser.parse_args()

print(args)

