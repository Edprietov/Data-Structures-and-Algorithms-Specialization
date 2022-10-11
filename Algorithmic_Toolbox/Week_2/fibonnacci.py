
def calculate_fibonnacci(fibonnacci_number_to_calculate):
    fibonnacci_numbers = []
    index = 2
    if (fibonnacci_number_to_calculate == 1) or (fibonnacci_number_to_calculate == 0):
           return fibonnacci_number_to_calculate
    else:
        fibonnacci_numbers.append(0)
        fibonnacci_numbers.append(1)
        while index < fibonnacci_number_to_calculate:
            fibonnacci_numbers.append(fibonnacci_numbers[index-1] + fibonnacci_numbers[index-1])
            index += 1
        return fibonnacci_numbers[fibonnacci_number_to_calculate-1]
