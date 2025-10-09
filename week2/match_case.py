day = input("What day is it today? ")
match day:
    case "Saturday" | "Sunday":
        print("weekend!!!!")
    case "Monday" | "Tuesday" | "Wednesday" | "Thursday" | "Friday":
        print("It is a weekday.")
    case _:
        print("OOPS")