const consultants = [
    { name: "John", rate: 4.5, price: 1000 },
    { name: "Bob", rate: 3, price: 1200 },
    { name: "Jenny", rate: 3.8, price: 800 },
];

let bookedTimesByPrice = {};
let bookedTimesByRate = {};

function book(consultants, hour, duration, criteria) {
    // # Re-arrange the consultants based on price (lowest --> highest)
    const prices = consultants.map((consultant) => consultant["price"]);
    const sortedPrices = prices.slice().sort((a, b) => {
        return a - b;
    });
    const sortedConsultantsByPrice = sortedPrices.flatMap((price) =>
        consultants.filter((consultant) => consultant.price == price)
    );
    // # Extract the names from sorted consultants by price
    const namesByPrice = sortedConsultantsByPrice.map(
        (consultant) => consultant["name"]
    );
    // # Create an object for storing booked times (if not done yet)
    // # based on the order of sorted consultants by price
    // # key: name, value: array of booked times (hours)
    if (Object.keys(bookedTimesByPrice).length == 0) {
        for (let i = 0; i < sortedConsultantsByPrice.length; i++) {
            bookedTimesByPrice[namesByPrice[i]] = [];
        }
    }

    // #Re-arrange the consultants based on rate (highest --> lowest)
    const rates = consultants.map((consultant) => consultant["rate"]);
    const sortedRates = rates.slice().sort((a, b) => {
        return b - a;
    });
    const sortedConsultantsByRate = sortedRates.flatMap((rate) =>
        consultants.filter((consultant) => consultant.rate == rate)
    );
    // # Extract the names from sorted consultants by rate
    const namesByRate = sortedConsultantsByRate.map(
        (consultant) => consultant["name"]
    );
    // # Create an object for storing booked times (if not done yet)
    // # based on the order of sorted consultants by rate
    // # key: name, value: array of booked times (hours)
    if (Object.keys(bookedTimesByRate).length == 0) {
        for (let i = 0; i < sortedConsultantsByRate.length; i++) {
            bookedTimesByRate[namesByRate[i]] = [];
        }
    }

    // # Store requested times in an array based on hour & duration
    let requestedTimes = [];
    let time = hour;
    requestedTimes.push(time);

    if (duration > 1) {
        for (let i = 0; i < duration - 1; i++) {
            time += 1;
            requestedTimes.push(time);
        }
    }

    // # Check if the requested time slot is available based on price or rate
    let availability = false;
    let availableConsultant;

    if (criteria == "price") {
        for (let key in bookedTimesByPrice) {
            let value = bookedTimesByPrice[key];

            // # Check if there is common elements between booked times and requested times
            let bookedTimesSet = new Set(value);
            let requestedTimesSet = new Set(requestedTimes);

            for (let num of requestedTimesSet) {
                if (bookedTimesSet.has(num)) {
                    availability = false;
                    // Break if any of requested times is unavailable
                    break;
                } else {
                    availability = true;
                }
            }

            // # Break once found an available consultant
            if (availability == true) {
                availableConsultant = key;
                break;
            }
        }

        if (availability == true) {
            console.log(availableConsultant);
            bookedTimesByPrice[availableConsultant].push(...requestedTimes);
            bookedTimesByRate[availableConsultant].push(...requestedTimes);
        } else {
            console.log("No Service");
        }
    } else if (criteria == "rate") {
        for (let key in bookedTimesByRate) {
            let value = bookedTimesByRate[key];

            // # Check if there is common elements between booked times and requested times
            let bookedTimesSet = new Set(value);
            let requestedTimesSet = new Set(requestedTimes);

            for (let num of requestedTimesSet) {
                if (bookedTimesSet.has(num)) {
                    availability = false;
                    break;
                } else {
                    availability = true;
                }
            }

            if (availability == true) {
                availableConsultant = key;
                break;
            }
        }

        if (availability == true) {
            console.log(availableConsultant);
            bookedTimesByRate[availableConsultant].push(...requestedTimes);
            bookedTimesByPrice[availableConsultant].push(...requestedTimes);
        } else {
            console.log("No Service");
        }
    }
}

book(consultants, 15, 1, "price"); // Jenny
console.log("-----------------------");
book(consultants, 11, 2, "price"); // Jenny
console.log("-----------------------");
book(consultants, 10, 2, "price"); // John
console.log("-----------------------");
book(consultants, 20, 2, "rate"); // John
console.log("-----------------------");
book(consultants, 11, 1, "rate"); // Bob
console.log("-----------------------");
book(consultants, 11, 2, "rate"); // No Service
console.log("-----------------------");
book(consultants, 14, 3, "price"); // John
