list = [{
    "voornaam": "Piet",
    "achternaam": "Heijn",
    "nationaliteit": "Nederlandse",
    "leeftijd": 47,
    "gewicht": 86
},
{
    "voornaam": "Masud",
    "achternaam": "Mohammed",
    "nationaliteit": "Iraans",
    "leeftijd": 37,
    "gewicht": 79
},
{
    "voornaam": "Marie",
    "achternaam": "Visser",
    "nationaliteit": "Belgische",
    "leeftijd": 42,
    "gewicht": 69
},
{
    "voornaam": "Abdullah",
    "achternaam": "Öcalan",
    "nationaliteit": "Turks",
    "leeftijd": 73,
    "gewicht": 85
},
{
    "voornaam": "Bjorn",
    "achternaam": "Hakke",
    "nationaliteit": "Zweeds",
    "leeftijd": 18,
    "gewicht": 71
},
{
    "voornaam": "Jouke",
    "achternaam": "Dijkstra",
    "nationaliteit": "Fries",
    "leeftijd": 29,
    "gewicht": 82
},
{
    "voornaam": "Bo",
    "achternaam": "Wáng",
    "nationaliteit": "Chinees",
    "leeftijd": 38,
    "gewicht": 65
}];
divList = [];

for (let index = 0; index < list.length; index++) {
    var person = document.createElement("div");
    person.classList.add("Person");
    divList.push(person);
    document.createElement("p");

    for (let indexx = 0; indexx < Object.keys(list[index]).length; indexx++) {
        var label = document.createElement("p");
        label.innerText = `${Object.keys(list[index])[indexx]}: ${list[index][Object.keys(list[index])[indexx]]}`;
        label.classList.add("text");
        divList[index].appendChild(label);
        document.getElementById("meow").appendChild(divList[index]);
    }
}
document.getElementById("show").addEventListener("click", myFunction);
function myFunction() {
    value = document.getElementById("value").value;
    for (let index = 0; index < divList.length; index++) {
        if (isNaN(value) || value == "") {
            divList[index].style.display = ""
        } else {
            if (list[index].leeftijd > Number(value)) {
                divList[index].style.display = ""
            } else {
                divList[index].style.display = "none"
            }
        }
    }
}
