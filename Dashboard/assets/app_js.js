// Disable right-click and call a function
document.addEventListener('contextmenu', function(event) {
  event.preventDefault(); // Prevent the default context menu
  myFunction(); // Call your function

});


// Your function to be called when right-click is disabled
function myFunction() {
//  alert('Right-click is disabled on this page!');
  showCoords(event);
};
//function myFunction1() {
//  alert('left-click is disabled on this page!');
//};

// Mouse position

function showCoords(event) {
  let x = event.clientX;
  let y = event.clientY;
  let text = "X coords: " + x + ", Y coords: " + y;
  alert(text);
}


//function printMousePos() {
//    var cursorX;
//    var cursorY;
//    document.onmousemove = function(e){
//    cursorX = e.pageX;
//    cursorY = e.pageY;
//    alert("mouse position");
//};










