var games = [
    {
        "title": "Counter-Strike: Global Offensive",
        "price": 0.00,
        "genre": "FPS",
        "rating": 4
    },
    {
        "title": "Dota 2",
        "price": 0.00,
        "genre": "MOBA",
        "rating": 3
    },
    {
        "title": "Goose Goose Duck",
        "price": 4.99,
        "genre": "Action",
        "rating": 2
    },
    {
        "title": "Apex Legends",
        "price": 0.00,
        "genre": "FPS",
        "rating": 4
    },
    {
        "title": "PUBG: BATTLEGROUNDS",
        "price": 29.99,
        "genre": "FPS",
        "rating": 5
    },
    {
        "title": "Lost Ark",
        "price": 49.99,
        "genre": "Action",
        "rating": 1
    },
    {
        "title": "Grand Theft Auto V",
        "price": 29.99,
        "genre": "FPS",
        "rating": 3
    },
    {
        "title": "Call of Duty®: Modern Warfare® II | Warzone™ 2.0",
        "price": 19.99,
        "genre": "FPS",
        "rating": 3
    },
    {
        "title": "Team Fortress 2",
        "price": 0.00,
        "genre": "FPS",
        "rating": 5
    },
    {
        "title": "Rust",
        "price": 39.99,
        "genre": "Action",
        "rating": 5
    },
    {
        "title": "Unturned",
        "price": 0.00,
        "genre": "RPG",
        "rating": 1
    },
    {
        "title": "ELDEN RING",
        "price": 59.99,
        "genre": "RPG",
        "rating": 5
    },
    {
        "title": "ARK: Survival Evolved",
        "price": 10.00,
        "genre": "RPG",
        "rating": 1
    },
    {
        "title": "War Thunder",
        "price": 0.00,
        "genre": "Simulation",
        "rating": 2
    },
    {
        "title": "Sid Meier's Civilization VI",
        "price": 29.99,
        "genre": "Simulation",
        "rating": 3
    },
    {
        "title": "Football Manager 2023",
        "price": 59.99,
        "genre": "Simulation",
        "rating": 3
    },
    {
        "title": "Warframe",
        "price": 0.00,
        "genre": "Looter-shooter",
        "rating": 3
    },
    {
        "title": "EA SPORTS™ FIFA 23",
        "price": 59.99,
        "genre": "Sport",
        "rating": 1
    },
    {
        "title": "Destiny 2",
        "price": 0.00,
        "genre": "FPS",
        "rating": 5
    },
    {
        "title": "Red Dead Redemption 2",
        "price": 59.99,
        "genre": "RPG",
        "rating": 4
    },
    {
        "title": "Tom Clancy's Rainbow Six Siege",
        "price": 19.99,
        "genre": "Simulation",
        "rating": 3
    },
    {
        "title": "The Witcher 3: Wild Hunt",
        "price": 39.99,
        "genre": "RPG",
        "rating": 4
    },
    {
        "title": "Terraria",
        "price": 9.99,
        "genre": "Sandbox",
        "rating": 2
    },
    {
        "title": "Stardew Valley",
        "price": 14.99,
        "genre": "Sandbox",
        "rating": 1
    },
    {
        "title": "Left 4 Dead 2",
        "price": 9.99,
        "genre": "FPS",
        "rating": 4
    },
    {
        "title": "Don't Starve Together",
        "price": 5.09,
        "genre": "RPG",
        "rating": 3
    },
    {
        "title": "MIR4",
        "price": 19.99,
        "genre": "RPG",
        "rating": 3
    },
    {
        "title": "PAYDAY 2",
        "price": 9.99,
        "genre": "Action",
        "rating": 2
    },
    {
        "title": "Path of Exile",
        "price": 0.00,
        "genre": "RPG",
        "rating": 4
    },
    {
        "title": "Project Zomboid",
        "price": 14.99,
        "genre": "Simulation",
        "rating": 4
    },
    {
        "title": "Valheim",
        "price": 19.99,
        "genre": "Sandbox",
        "rating": 5
    },
    {
        "title": "Muck",
        "price": 0.00,
        "genre": "Action",
        "rating": 6
    },
    {
        "title": "Minecraft Java Edition",
        "price": 25.00,
        "genre": "Sandbox",
        "rating": 8
    },
    {
        "title": "Minecraft windows 10 edition",
        "price": 30.00,
        "genre": "Sandbox",
        "rating": 7
    },
    {
        "title": "Minecraft Bedrock Edition",
        "price": 7.00,
        "genre": "Sandbox",
        "rating": 8
    },
    {
        "title": "Crush Crush",
        "price": 0.00,
        "genre": "Simulation",
        "rating": 6
    },
    {
        "title": "Fortnite",
        "price": 0.00,
        "genre": "Action",
        "rating": 6
    },
    {
        "title": "Among us",
        "price": 9.00,
        "genre": "Action",
        "rating": 7
    },
    {
        "title": "Subway Surfers",
        "price": 0.00,
        "genre": "Simulation",
        "rating": 5
    },
    {
        "title": "Roblox",
        "price": 0.00,
        "genre": "Action,Sandbox,Simulation,FPS,RPG,Looter-shooter,Sport",
        "rating": 7
    },
    {
        "title": "DayZ",
        "price": 44.99,
        "genre": "Simulation",
        "rating": 3
    }
]
ActiveGenreFilter = '';

function myFunction() {
    document.getElementById("myDropdown").classList.toggle("show");
}

// Close the dropdown if the user clicks outside of it
window.onclick = function (event) {
    if (!event.target.matches('.dropbtn')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        var i;
        for (i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.classList.contains('show')) {
                openDropdown.classList.remove('show');
            }
        }
    }
}

function filterThis(filter) {
    ActiveGenreFilter = filter;
    console.log(ActiveGenreFilter);
}

gameList = [];
for (let i = 0; i < games.length; i++) {
    var gameRow = document.createElement("div");
    gameRow.classList.add("game", "row");
    var game = document.createElement("div");
    game.classList.add("gameInfo", "space_between", "border", "fancy-background", "width");
    var cartButton = document.createElement("button");
    cartButton.dataset.value = "Add to cart";
    cartButton.innerText = "Add to cart";
    cartButton.classList.add("smallWidth", "border", "fancy-background", "magic");
    cartButton.id = games[i].title;
    var gameName = document.createElement("p");
    var gameGenre = document.createElement("p");
    var gameRating = document.createElement("p");
    var gamePrice = document.createElement("p");
    gameName.innerText = games[i].title;
    gameName.dataset.value = gameName.innerText;
    gameGenre.innerText = games[i].genre;
    gameGenre.dataset.value = gameGenre.innerText;
    gameRating.innerText = `${games[i].rating}/5`;
    gameRating.dataset.value = gameRating.innerText;
    if (games[i].price == 0) {
        gamePrice.innerText = "Free";
    } else {
        gamePrice.innerText = "$" + games[i].price;
    }
    gamePrice.dataset.value = gamePrice.innerText;
    gameName.classList.add("margin", "name", "quarterWidth", "magic");
    gameGenre.classList.add("margin", "genre", "quarterWidth", "magic");
    gameRating.classList.add("margin", "rating", "quarterWidth", "magic");
    gamePrice.classList.add("margin", "price", "quarterWidth", "magic");
    cartButton.onclick = function () {
        console.log(this.id);
    };
    game.appendChild(gameName);
    game.appendChild(gameGenre);
    game.appendChild(gameRating);
    game.appendChild(gamePrice);
    gameRow.appendChild(cartButton);
    gameRow.appendChild(game);
    document.getElementById("gameList").appendChild(gameRow);
}

function cartGame(game) {

}

const letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890";
const ignore = ' ';
const elements = document.getElementsByClassName("magic");
for (let i = 0; i < elements.length; i++) {
    elements[i].addEventListener("mouseover", event => {
        let iterations = 0;
        const interval = setInterval(() => {
            event.target.innerText = event.target.innerText.split("").map((letter, index) => {
                if (index < iterations) {
                    return event.target.dataset.value[index].toUpperCase();
                }
                if (ignore.indexOf(event.target.dataset.value[index]) >= 0) {
                    return event.target.dataset.value[index].toUpperCase();
                }
                return letters[Math.floor(Math.random() * 35)];
            }).join("");
            if (iterations >= event.target.dataset.value.length) clearInterval(interval)
            iterations += 1 / 3;
        }, 30);
    });
}