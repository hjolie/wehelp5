const contentContainer = document.getElementById("content-container");
const spotContainer3 = document.getElementById("spot-container-3-columns");
const spotContainer10 = document.getElementById("spot-container-10-columns");
const loadMoreBtn = document.getElementById("load-more-btn");
const loadMoreContainer = document.createElement("div");
loadMoreContainer.id = "load-more-container";

function createPromotionItems(className, text, index) {
    const promotionItem = document.createElement("div");
    promotionItem.className = `promotion-item ${className}`;

    const promotionImage = document.createElement("div");
    promotionImage.className = "promotion-image";
    promotionImage.style.backgroundImage = `url(${spotImageArray[index]})`;

    const promotionText = document.createElement("p");
    promotionText.textContent = text;

    promotionItem.appendChild(promotionImage);
    promotionItem.appendChild(promotionText);

    return promotionItem;
}

function createTitleItems(className, text, index) {
    const titleItem = document.createElement("div");
    titleItem.className = `title-item ${className}`;

    const titleImage = document.createElement("div");
    titleImage.className = "title-image";
    titleImage.style.backgroundImage = `url(${spotImageArray[index]})`;

    const starIconContainer = document.createElement("div");
    starIconContainer.className = "star-icon";
    const starIcon = document.createElement("i");
    starIcon.className = "fas fa-star";
    starIconContainer.appendChild(starIcon);

    const titleText = document.createElement("p");
    titleText.textContent = text;

    titleItem.appendChild(titleImage);
    titleItem.appendChild(starIconContainer);
    titleItem.appendChild(titleText);

    return titleItem;
}

function createLoadMoreItems(text, index) {
    const titleItem = document.createElement("div");
    titleItem.className = "title-item";

    const titleImage = document.createElement("div");
    titleImage.className = "title-image";
    titleImage.style.backgroundImage = `url(${spotImageArray[index]})`;

    const starIconContainer = document.createElement("div");
    starIconContainer.className = "star-icon";
    const starIcon = document.createElement("i");
    starIcon.className = "fas fa-star";
    starIconContainer.appendChild(starIcon);

    const titleText = document.createElement("p");
    titleText.textContent = text;

    titleItem.appendChild(titleImage);
    titleItem.appendChild(starIconContainer);
    titleItem.appendChild(titleText);

    return titleItem;
}

// ---------------------------------------------------------------- //

let spotTitleArray = [];
let spotImageArray = [];

function getData() {
    fetch(
        "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
    )
        .then((response) => {
            return response.json();
        })
        .then((data) => {
            for (let i = 0; i < data.data.results.length; i++) {
                let spotTitle = data.data.results[i].stitle;
                let spotImages = data.data.results[i].filelist;
                const regexPattern = /https:\/\/[^\s]+?\.(jpg|jpeg|JPG)/;
                const match = spotImages.match(regexPattern);
                const firstImageUrl = match[0];
                spotTitleArray.push(spotTitle);
                spotImageArray.push(firstImageUrl);
            }

            for (let i = 1; i < 4; i++) {
                const promotionClassName = `promotion${i}`;
                const promotionText = spotTitleArray[i - 1];
                spotContainer3.appendChild(
                    createPromotionItems(
                        promotionClassName,
                        promotionText,
                        i - 1
                    )
                );
            }

            for (let i = 1; i < 11; i++) {
                const titleClassName = `title${i}`;
                const titleText = spotTitleArray[i + 2];

                // Grid 442 for < 1200px
                spotContainer10.appendChild(
                    createTitleItems(titleClassName, titleText, i + 2)
                );
                // Grid 444 for < 1200px - currently not displayed
                loadMoreContainer.appendChild(
                    createLoadMoreItems(titleText, i + 2)
                );
            }
        });
}

getData();

// ---------------------------------------------------------------- //

let currentItemCount = 13;

loadMoreBtn.addEventListener("click", () => {
    loadMoreBtn.style.display = "none";
    spotContainer10.style.display = "none"; //Switch grid from 442 to 444 for < 1200px

    for (let i = currentItemCount; i < currentItemCount + 10; i++) {
        if (i > spotTitleArray.length - 1) {
            loadMoreBtn.style.display = "none";
            break;
        } else {
            const titleText = spotTitleArray[i];

            contentContainer.appendChild(loadMoreContainer); //Containing the initial 10 columns
            loadMoreContainer.appendChild(createLoadMoreItems(titleText, i)); //the next 10 columns

            contentContainer.appendChild(loadMoreBtn);
            loadMoreBtn.style.display = "block";
        }
    }
    currentItemCount += 10;
});
