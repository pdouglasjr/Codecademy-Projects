# Name:     gradebook/script.py
# Author:   Phillip Douglas

last_semester_gradebook = [("politics", 80), ("latin", 96), ("dance", 97), ("architecture", 65)]

# List of subjects
subjects = ["physics", "calculus", "poetry", "history"]

# List of grades
grades = [98, 97, 85, 88]

# Add Computer Science grade of 100
subjects += ["computer science"]
grades += [100]

# Add Visual Arts grade of 93
subjects += ["visual arts"]
grades += [93]

# Zip subjects and grades into a gradebook
gradebook = zip(subjects, grades)

# Print gradebook
print(f"Gradebook: {list(gradebook)}")

# Add last semester gradebook to current gradebook
gradebook = list(zip(subjects, grades)) + last_semester_gradebook

# Print updated gradebook
print(f"Updated Gradebook: {gradebook}")