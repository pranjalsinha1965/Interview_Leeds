def sum_of_elements(arr):
    return sum(arr)

def find_largest_smallest(arr):
    if len(arr) == 0:
        return None, None
    else:
        return max(arr), min(arr)

def calculate_average(arr):
    if len(arr) == 0:
        return None
    else:
        return sum(arr) / len(arr)

def reverse_array(arr):
    return arr[::-1]

def copy_array(arr):
    return arr.copy()

def remove_duplicates(arr):
    return list(set(arr))
    
def calculate_frequency(arr):
    freq_dict = {}
    for num in arr:
        if num in freq_dict:
            freq_dict[num] += 1
        else:
            freq_dict[num] = 1
    return freq_dict

def separate_even_odd(arr):
    even = [num for num in arr if num % 2 == 0]
    odd = [num for num in arr if num % 2 != 0]
    return even, odd           

def search_element(arr, element):
    if element in arr:
        return arr.index(element)
    else:
        return -1

# Example usage
array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print("Sum of elements:", sum_of_elements(array))
largest, smallest = find_largest_smallest(array)
print("Largest element:", largest)
print("Smallest element:", smallest)
print("Average of elements:", calculate_average(array))
print("Reversed array:", reverse_array(array))
copied_array = copy_array(array)
print("Copied array:", copied_array)
print("Array with duplicates removed:", remove_duplicates(array))
print("Frequency of elements:", calculate_frequency(array))
even, odd = separate_even_odd(array)
print("Even numbers:", even)
print("Odd numbers:", odd)
element_to_search = 5
index = search_element(array, element_to_search)
if index != -1:
    print("Element", element_to_search, "found at index:", index)
else:
    print("Element", element_to_search, "not found in the array.")
