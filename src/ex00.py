from Vector import Vector


def main():

    print("Vectors")
    v1 = Vector([5, 2, 3])
    v2 = Vector([-1, 7, 6])

    print(f"{v1} + {v2} = {v1 + v2}")
    print(f"{v1} - {v2} = {v1 - v2}")
    print(f"{v1} * 3 = {v1 * 3}")
    print(f"3 * {v1} = {3 * v1}")

    print("\n","-" * 40, "\n")

    print("Matrices")


if __name__ == "__main__":
    main()
