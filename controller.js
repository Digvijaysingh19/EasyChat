var app = angular.module('MainApp',[ ]);
app.controller('people',function($scope,$http)
{
    $http.get('http://127.0.0.1:8887/database.json')
.success(function(response){
$scope.persons=response.records; 
});
});