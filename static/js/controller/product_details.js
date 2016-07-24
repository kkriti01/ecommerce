angular.module('myApp')
  .controller('productdetailsControllers', ['$scope', '$http', '$location','$routeParams','$rootScope',  function($scope, $http, $location, $routeParams, $rootScope){
        $http.get('/api/product/' +$routeParams.product_id + '/').success(function(data)
        {
        $scope.product = data
        });



}]);
