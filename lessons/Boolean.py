is_male = 1
is_tall = 0

if is_male and is_tall:
    print("you both")
elif is_male and not(is_tall):
    print("your short dude")
elif not(is_male) and is_tall:
    print("your a tall girl")

else:
    print("neiter")