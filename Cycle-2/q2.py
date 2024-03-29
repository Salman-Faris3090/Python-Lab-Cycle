def rotateRight(lst,k):
    k=k%len(lst)
    return lst[-k:]+lst[:-k]

def main():
    # Step 1:Convert to list of integers
    num_str = input("Enter a string of numbers separated by spaces: ")
    num_list = list(map(int, num_str.split()))

    # Step 2:Rotate elements in the list by k position to the right
    k = int(input("Enter the number of positions to rotate the list to the right: "))
    rotated_list = rotateRight(num_list, k)
    print(f"Rotated List ({k} positions to the right): {rotated_list}")

    # Step 3: Convert the list into a tuple using list comprehension
    num_tuple = tuple([x for x in rotated_list])
    print(f"List converted to tuple: {num_tuple}")

    # Step 4: Remove all duplicates from the tuple and convert it into a list again
    unique_list = list(set(num_tuple))
    print(f"List with duplicates removed: {unique_list}")

    # Step 5: Create another list by putting the results of the evaluation of the function f(x) = x^2 - x with each element in the final list
    def f(x):
        return x**2 - x
    result_list = [f(x) for x in unique_list]
    print(f"List after applying function f(x) = x^2 - x: {result_list}")

    # Step 6: Sort both lists and merge them to create a single sorted list
    sorted_list1 = sorted(unique_list)
    sorted_list2 = sorted(result_list)
    merged_list = sorted_list1 + sorted_list2
    print(f"Merged and sorted list: {merged_list}")

if __name__ == '__main__':
    main()