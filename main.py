from mean_var_std import calculate

try:
    # Example input to test the function
    result = calculate([0, 1, 2, 3, 4, 5, 6, 7, 8])
    print(result)  # Print the result dictionary
except ValueError as e:
    print(e)  # Print the error message if the input list is invalid

