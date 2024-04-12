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

func("彭大牆", "陳王明雅", "吳明"); // print 彭大牆
console.log("-----------------------------------");
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花"); // print 林花花
console.log("-----------------------------------");
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花"); // print 沒有
console.log("-----------------------------------");
func("郭宣雅", "夏曼藍波安", "郭宣恆"); // print 夏曼藍波安
