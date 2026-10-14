def calculate_total(price, quantity):
    return price * quantity


def greet_user(name):
    print("Welcome, " + name)


if __name__ == "__main__":
    print(calculate_total(100, 3))
    greet_user("SonarQube")