# sectiona A question 1(i)

def rectangle_area(length,width):
    area = length * width
    return area
print(rectangle_area(6,3))


# question1(11) given


numbers = [ 3, 8, 5, 10, 14]

sum_of_evens = 0

for numbers in numbers:
    
        sum_of_evens += numbers

print("Sum of even numbers:", sum_of_evens)


# question 1(iii)

def numbers(num1, num2, num3):
 
    numbers = [num1, num2, num3]

    total_sum = sum(numbers)

    
    largest_num = max(numbers)
    smallest_num = min(numbers)

   
    return total_sum, largest_num, smallest_num


sum_value, large_value, small_value = numbers(10, 4, 7)

print(f"The numbers are: 10, 4, 7")
print(f"Sum: {sum_value}")
print(f"Largest: {large_value}")
print(f"Smallest: {small_value}")


# Question1(iii) 
student_record = {"name": "Grace Nakato", "score": 95, "grade": "B", "school": "WITI"}
print(student_record)

