# process_data.py

import csv
import sys
from utils import calculate_average, assign_grade

def process_grades():
    if len(sys.argv) < 2:
        print("Usage: python main.py <input_file>")
        return

    input_file = sys.argv[1]
    output_file = 'student_results.csv'
    students = []

    try:
        with open(input_file, 'r') as file:
            reader = csv.reader(file)
            next(reader)  #skip the geader row
            for row in reader:
                if len(row) != 4:
                    continue  # skip rows that do not have 4 elements
                name, math, science, english = row
                try:
                    scores = [int(math), int(science), int(english)]
                    average = calculate_average(scores)
                    grade = assign_grade(average)
                    students.append([name, average, grade])
                except ValueError:
                    print(f"Invalid scores for {name}, skipping.")

        with open(output_file, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Name', 'Average', 'Grade'])
            writer.writerows(students)

        print(f"Results saved to {output_file}")

    except FileNotFoundError:
        print(f"Error: File '{input_file}' not found.")
