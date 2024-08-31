
def bubble_sort(arr):
    """Sorts an array using the Bubble Sort algorithm."""
    length = len(arr)
    for i in range(length - 1):
        for j in range(length - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

def calculate_column_averages(marks):
    """
    Calculates the average score for each column (subject) in the marks matrix
    and sorts the averages.
    
    Args:
        marks (list of list of int): 2D list where each row represents a student's
                                     scores in different subjects.

    Returns:
        None
    """
    num_rows = len(marks)
    num_cols = len(marks[0])
    
    # Initialize lists to store column sums and averages
    column_sums = [0] * num_cols
    column_averages = [0] * num_cols

    # Calculate sums for each column
    for j in range(num_cols):
        for i in range(num_rows):
            column_sums[j] += marks[i][j]

    # Calculate averages and print them
    for j in range(num_cols):
        column_averages[j] = column_sums[j] / num_rows
        print(f'Total average for subject {j + 1} is {column_averages[j]:.2f}')

    # Sort the averages and print the sorted list
    bubble_sort(column_averages)
    print("Sorted averages:", column_averages)

# Example matrix with 5 rows and 5 columns
marks = [
    [34, 34, 56, 34, 32],
    [78, 56, 78, 98, 56],
    [65, 67, 45, 87, 34],
    [45, 65, 34, 76, 32],
    [56, 34, 67, 35, 78]
]

calculate_column_averages(marks)




























# def BubbleSort(A,l):
#     for i in range(1,l,1):
#         for j in range(0,l-i,1):
#             if(A[j]>A[j+1]):
#                 A[j],A[j+1]=A[j+1],A[j]

# def col_sum(marks):
#     savg=[0 for i in range(5)]
#     merit=[0 for i in range(5)]
#     for j in range(5):
#         for i in range(5):
#             savg[j]=savg[j]+marks[i][j]
#     for j in range(5):
#         print('Total average of student',i+1,'is',savg[j]/5)
#         merit[j]=savg[j]/5

#     BubbleSort(merit,5)
#     print(merit)

# marks=[[34,34,56,34,32],[78,56,78,98,56],[65,67,45,87,34],[45,65,34,76,32],[56,34,67,35,78],[67,45,87,56,34]]
# col_sum(marks)