function start() {
    alert("Start");
}
function test(){
    alert("Test");
}

// Refresh the div with id div1 inside the div with id div-wrapper each x miliseconds

window.setInterval(function(){
var url = 'index.php'; //url of the page we are currently executing the code         
$('#div1-wrapper').load(url + ' #div1'); //note: the space before #div1 is very important
}, 120000);

/*
$(window).load(function () {

  $("#div2").endlessScroll({ 
      width: '100%', 
      height: '300px', 
      steps: -1, 
      speed: 10, 
      mousestop: false 
  });
      $("#div3").endlessScroll({ 
      width: '100%', 
      height: '900px', 
      steps: -1, 
      speed: 10, 
      mousestop: false 
  });
      $("#testa").endlessScroll({ 
      width: '10%', 
      height: '20px', 
      steps: -1, 
      speed: 10, 
      mousestop: false 
  });
  // Recopy the previous line to add scrolling to other divs.

});
*/

