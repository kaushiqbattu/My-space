def main():
    name = input("Enter you name ")
    hello(name)
    hello()

def hello(x="world"):
    print("Hello,",x)

main()
