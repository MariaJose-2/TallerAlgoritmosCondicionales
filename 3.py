"""""
Diseñe un algoritmo que guarde el nombre del aprendiz, nombre del curso,
nota definitiva, el nro de clases en el semestre y el número de las fallas. En el
caso de que las fallas superen el 30% del número de clases se debe mostrar
la nota que no aprobó y se calificara cero(0).
"""
learnerName = input("Enter the name of the trainee: ")
courseName = input("Enter the name of the course: ")
finalNote = float(input("Enter the final note: "))
num_classes_semester = int(input("Enter the number of classes in the semester: "))
number_failures = int(input("Enter the number of failures: "))
allowed_failure_percentage = 0.3 * num_classes_semester
if number_failures > allowed_failure_percentage:
    print(f"Not approved. Final score: 0")
else:
    print(f"Approved. Final note:{finalNote}")
    