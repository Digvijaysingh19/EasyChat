<<<<<<< HEAD
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
app.controller('contact-list',function($scope,$http)
{
  $scope.first_name = null;
  $scope.last_name = null;
  $scope.key = null;
  $scope.username = null;

  $scope.postData = function (first_name, last_name, key, username)
  {
    var data = {
      first_name : first_name,
      last_name : last_name,
      key : key,
      username : username
    };
    getData(data)
  }
  getDatafromDB().then(function (response){
    $scope.data = response.data;
  })
  // var contacts = {
  //   first_name : first_name,
  //   last_name : last_name,
  //   key : key,
  //   username : username
  // };
  function getDatafromDB() {
    return $http.get('/handlers/chat')
  }
});

// $http.get('/handlers/chat').then(function(response){
//   $scope.contacts = response.contacts;
// $scope.contacts = ["AngularJS","REactJs","Easychat"];
// function getDatafromDB() {
  // var pd
// }        $http.get('/chat').then(function(response){
                // $scope.contacts = response.data; 
                // console.log(respones\)
          //     })
          // });
=======
app.controller('contact-list',function($scope,$http){
  $http.get('/handlers/chat').then(function(response){
    $scope.contacts = response.data; 
    })
});
>>>>>>> 6562d182f44da79d9719bccb07f88fc86b075372
