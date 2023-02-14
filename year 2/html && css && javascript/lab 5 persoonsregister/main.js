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
selected = 0;
document.getElementById("error").hidden = true;

document.getElementById("show").addEventListener("click", myFunction);

function myFunction() {
    value = document.getElementById("number").value;
    console.log(value)
    if (isNaN(value) || value < 0 || value > 6 || value == "") {
        document.getElementById("error").hidden = false;
    } else {
        document.getElementById("error").hidden = true;
        selected = Number(value);
        document.getElementById('voornaam').innerHTML = list[selected]["voornaam"];
        document.getElementById('achternaam').innerHTML = list[selected]["achternaam"];
        document.getElementById('nationaliteit').innerHTML = list[selected]["nationaliteit"];
        document.getElementById('leeftijd').innerHTML = list[selected]["leeftijd"];
        document.getElementById('gewicht').innerHTML = list[selected]["gewicht"];
    }


}