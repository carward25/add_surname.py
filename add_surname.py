#name: Cassidy Ward
#date: 11/3/2021
#description: this function takes as a parameter a list of first names
#then returns a list that contains only those names that start with a "K",
# but with the surname "Kardashian" added to each one, with a space between the first and last names.

def add_surname(name_list):
   res = [name+' Kardashian' for name in name_list if name[0]=='K']
   return res

name_list = ["Kiki", "Krystal", "Pavel", "Annie", "Koala"]
print(add_surname(name_list))
