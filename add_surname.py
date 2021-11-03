#name: Cassidy Ward
#date: 11/3/2021
#description: this function takes as a parameter a list of first names
#then returns a list that contains only those names that start with a "K",
#but with the surname "Kardashian" added to each one, with a space between the first and last names.

def add_surname(lst):
    return [x+" Kardashian" for x in lst if x[0].lower()=='k']

