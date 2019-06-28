'use strict';

// Declare app level module which depends on views, and core components
var app = angular.module('myApp', [
  'ngRoute',
  'ngMaterial',
  'ngAnimate', 
  'ngAria'
])
app.config(function($locationProvider, $routeProvider) {
  $locationProvider.hashPrefix('!');
  $routeProvider.when('/chat', {
  	templateUrl: 'components/chat/chat.html',
    // controller: 'AppCtrl'
    controller: 'contact-list'
  })
  // .when('/', {
  // 	template: 'blank'
  // })
  // .otherwise({redirectTo: '/view1'});
});
