// ----------------------- Task 1 ----------------------- //
const messages = {
    Bob: "I'm at Ximen MRT station.",
    Mary: "I have a drink near Jingmei MRT station.",
    Copper: "I just saw a concert at Taipei Arena.",
    Leslie: "I'm at home near Xiaobitan station.",
    Vivian: "I'm at Xindian station waiting for you.",
};

function findAndPrint(messages, currentStation) {
    // # Extract names and messages into two separate arrays
    const nameArray = Object.keys(messages);
    const messageArray = nameArray.map((key) => {
        return messages[key];
    });

    const greenLine = {
        Songshan: 0,
        "Nanjing Sanmin": 1,
        "Taipei Arena": 2,
        "Nanjing Fuxing": 3,
        "Songjiang Nanjing": 4,
        Zhongshan: 5,
        Beimen: 6,
        Ximen: 7,
        Xiaonanmen: 8,
        "Chiang Kai-Shek Memorial Hall": 9,
        Guting: 10,
        "Taipower Building": 11,
        Gongguan: 12,
        Wanlong: 13,
        Jingmei: 14,
        Dapinglin: 15,
        Qizhang: 16,
        Xiaobitan: 15.5,
        "Xindian City Hall": 17,
        Xindian: 18,
    };

    // # Extract stations to an array
    const greenLineStationArray = Object.keys(greenLine);
    // # Extract station values to an array
    const greenLineNumArray = greenLineStationArray.map((key) => {
        return greenLine[key];
    });

    // # Find current station index from green line station array
    const currentStationIndex = greenLineStationArray.indexOf(currentStation);
    // # Find current station value based on the current station index
    const currentStationNum = greenLineNumArray[currentStationIndex];

    let distanceArray = [];
    let sameStation = false;
    let friendAtSameStation;

    for (let message of messageArray) {
        for (let station of greenLineStationArray) {
            if (message.includes(station)) {
                // # Find which message and station (index)
                const messageIndex = messageArray.indexOf(message);
                const stationIndex = greenLineStationArray.indexOf(station);

                let stationNum = 0;
                let distance = 0;

                // # Set different values for "Xiaobitan" based on the current station
                if (station == "Xiaobitan" && stationIndex < 16) {
                    stationNum = 16.5;
                } else if (station == "Xiaobitan" && stationIndex > 16) {
                    stationNum = 15.5;
                } else {
                    stationNum = greenLineNumArray[stationIndex];
                }

                // # Calculate distance
                if (stationNum > currentStationNum) {
                    distance = stationNum - currentStationNum;
                    distanceArray.push(distance);
                } else if (stationNum < currentStationNum) {
                    distance = currentStationNum - stationNum;
                    distanceArray.push(distance);
                } else if (stationNum == currentStationNum) {
                    sameStation = true;
                    friendAtSameStation = nameArray[messageIndex];
                }
            }
        }
    }

    // # Find the minimum distance and print the name
    if (sameStation) {
        console.log(friendAtSameStation);
    } else {
        const minDistance = Math.min(...distanceArray);
        const minDistanceIndex = distanceArray.indexOf(minDistance);
        const theNearestFriend = nameArray[minDistanceIndex];
        console.log(theNearestFriend);
    }
}

console.log("----------------------- Task 1 -----------------------");
findAndPrint(messages, "Wanlong"); // print Mary
findAndPrint(messages, "Songshan"); // print Copper
findAndPrint(messages, "Qizhang"); // print Leslie
findAndPrint(messages, "Ximen"); // print Bob
findAndPrint(messages, "Xindian City Hall"); // print Vivian

// ----------------------- Task 2 ----------------------- //

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

console.log("----------------------- Task 2 -----------------------");
book(consultants, 15, 1, "price"); // Jenny
book(consultants, 11, 2, "price"); // Jenny
book(consultants, 10, 2, "price"); // John
book(consultants, 20, 2, "rate"); // John
book(consultants, 11, 1, "rate"); // Bob
book(consultants, 11, 2, "rate"); // No Service
book(consultants, 14, 3, "price"); // John

// ----------------------- Task 3 ----------------------- //

function func(...data) {
    // # Extract each middle name out to an array
    let middleNameList = [];
    let middleName;
    for (let fullname of data) {
        if (fullname.length == 2 || fullname.length == 3) {
            middleName = fullname[1];
            middleNameList.push(middleName);
        } else if (fullname.length == 4 || fullname.length == 5) {
            middleName = fullname[2];
            middleNameList.push(middleName);
        }
    }

    // # Find the unique middle name from the array above
    const uniqueMiddleName = findUniqueMiddleName(middleNameList);

    // # Print the fullname with unique middle name
    if (uniqueMiddleName != "") {
        let uniqueMiddleNameIndex = middleNameList.indexOf(uniqueMiddleName);
        console.log(data[uniqueMiddleNameIndex]);
    } else {
        console.log("沒有");
    }
}

const findUniqueMiddleName = (myList) => {
    let middleNames = myList.join("");
    let middleNameCounts = {};

    for (let name of middleNames) {
        if (middleNameCounts[name]) {
            middleNameCounts[name]++;
        } else {
            middleNameCounts[name] = 1;
        }
    }

    let uniqueMiddleName = "";

    for (let name in middleNameCounts) {
        if (middleNameCounts[name] == 1) {
            uniqueMiddleName = name;
        }
    }

    return uniqueMiddleName;
};

console.log("----------------------- Task 3 -----------------------");
func("彭大牆", "陳王明雅", "吳明"); // print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花"); // print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花"); // print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆"); // print 夏曼藍波安

// ----------------------- Task 4 ----------------------- //

function getNumber(index) {
    let numList = [];

    for (let i = 0; i < index * 4; i++) {
        if (i % 7 == 0) {
            numList.push(i);
            numList.push(i + 4);
            numList.push(i + 8);
        }
    }

    console.log(numList[index]);
}

console.log("----------------------- Task 4 -----------------------");
getNumber(1); // print 4
getNumber(5); // print 15
getNumber(10); // print 25
getNumber(30); // print 70
