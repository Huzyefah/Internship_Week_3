# Define the source data (2D array)
electricity_matrix = [
    [50, 120, 250],  # Slab 1: Units consumed for each customer
    [80, 150, 280],  # Slab 2: Units consumed for each customer
    [120, 200, 320]  # Slab 3: Units consumed for each customer
]

# Display student's ID
student_id = "YourStudentID"
print(f"Student ID: {student_id}")

# Function to calculate and display cost for slab 1
def costSlab1():
    slab1_rate = 10  # Cost per unit for slab 1
    for i, units in enumerate(electricity_matrix[0]):
        cost = units * slab1_rate
        print(f"Customer {i + 1}, Slab 1 Cost: Rs. {cost}")

# Function to calculate and display cost for slab 2
def costSlab2():
    slab2_rate = 15  # Cost per unit for slab 2
    for i, units in enumerate(electricity_matrix[1]):
        cost = units * slab2_rate
        print(f"Customer {i + 1}, Slab 2 Cost: Rs. {cost}")

# Function to calculate and display cost for slab 3
def costSlab3():
    slab3_rate = 20  # Cost per unit for slab 3
    for i, units in enumerate(electricity_matrix[2]):
        cost = units * slab3_rate
        print(f"Customer {i + 1}, Slab 3 Cost: Rs. {cost}")

# Main menu
while True:
    print("\n1. Display bill of slab 1 and slab 2")
    print("2. Display bill of slab 3")
    print("Press any other key to exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        costSlab1()
        costSlab2()
    elif choice == '2':
        costSlab3()
    else:
        print("Exiting the program.")
        break
