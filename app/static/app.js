'use strict';

// Declare app level module which depends on views, and core components
var app = angular.module('myApp', [
  'ngRoute',
  'ngMaterial',
  'ngAnimate', 
  'ngAria'
])
.controller('AppCtrl', function ($scope, $mdSidenav) {
    $scope.toggleLeft = buildToggler('left');
    function buildToggler(componentId) {
      return function() {
        $mdSidenav(componentId).toggle();
      };
    }
  });

app.config(function($locationProvider, $routeProvider) {
  $routeProvider.when('/', {
  	templateUrl: 'components/chat/chat.html',
    controller: 'contact-list'
  })
});