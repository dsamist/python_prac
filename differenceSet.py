
# Read the input
num_english = int(input())
english_students = set(map(int, input().split()))
num_french = int(input())
french_students = set(map(int, input().split()))

# Find the students who have subscribed to only English newspapers
only_english_students = english_students - french_students

# Print the total number of students who have subscribed to only English newspapers
print(len(only_english_students))


#code for asymmetric difference, that is, the elements that are in either of the sets but not in both
english_or_french = english_students.symmetric_difference(french_students)
