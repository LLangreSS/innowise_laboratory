def generate_profile(age):
    """Returns life stage ('Child', 'Teenager', or 'Adult') based on age."""
    if 0 <= age <= 12:
        return 'Child'
    elif 13 <= age <= 19:
        return 'Teenager'
    else:
        return 'Adult'


def main():
    """Main function to collect user data, generate profile, and display summary."""
    user_name = input("Enter your full name: ")
    birth_year_str = input("Enter your birth year: ")
    birth_year = int(birth_year_str)
    current_age = 2025 - birth_year

    hobbies = []
    while True:
        hobby_input = input("Enter a favorite hobby or type 'stop' to finish: ")
        if hobby_input.lower() == 'stop':
            break
        hobbies.append(hobby_input)

    life_stage = generate_profile(current_age)
    user_profile = {"name": user_name,
                    "age": current_age,
                    "stage": life_stage,
                    "hobbies": hobbies}

    print("\n---")
    print("Profile Summary:")
    print(f"Name: {user_profile['name']}")
    print(f"Age: {user_profile['age']}")
    print(f"Life Stage: {user_profile['stage']}")

    if len(user_profile["hobbies"]) == 0:
        print("You didn't mention any hobbies.")
    else:
        print(f"Favorite Hobbies ({len(user_profile['hobbies'])}):")
        for hobby in user_profile["hobbies"]:
            print(f"- {hobby}")
    print("---")


if __name__ == '__main__':
    main()
