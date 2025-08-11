#%%
numero = 4
count = 4

while count <= 100:
    if count % numero == 0:
        print(f"{count} é divisível por {numero}")

    count +=1
print("Acabou")