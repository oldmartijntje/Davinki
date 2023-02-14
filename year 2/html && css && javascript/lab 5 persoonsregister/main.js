list = [{
    "voornaam": "Piet",
    "achternaam": "Heijn",
    "nationaliteit": "Nederlandse",
    "leeftijd": 47,
    "gewicht": 86
}];
selected = 0;

document.getElementById("show").addEventListener("click", myFunction);

function myFunction() {
    document.getElementById('voornaam').innerHTML = list[selected]["voornaam"];
    document.getElementById('achternaam').innerHTML = list[selected]["achternaam"];
    document.getElementById('nationaliteit').innerHTML = list[selected]["nationaliteit"];
    document.getElementById('leeftijd').innerHTML = list[selected]["leeftijd"];
    document.getElementById('gewicht').innerHTML = list[selected]["gewicht"];
    document.getElementById('show').hidden = true;
}