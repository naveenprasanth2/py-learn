import argparse

parser = argparse.ArgumentParser(description="Simple Calculator")

parser.add_argument("num1", type=float, help="Please enter the first argument")
parser.add_argument("num2", type=float, help="Please enter the second argument")
parser.add_argument("operation", choices=["add", "sub", "mul", "div"], help="Operation to perform")

args = parser.parse_args()

match args.operation:
    case "add":
        print(args.num1 + args.num2)
    case "sub":
        print(args.num1 - args.num2)
    case "mul":
        print(args.num1 * args.num2)
    case "div":
        print(args.num1 / args.num2)