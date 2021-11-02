#Creating functions with outputs
# 
def name_function(f_name, l_name):
    if f_name == "" or l_name == "":
        return "you didn't provide a valid inputs"

# using the .title function capitalizes the first letter. 

    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"Results: {formated_f_name} {formated_l_name}"

print(name_function (input("What is your first name? "), input("What is your last name? ")))
