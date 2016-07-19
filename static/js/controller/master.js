angular.module('myApp')
  .controller('MasterControllers', ['$scope', '$http', '$location', function($scope, $http, $location){
        console.log('Master controller loaded.');
        $http.get('/api/category/').success(function(data){
        $scope.category = data
    });
    $http.get('/cart/').success(function(data)
    {
        $scope.cart_items = data.items;
        $scope.cart_item_count = data.items.length;
         console.log($scope.cart_items);
        var price= 0;
        for(i in data.items){
            price += data.items[i].price;
        }
        $scope.cart_total_price = price;

    });

}]);
