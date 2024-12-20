def main():
    greeting = "Привет, как дела?"
    print(value(greeting))

def value(greeting):
    if greeting.startswith("здравствуйте"):
        return 0
    elif greeting.startswith(""):
        return 20
    else:
        return 20

if __name__ == "__main__":
    main()
