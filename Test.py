def check_criterion(lst, criterion):
    # The 'all()' function will check if all elements in the list meet the criterion
    if all(element > criterion for element in lst):
        # Your code here - this block will only execute if all elements meet the criterion
        print("All elements in the list meet the criterion.")
    else:
        # This block will execute if at least one element does not meet the criterion
        print("Not all elements in the list meet the criterion.")

# Example usage:
my_list = [10, 15, 20, 25, 30]
criterion_value = 5
check_criterion(my_list, criterion_value)