# %%
import sys
# entrada = input()
for n in sys.stdin:

# lineas = entrada.split('\n')
# print(lineas)
# for n in lineas:

    n = int(n)
    cuadrados = n*(n+1)*(2*n+1)/6

    rectangulos = (n*(n+1)/2)**2

    print(int(cuadrados),' ',int(rectangulos))










