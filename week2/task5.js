function find(spaces, stat, n) {
    // # Extract car indices of 1 to an array
    const availableCarIndexArray = stat
        .map((car, index) => (car == 1 ? index : -1))
        .filter((index) => index != -1);

    // # Extract available spaces to an array based on car indices
    let availableSpacesArray = [];
    for (let spaceIndex in spaces) {
        let availableSpaces = spaces[spaceIndex];
        for (let carIndex of availableCarIndexArray) {
            if (spaceIndex == carIndex) {
                availableSpacesArray.push(availableSpaces);
            }
        }
    }

    // # Find the most fitted car
    let statOfFound = "";
    let spaceDifferenceArray = [];
    let theMostFittedCarIndex;
    for (let spaces of availableSpacesArray) {
        if (spaces == n) {
            statOfFound = "Found Exact Spaces";
            index = availableSpacesArray.indexOf(spaces);
            theMostFittedCarIndex = availableCarIndexArray[index];
            break;
        } else if (spaces > n) {
            statOfFound = "Found";
            let spaceDifference = spaces - n;
            spaceDifferenceArray.push(spaceDifference);
        } else if (spaces < n) {
            statOfFound = "Not Found";
        }
    }

    // # Print car index based on stat of found
    if (statOfFound == "Found Exact Spaces") {
        console.log(theMostFittedCarIndex);
    } else if (statOfFound == "Found") {
        let minSpaceDifference = Math.min(...spaceDifferenceArray);
        let index = spaceDifferenceArray.indexOf(minSpaceDifference);
        theMostFittedCarIndex = availableCarIndexArray[index];
        console.log(theMostFittedCarIndex);
    } else if (statOfFound == "Not Found") {
        console.log(-1);
    }
}

console.log("----------------------- Task 5 -----------------------");
find([3, 1, 5, 4, 3, 2], [0, 1, 0, 1, 1, 1], 2); // print 5
find([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4); // print -1
find([4, 6, 5, 8], [0, 1, 1, 1], 4); // print 2
