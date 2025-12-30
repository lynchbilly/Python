def main():
    spacecraft = {"name": "James Webb Space Telescope"}
    print(create_report(spacecraft))


def create_report(spacecraft):
    return f"""
    ========= REPORT =========

    Name: {spacecraft.get("name")}
    Distance: {spacecraft.get("distance")} AU

    ==========================
    """


main()
