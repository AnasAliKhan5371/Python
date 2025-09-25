# list comprehensions
# view student data, find passing students, calculate the class average, and identify top performers

students=[
    {"name":"Alice","grade":88},
    {"name":"Bob","grade":78},
    {"name":"Claire","grade":82},
    {"name":"Diana","grade":56},
    {"name":"Elizabeth","grade":99},
    {"name":"Fiona","grade":91},
    {"name":"Gary","grade":66},
    {"name":"Natasha","grade":100}
]

def menu():

    print("\n--- Student Grade Manager ---")
    print("1. Display All Students")
    print("2. Passing Students ( >= 70)")
    print("3. Class Average")
    print("4. Top Performers ( >= 90)")
    print("5. Get Students Names")
    print("6. Exit")
    print("-----------------------------")

def main():
    while True:
        menu()
        choice=input("Enter choice (1-6) : ")

        if choice == '1':
            print("\n--- All Students ---")
            for student in students:
                print(f"Name: {student['name']}, Grade: {student['grade']}")

        elif choice=='2':
            passing=[s for s in students if s['grade']>=70]
            print("\n--- Passing Students (>= 70) ---")
            for student in passing:
                print(f"Name: {student['name']}, Grade: {student['grade']}")

        elif choice == '3':
            grades = [s['grade'] for s in students]
            if grades:
                average = sum(grades) / len(grades)
                print(f"\n📈 Class Average: {average:.2f}")
            else:
                print("No students to calculate an average for.")

        elif choice == '4':
            top_performers = [s for s in students if s['grade'] >= 90]
            print("\n--- Top Performers (>= 90) ---")
            for student in top_performers:
                print(f"Name: {student['name']}, Grade: {student['grade']}")

        elif choice == '5':
            student_names = [s['name'] for s in students]
            print("\n--- Student Names ---")
            print(", ".join(student_names))

        elif choice == '6':
            print("Exiting the program. Goodbye! 👋")
            break

        else:
            print("\nInvalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()