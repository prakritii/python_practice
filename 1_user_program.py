father_name = input("Enter your father name: ")
father_age = input("What is your father age?: ")
father_gender = input("Enter your father gender: ")
father_occupation = input("What is your father occupation?: ")
father_live = input("Where do your father live?: ")
mother_name = input("Enter your mother name: ")
mother_age = input("What is your mother age?: ")
mother_gender = input("Enter your mother gender: ")
mother_occupation = input("What is your mother occupation?: ")
mother_live = input("Where do your mother live?: ")
brother_name = input("Enter your brother name: ")
brother_age = input("What is your brother age?: ")
brother_gender = input("Enter your brother gender: ")
brother_occupation = input("What is your brother occupation?: ")
brother_live = input("Where do your brother live?: ")
family_details = {
    "Father": {
        "Name":father_name,
        "Age": father_age,
        "Gender": father_gender,
        "Job": father_occupation,
        "City": father_live
    },
    "Mother": {
        "Name": mother_name,
        "Age": mother_age,
        "Gender": mother_gender,
        "Job": mother_occupation,
        "City": mother_live
    },
    "Brother": {
        "Name": brother_name,
        "Age": brother_age,
        "Gender": brother_gender,
        "Job": brother_occupation,
        "City": brother_live
    }

}


print(f'''
Your father name is {father_name}, He is {father_age} years old, He is {father_gender}, who works as a {father_occupation} and lives in {father_live}/n
Your mother name is {mother_name}, she is {mother_age} years old, a {mother_gender} who works as a {mother_gender} and lives in {mother_live}/n
Your brother name is {brother_name}, he is {brother_age} years old, he works as a {brother_occupation} and lives in {brother_live}
''')
