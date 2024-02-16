
def record_yield(yield_records):
    cow_id = input("Enter the 3-digit identity code of the cow: ")
    yield_amount = float(input("Enter the yield in litres upto one decimal place "))
    if cow_id not in yield_records:
        yield_records[cow_id] = []
    yield_records[cow_id].append(yield_amount)


def calculate_statistics(yield_records):
    total_volume = 0
    total_cows = 0
    for cow_id, yields in yield_records.items():
        total_volume += sum(yields)
        total_cows += 1
    average_yield = total_volume / total_cows
    return round(total_volume), round(average_yield)


def identify_cows(yield_records):
    most_productive_cow = max(yield_records, key=lambda x: sum(yield_records[x]))
    low_volume_cows = [cow_id for cow_id, yields in yield_records.items() if len([yield_amount for yield_amount in yields if yield_amount < 12]) >= 4]
    return most_productive_cow, low_volume_cows


def main():
    yield_records = {}

    # TASK 1 
    for _ in range(14):
        record_yield(yield_records)

    # TASK 2
    total_volume, average_yield = calculate_statistics(yield_records)
    print("Total weekly volume of milk for the herd:", total_volume, "litres")
    print("Average yield per cow in a week:", average_yield, "litres")

    # TASK 3
    most_productive_cow, low_volume_cows = identify_cows(yield_records)
    print("Most productive cow this week:", most_productive_cow)
    if low_volume_cows:
        print("Cows producing less than 12 litres for four or more days this week:", low_volume_cows)
    else:
        print("No cows producing less than 12 litres for four or more days this week.")

if __name__ == "__main__":
    main()
