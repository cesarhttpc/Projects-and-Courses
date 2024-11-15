# %%
my_string="Hello bola de hello Hello" 
char = my_string[0]
# print(char)

new_text = my_string.replace("Hello ","Hi")
print(new_text)

cadena = "           Para cadenas separadas como texto    "   
pegado = cadena.strip()
print(cadena.upper().strip())
# print(pegado, "text")

x = 1/1
type(x)

# %%
int(False)

# %%
tuple1 = (1,3,3,5,2,9,2,5,2)

tuple1[2] = 00
print(tuple1)

# %%

lista = [1,5,6,3,8,4,5]

del(lista[1])
print(lista)
# %%
lista1 = [1,2,3]
lista2 = [1,1,1]

print(lista1+lista2)
# %%

# Dictionaries
Dict = {"Triller": 1982, "Back in black": 1980, "The Dark Side of the Moon": 1973, "The Bodyguard": 1992}

Dict["Back in black"]

# ADD
Dict["The Graduation"] = '2007'

# DELETE    
# del(Dict["The Graduation"])

print(Dict)

# Is it in the dict?
isit = "Starboy" in Dict
print(isit)

# ALL THE KEYS
Dict.keys()
Dict.values()


# %%
# KEYS AS A LIST    
listaKeys = list(Dict.keys())
print(listaKeys)

# %%
# SET

A = ["AC/DC", "Back in Black", "NSYNC", "Thriller","AC/DC"]

conjunto_A = set(A)
print(conjunto_A)

conjunto_A.add("KISS")
print(conjunto_A)

conjunto_A.remove("KISS")
print(conjunto_A)

# Is it in?
"AC/DC" in conjunto_A

B = ["The Dark Side of the Moon", "Thriller", "AC/DC"]
conjunto_B = set(B)

# INTERSECTION
print(conjunto_A & conjunto_B)

# UNION
print(conjunto_A.union(conjunto_B)) 


# %%
for i, x in enumerate(['A', 'B', 'C']):
    print(i, x)
# %%

lista = [1,3,2]
lista.sort()
print(lista)
# sorted(lista)


# %%


class Vehicle:
    color = "white"


    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage
        self.seating_capacity = None


    def assign_seating_capacity(self, seating_capacity):
        self.seating_capacity = seating_capacity


V1 = Vehicle(150, 25)

# dir(V1)

V1.color = 'red'
#%%

x = 1 
x = x > -5
print(x)


