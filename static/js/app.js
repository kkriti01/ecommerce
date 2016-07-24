"use strict";

var myApp = angular.module('myApp', ['ngRoute']);

myApp.config(function($interpolateProvider ,$httpProvider){
         $httpProvider.defaults.xsrfCookieName = 'csrftoken';
         $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';
        $interpolateProvider.startSymbol('{/');
        $interpolateProvider.endSymbol('/}');
    });

myApp.config(['$routeProvider',
  function($routeProvider) {
    $routeProvider
      .when('/', {
        templateUrl: '/static/partials/shop.html',
        controller: 'shopCtrl'
      })
       .when('/category/category_items/:category_id/', {
        templateUrl: '/static/partials/category_items.html',
        controller: 'categoryCtrl'
      })
      .when('/product/product_items/:product_id/', {
        templateUrl: '/static/partials/products_details.html',
        controller: 'productdetailsControllers'
      })
      .otherwise({
       redirectTo: '/'
     });
  }]);

