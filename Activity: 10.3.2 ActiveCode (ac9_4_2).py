try:
    with open("travel_plans2.txt", "r") as fileref:
        content = fileref.readlines()
        num_lines = len(content)
    print("number of lines", num_lines)
except IOError as e:
    print(f"An error occurred: {e}")