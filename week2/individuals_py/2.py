consultants=[
    {"name":"John", "rate":4.5, "price":1000},
    {"name":"Bob", "rate":3, "price":1200},
    {"name":"Jenny", "rate":3.8, "price":800}
]

# --------------------------------------------------------------

booked_times_by_price = {}
booked_times_by_rate = {}

# --------------------------------------------------------------

def book(consultants, hour, duration, criteria):
    # Re-arrange the consultants based on price (lowest --> highest)
    prices = [consultant["price"] for consultant in consultants]
    sorted_prices = sorted(prices)
    sorted_consultants_by_price = [consultant for price in sorted_prices for consultant in consultants if consultant["price"] == price]

    # Extract the names from sorted consultants by price
    names_by_price = [consultant["name"] for consultant in sorted_consultants_by_price]

    # Create a dic for storing booked times (if not done yet)
    # based on the order of sorted consultants by price
    # key: name, value: list of booked times (hours)
    if booked_times_by_price == {}:
        for i in range(len(sorted_consultants_by_price)):
            booked_times_by_price[names_by_price[i]] = []

    #Re-arrange the consultants based on rate (highest --> lowest)
    rates = [consultant["rate"] for consultant in consultants]
    sorted_rates = sorted(rates, reverse=True)
    sorted_consultants_by_rate = [consultant for rate in sorted_rates for consultant in consultants if consultant["rate"] == rate]

    # Extract the names from sorted consultants by rate
    names_by_rate = [consultant["name"] for consultant in sorted_consultants_by_rate]

    # Create a dic for storing booked times (if not done yet)
    # based on the order of sorted consultants by rate
    # key: name, value: list of booked times (hours)
    if booked_times_by_rate == {}:
        for i in range(len(sorted_consultants_by_rate)):
            booked_times_by_rate[names_by_rate[i]] = []

    # Store requested times in a list based on hour & duration
    requested_times = []
    time = hour
    requested_times.append(time)
    if duration > 1:
        for i in range(duration - 1):
            time += 1
            requested_times.append(time)
    
    # Check if the requested time slot is available based on price or rate
    if criteria == "price":
        availability = True
        for key, value in booked_times_by_price.items():
            # Check if there is common elements between booked times and requested times
            booked_times_set = set(value)
            requested_times_set = set(requested_times)
            if booked_times_set.intersection(requested_times_set) == set():
                availability = True
                available_consultant = key
                break
            else:
                availability = False
        if availability == False:
            print("No Service")
        else:
            print(available_consultant)
            value.extend(requested_times)
            booked_times_by_rate[available_consultant].extend(requested_times)
    else:
        availability = True
        for key, value in booked_times_by_rate.items():
            # Check if there is common elements between booked times and requested times
            booked_times_set = set(value)
            requested_times_set = set(requested_times)
            if booked_times_set.intersection(requested_times_set) == set():
                availability = True
                available_consultant = key
                break
            else:
                availability = False
        if availability == False:
            print("No Service")
        else:
            print(available_consultant)
            value.extend(requested_times)
            booked_times_by_price[available_consultant].extend(requested_times)

# --------------------------------------------------------------

book(consultants, 15, 1, "price") # Jenny: 15, 16
print()
book(consultants, 11, 2, "price") # Jenny: 11, 12, 13
print()
book(consultants, 10, 2, "price") # John: 10, 11, 12
print()
book(consultants, 20, 2, "rate") # John: 20, 21, 22
print()
book(consultants, 11, 1, "rate") # Bob: 11, 12
print()
book(consultants, 11, 2, "rate") # No Service 11, 12, 13
print()
book(consultants, 14, 3, "price") # John: 14, 15, 16, 17