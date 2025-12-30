from soil import sample


def main():
    moisture = sample()
    print(f"Moisture is {moisture}%")

    while moisture > 20:
        moisture = sample()
        print(f"Moisture is {moisture}%")

    print("Time to water!")


main()
