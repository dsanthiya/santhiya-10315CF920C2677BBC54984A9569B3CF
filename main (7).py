'''
Implement a function called sort_students that takes a list of student objects as input and sorts the 
list based on their CGPA (Cumulative Grade point Average) in descending order. Each student object
has the following attributes: name (string), roll_number (string), and cgpa (float). Test the function
with different input lists of students.
'''

class Student:

  def __init__(self, name,roll_number, cgpa):
    self.name = name
    self.roll_number = roll_number
    self.cgpa = cgpa


def sort_students(student_list):
  # Sort the list of students in descending order of CGPA
  sorted_students = sorted(student_list, 
                           key=lambda student: student.cgpa,
                           reverse=True)
  return sorted_students


# Example usage:
students = [
    student("Hari", "A123", 7.8),