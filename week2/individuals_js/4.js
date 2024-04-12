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

getNumber(1); // print 4
getNumber(5); // print 15
getNumber(10); // print 25
getNumber(30); // print 70
