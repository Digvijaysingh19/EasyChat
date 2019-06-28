     var aa = angular.module('a', ['ngMaterial'])

/* When the user clicks on the button, 
toggle between hiding and showing the dropdown content */
function myFunction() {
  document.getElementById("myDropdown").classList.toggle("show");
}

// Close the dropdown if the user clicks outside of it
window.onclick = function(event) {
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
// Dropdown end
// contact list js
app.controller('contact-list',function($scope,$http){
  $http.get('/handlers/chat').then(function(response){
    $scope.contacts = response.data; 
    })
});
// contact list end
// message send controller
app.controller('sendtext',function($scope,$http){
  // $http.get('/handlers/chat').then(function(response){
  //   $scope.contacts = response.data; 
  //   })
});



