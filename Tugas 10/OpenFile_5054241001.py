file = open("5054241001.txt", "w")
Line = ["Nama saya Ustu Bina Syahdiba \n", "Asal saya dari HelpAgung \n", "Saya suka makan abon \n"]

file.write("Ambatakum Assalamualaikum \n")
file.writelines(Line)
file.close()

file = open("5054241001.txt", "r+")
print("Output of the file after modification:")
print(file.read())
print()

file.seek(0)

print(f"Output of Read({len("Ambatakum Assalamualaikum \n")}) function is: ")
print(file.readline(100))
print(file.read())
