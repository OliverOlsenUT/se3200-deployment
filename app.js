const serverURL = window.location.protocol === 'file:' 
? "http://localhost:8080" // local url for development
: ""; // prod url
console.log("connected");
let inputGameName = document.querySelector("#input-game-name");
let inputGameGenres = document.querySelector("#input-game-genres");
let inputGameReview = document.querySelector("#input-game-review");
let inputGameCost = document.querySelector("#input-game-cost");
let inputGameEsrb = document.querySelector("#input-game-esrb");
let cancelReviewButton = document.querySelector("#cancel-review-button");
let saveReviewButton = document.querySelector("#save-review-button");
let editId = null;
let gameViewWrapper = document.querySelector("section");

function saveReview() {
    // prep data to send to server;
    let data = "name=" + encodeURIComponent(inputGameName.value) +
        "&genres=" + encodeURIComponent(inputGameGenres.value) +
        "&cost=" + encodeURIComponent(inputGameCost.value) +
        "&esrb_rating=" + encodeURIComponent(inputGameEsrb.value) +
        "&review=" + encodeURIComponent(inputGameReview.value);
    console.log(data);
    cancelReviewButton.style.visibility = "hidden";
    let url = serverURL + "/games";
    let method = "POST";
    if (editId) {
        url += "/" + editId;
        method = "PUT";
        console.log(editId);
        document.querySelector("#game" + editId).scrollIntoView();
    }
    // send value to server
    fetch(url,
        {
            method: method,
            body: data,
            headers: {
                "Content-Type": "application/x-www-form-urlencoded"
            }
        }
    ).then(function (response) {
        console.log("done", response);
        clear();
        fetch_games();
    });
}

function addGameReview(obj) {
    let gameName = document.createElement("h2");
    gameName.textContent = obj["name"];
    gameName.id = "game"+ obj["id"];
    let gameGenres = document.createElement("h3");
    gameGenres.textContent = "Genres: " + obj["genres"] + ". Cost: $" + 
        obj.cost + ". Rated " + obj.esrb_rating + ".";
    let gameReview = document.createElement("p");
    gameReview.textContent = obj["review"];

    let editButton = document.createElement("button");
    editButton.textContent = "Edit";
    let deleteButton = document.createElement("button");
    deleteButton.textContent = "Delete";
    gameViewWrapper.appendChild(gameName);
    gameViewWrapper.appendChild(gameGenres);
    gameViewWrapper.appendChild(gameReview);
    gameViewWrapper.appendChild(editButton);
    gameViewWrapper.appendChild(deleteButton);

    deleteButton.onclick = function() {
        if (confirm("Are you sure you want to delete " + obj.name +"?"))
        {
            console.log(serverURL + "/games/" + obj.id);
            fetch(serverURL + "/games/" + obj.id,
                {
                    method: "DELETE"
                }
            ).then(function (response) {
                console.log("done", response);
                fetch_games();
                if (editId == obj.id) {
                    clear();
                }
            });
        }
    }

    editButton.onclick = function () {
        console.log(obj);
        inputGameName.value = obj.name;
        inputGameGenres.value = obj.genres;
        inputGameReview.value = obj.review;
        inputGameCost.value = obj.cost;
        inputGameEsrb.value = obj.esrb_rating;
        editId = obj.id;
        cancelReviewButton.style.visibility = "visible";
        inputGameName.scrollIntoView();
        fetch_games();
    }
}

function fetch_games() {
    fetch(serverURL + "/games")
        .then(function (response) {
            response.json()
                .then(function (data) {
                    gameViewWrapper.innerHTML = "";
                    console.log(data);
                    let recommendedGames = data;
                    recommendedGames.forEach(addGameReview);
                })
        });

}

cancelReviewButton.onclick = clear;
saveReviewButton.onclick = saveReview;
fetch_games();

function clear() {
    inputGameName.value = "";
    inputGameGenres.value = "";
    inputGameReview.value = "";
    inputGameEsrb.value = "E";
    inputGameCost.value = "";
    cancelReviewButton.style.visibility = "hidden";
    editId = null;
}