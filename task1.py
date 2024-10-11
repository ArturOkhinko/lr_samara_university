def processed_list():
    counts_days = [3, 5, 7, 4, 4, 9, 6, 5]
    new_count_day = 10
    count_element_for_delete = 2

    print_extreme_days(counts_days)
    avarage_dosage_medication(counts_days)
    counts_days.append(new_count_day)
    del counts_days[:count_element_for_delete]
    counts_days = remove_every_second(counts_days)

def print_extreme_days(counts_days):
    message = f'Минимальный курс: {min(counts_days)}, а максимальный курс: {max(counts_days)}.'
    print(message)

def avarage_dosage_medication(counts_days):
    sum = 0
    for count_day in counts_days:
        sum += count_day
    
    avarage_value = sum / len(counts_days)
    return avarage_value

def remove_every_second(counts_days):
    return [value for index, value in enumerate(counts_days) if index % 2 == 0]

processed_list()