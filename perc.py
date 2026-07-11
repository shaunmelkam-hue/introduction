print("Enter marks obtained in 4 subjects: ")
math = int(input("Math: "))
science = int(input("Science: "))
english = int(input("English: "))
hindi = int(input("Hindi: "))

sum = math + science + english + hindi
print("sum of math, science, english and hindi is: ", sum)

perc=(sum / 400) * 100

print(end="Percentage mark = ")
print(perc)