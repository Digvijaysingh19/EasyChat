app.controller('contact-list',function($scope,$http){
  $http.get('/handlers/chat').then(function(response){
    $scope.contacts = response.data; 
    })
});