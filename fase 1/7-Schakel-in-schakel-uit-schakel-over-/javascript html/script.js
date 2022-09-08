function myFunction(values) {
    function compact(values, onOrOff, consoleLog, color, buttonText){
      values[0] = onOrOff;
      console.log(consoleLog);
      document.body.style.backgroundColor = color;
      btn.innerHTML = buttonText;
      return values
    }
    if (values[0] == "on")  
    {
      compact(values, 'off', 'The light has been turned off', 'black', 'Turn The Light On')
    }
    else if (values[0] == "off")  
    {
      compact(values, 'on', 'The light has been turned on', 'yellow', 'Turn The Light Off')
    }
    /*
    values[1] += 1
    if (values[1] > 15){
      window.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ', '_blank').focus();
    }
    */
    return values
  }

var btn = document.createElement('button');
btn.style.margin = '10px';
btn.innerHTML = 'Turn The Light On';
document.body.appendChild(btn);

  
// schijf hier tussen je code
document.body.style.backgroundColor = "black";
var values = ["off", 0];
var button = document.querySelector('button');
button.onclick = function() {
  //do stuff
  values = myFunction(values)
}

// schijf hier tussen je code