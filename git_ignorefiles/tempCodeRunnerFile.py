total_no_of_classes_attended = int(input("enter the number of classes attended: "))
a = total_no_of_classes
b = total_no_of_classes_attended
percentage_of_classes_attended = b/a * 100
c = percentage_of_classes_attended
if b/a * 100 >= 75:
    print("student is allowed to sit in the exam")
else:
    ("student is not allowed to sit in the exam")
print(c)
