angular.module('myApp')
  .controller('categoryCtrl', ['$scope', '$http', '$location', '$routeParams',
    function($scope, $http, $location, $routeParams){
        console.log('Category Controller called.')
        $http.get('/api/category/category_details/' +$routeParams.category_id +'/').success(function(data){
        $scope.category = data["product"]

    });
}]);
