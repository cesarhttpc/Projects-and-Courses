# %%

# import os

# path_console = os.getcwd()
# path_file =  "\Example.txt"
# print(path_console)

# file = open(path_console+path_file,'r')
# # file.name()
# # file.read()
# # file.close()

# %%

file = open("Example.txt","r")
print("File name: ", file.name)
print("File mode: ", file.mode)
archivo = file.read()
file.close()

print(archivo)

# %%
# Alternative for open files

with open("Example.txt","r") as file1:
    file_stuff = file1.read()

    print(file_stuff)

print(file1.closed)
print(file_stuff)


# %%
with open("Example.txt","r") as file1:
    file_stuff = file1.readline()
    print(file_stuff)

    file_stuff = file1.readline()
    print(file_stuff)

# %%
with open("Example.txt", "r") as file2:
    for line in file2:
        print(line)

# %%

with open("Example.txt","r") as file3:
    file_stuff = file3.readline(16)
    print(file_stuff)

    file_stuff = file3.readline(5)
    print(file_stuff)

    file_stuff = file3.readline(9)
    print(file_stuff)

# %%

with open("Example2.txt","w") as file1:
    file1.write("This is line A\n")
    file1.write("This is line B\n")

# %%
Lines = ["This is line A\n","This is line B\n","This is line C\n"]
with open("Example2.txt","w") as file1:

    for line in Lines:
        file1.write(line)

# %%
# COPY A FILE

with open("Example.txt","r") as readfile:
    with open("Example3.txt","w") as writefile: 

        for line in readfile:
            writefile.write(line)

# %%

import pandas as pd

songs = {'Album': ['Thriller','Back in Black','The Dark Side of the Moon','The Bodyguard','Bat out of Hell'],
                   'Released': [1982, 1990, 1973,1992,1977],
                   'Length' :['00:43:19','00:42:11','00:42:49','00:55:44','00:46:33']
                   }

songs_frame = pd.DataFrame(songs)

print(songs_frame)

songs_frame.to_csv('songs.csv')

# %%
songs_frame.loc[1:3,'Album']

# %%
import numpy as np

A = np.array([[1,2],[3,4]])
B = np.array([[5,6],[7,8]])
print(A.dot(B)) # print(np.dot(A,B))
print(A*B)

# %%
C = np.array([[1,1,3],[4,3,2]])
print(C[0:2,2])