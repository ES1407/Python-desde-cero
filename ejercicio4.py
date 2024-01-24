def to_mod_list(employee_list):
   """ Modifies the employee list of dictionaries into list of employee-department strings """
   return list(map(mod, employee_list))

def generate_usernames(mod_list):
   """ Generates a list of usernames """
   return [name.replace(" ", "_") for name in mod_list]

def map_id_to_initial(employee_list):
   """ Maps employee id to first initial """
   return {emp['id']: emp['name'][0] for emp in employee_list}

def main():
   mod_emp_list = to_mod_list(employee_list)
   print("Modified employee list: " + str(mod_emp_list) + "\n")

   print(f"List of usernames: {generate_usernames(mod_emp_list)}\n")

   print(f"Initials and ids: {map_id_to_initial(employee_list)}")

if __name__ == "__main__":
   main()