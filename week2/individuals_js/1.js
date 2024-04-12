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

findAndPrint(messages, "Wanlong"); // print Mary
findAndPrint(messages, "Songshan"); // print Copper
findAndPrint(messages, "Qizhang"); // print Leslie
findAndPrint(messages, "Ximen"); // print Bob
findAndPrint(messages, "Xindian City Hall"); // print Vivian
