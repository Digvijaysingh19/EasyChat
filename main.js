var myApp = angular.module("myList",[]);
myApp.controller("myListController", function ($scope) {
   $scope.item = ["AngularJS","ReactJS","UnderscoreJS"]; 
   $scope.newitem = "" ;

});