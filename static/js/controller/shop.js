angular.module('myApp')
  .controller('shopCtrl', ['$scope', '$http', '$location', function($scope, $http, $location){
    $http.defaults.headers.post["Content-Type"] = "application/x-www-form-urlencoded";
    $http.get('/api/product/').success(function(data)
    {
        $scope.products = data;
    });

}]);
