def collect_user_data():
    print("\n👋 Welcome to Smart Health Assistant!\n")
    weight = float(input("Enter your weight (in kg): "))
    height = float(input("Enter your height (in cm): "))
    age = int(input("Enter your age: "))
    gender = input("Enter your gender (Male/Female): ")
    preference = input("Dietary Preference (Veg/Non-Veg/Vegan): ")

    return {
        "weight": weight,
        "height": height,
        "age": age,
        "gender": gender,
        "dietary_preference": preference
    }
