from typing import List
import struct
from rich.console import Console
from rich.table import Table


# Employee Class
class Employee:
    def __init__(self, name: str, salary: float, years: float):
        self.name = name
        self.salary = salary
        self.years = years

    def processRaise(self) -> None:
        # Find Raise amount based on table
        if self.salary <= 30000:
            if self.years <= 2:
                raise_amount = 0.03
            else:
                raise_amount = 0.025
        elif self.salary <= 60000:
            if self.years <= 5:
                raise_amount = 0.0225
            else:
                raise_amount = 0.002
        elif self.salary <= 80000:
            if self.years <= 5:
                raise_amount = 0.00175
            else:
                raise_amount = 0.0015
        else:
            if self.years <= 5:
                raise_amount = 0.00125
            else:
                raise_amount = 0.001

        # Update salary
        new_salary = (self.salary * raise_amount) + self.salary
        self.salary = new_salary

    def __str__(self) -> str:
        return f"Employee Name: {self.name} Salary: {self.salary} Years of Experience: {self.years}"


# Custom DataInputStream - mimics Java implementations
class DataInputStream:
    def __init__(self, stream):
        self.stream = stream

    def read_boolean(self):
        data = self.stream.read(1)
        if len(data) < 1:
            raise EOFError("Unexpected end of stream")
        return struct.unpack("?", data)[0]

    def read_byte(self):
        data = self.stream.read(1)
        if len(data) < 1:
            raise EOFError("Unexpected end of stream")
        return struct.unpack("b", data)[0]

    def read_unsigned_byte(self):
        data = self.stream.read(1)
        if len(data) < 1:
            raise EOFError("Unexpected end of stream")
        return struct.unpack("B", data)[0]

    def read_char(self):
        data = self.stream.read(2)
        if len(data) < 2:
            raise EOFError("Unexpected end of stream")
        return chr(struct.unpack(">H", data)[0])

    def read_double(self):
        data = self.stream.read(8)
        if len(data) < 8:
            raise EOFError("Unexpected end of stream")
        return struct.unpack(">d", data)[0]

    def read_float(self):
        data = self.stream.read(4)
        if len(data) < 4:
            raise EOFError("Unexpected end of stream")
        return struct.unpack(">f", data)[0]

    def read_short(self):
        data = self.stream.read(2)
        if len(data) < 2:
            raise EOFError("Unexpected end of stream")
        return struct.unpack(">h", data)[0]

    def read_unsigned_short(self):
        data = self.stream.read(2)
        if len(data) < 2:
            raise EOFError("Unexpected end of stream")
        return struct.unpack(">H", data)[0]

    def read_long(self):
        data = self.stream.read(8)
        if len(data) < 8:
            raise EOFError("Unexpected end of stream")
        return struct.unpack(">q", data)[0]

    def read_utf(self):
        length_data = self.stream.read(2)
        if len(length_data) < 2:
            raise EOFError("Unexpected end of stream")
        utf_length = struct.unpack(">H", length_data)[0]
        utf_data = self.stream.read(utf_length)
        if len(utf_data) < utf_length:
            raise EOFError("Unexpected end of stream")
        return utf_data.decode("utf-8")

    def read_int(self):
        data = self.stream.read(4)
        if len(data) < 4:
            raise EOFError("Unexpected end of stream")
        return struct.unpack(">i", data)[0]


# Main function, processes employee data from a binary file
def process_employee_data(file_path1: str, file_path2: str) -> None:
    employees = []
    old_employee_info = []
    total_salary_before = 0
    total_salary_after = 0

    console = Console()

    table = Table(title="Employee Data")
    table.add_column("Name")
    table.add_column("Salary")
    table.add_column("Years worked")
    table_processed = Table(title="New Employee Data")
    table_processed.add_column("Name")
    table_processed.add_column("New Salary")
    table_processed.add_column("Years worked")
    salary_table = Table(title="Salaries before : after")
    salary_table.add_column("Before Processing")
    salary_table.add_column("After Processing")

    with open(file_path1, "rb") as file:
        stream = DataInputStream(file)

        try:
            while True:
                # Parse data
                name = stream.read_utf()
                salary = stream.read_double()
                years = stream.read_double()

                # Create Employee, add to employees list
                employee = Employee(name, salary, years)
                employees.append(employee)
                table.add_row(employee.name, str(employee.salary), str(employee.years))

                # Add onto total salary before
                total_salary_before += employee.salary

                # Update salary
                employee.processRaise()
                total_salary_after += employee.salary

        except EOFError:
            # End of file reached
            pass

    # print Current Employee data
    console.print(table)
    print()

    # populate processed table and print
    for employee in employees:
        table_processed.add_row(
            employee.name, str(employee.salary), str(employee.years)
        )
    console.print(table_processed)

    # populate salary_table and print
    salary_table.add_row(str(total_salary_before), str(total_salary_after))
    console.print(salary_table)


# Call to main
if __name__ == "__main__":
    process_employee_data("employeeData.dat", "employeeDataProcessed.dat")
