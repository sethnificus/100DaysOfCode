#Creating functions with outputs
# 
def name_function(f_name, l_name):

    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"

print(name_function ("SeTH", "KUTTner"))
