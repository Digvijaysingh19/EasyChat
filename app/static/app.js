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
  // $locationProvider.hashPrefix('!');
  $routeProvider.when('/chat', {
  	templateUrl: 'components/chat/chat.html',
    // controller: 'AppCtrl'
    controller: 'contact-list'
  })
  .when('/', {
    template: 'blank',
    controller: 'index-controller'
  })
  // .otherwise({redirectTo: '/view1'});
});
// var sd = angular.module('MyApp', ['ngMaterial'])
//   .controller('AppCtrl', function ($scope, $mdSidenav) {
//     $scope.toggleLeft = buildToggler('left');

//     function buildToggler(componentId) {
//       return function() {
//         $mdSidenav(componentId).toggle();
//       };
//     }
//   });


