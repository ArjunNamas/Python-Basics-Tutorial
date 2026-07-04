def ask_questions(person):
    age = int(input(f"What is your {person}'s age? ")) 
    name = input(f"What is your {person}'s name? ")
    occ = input(f"What is your {person}'s occupation? ")

    return name, age, occ 

my_name, my_age, my_occ = ask_questions("own")
friend_name, friend_age, friend_occ = ask_questions("friend")


print(my_name)