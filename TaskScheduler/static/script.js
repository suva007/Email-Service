
document.addEventListener('DOMContentLoaded',function(event){
    // array with texts to type in typewriter
    var dataText = [ "Meowww!!.", "I am a Reminder Cat.", "I will notify you about your events", "Just fill in the information below"];
    
    // type one text in the typwriter
    // keeps calling itself until the text is finished
    function typeWriter(text, i, fnCallback) {
      // check if text isn't finished yet
      if (i < (text.length)) {
        // add next character to h1
       document.querySelector("h1").innerHTML = text.substring(0, i+1) +'<span aria-hidden="true"></span>';
  
        // wait for a while and call this function again for next character
        setTimeout(function() {
          typeWriter(text, i + 1, fnCallback)
        }, 100);
      }
      // text finished, call callback if there is a callback function
      else if (typeof fnCallback == 'function') {
        // call callback after timeout
        setTimeout(fnCallback, 700);
      }
    }
    // start a typewriter animation for a text in the dataText array
     function StartTextAnimation(i) {
       if (typeof dataText[i] == 'undefined'){
          setTimeout(function() {
            StartTextAnimation(0);
          }, 20000);
       }
       // check if dataText[i] exists
      if (i < dataText[i].length) {
        // text exists! start typewriter animation
       typeWriter(dataText[i], 0, function(){
         // after callback (and whole text has been animated), start next text
         StartTextAnimation(i + 1);
       });
      }
    }
    // start the text animation
    StartTextAnimation(0);
  });

// Input validation:
function checkInput() {
  var validRegex = /^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/;
  let email = document.forms["myForm"]["myInput"].value;
  let subject = document.forms["myForm"]["myInput1"].value;
  let description = document.forms["myForm"]["myInput2"].value;
  let date = document.forms["myForm"]["date"].value;
  if (email == "") {
    alert("Email must be filled out");
    return false;
  }
  if (subject == "") {
    alert("Subject must be filled out");
    return false;
  }
  if (description == "") {
    alert("Description must be filled out");
    return false;
  }
  if (date == "") {
    alert("Date must be filled out");
    return false;
  }
  var p2 = "<p style='color:green' text-align: right;>Processing!!!</p>";
  document.getElementById("p1").insertAdjacentHTML('beforebegin', p2);
}