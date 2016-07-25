angular.module('myApp')
  .controller('productdetailsControllers', ['$scope', '$http', '$location','$routeParams','$rootScope',  function($scope, $http, $location, $routeParams, $rootScope){
        $http.get('/api/product/' +$routeParams.product_id + '/').success(function(data)
        {
        $scope.product = data
        });


    $rootScope.remove_cart_item = function(item_id) {
        $http({
                url: '/cart/remove_item/',
                method: "POST",
                data: $.param({
                    'item_id': item_id
                })
            })
            .then(function(response) {
                    $rootScope.cart_items = response.data.items;
                    $rootScope.cart_item_count = response.data.items.length;
                    $rootScope.price= 0;
                    for(i in response.data.items){
                        price += response.data.items[i].price;
                    }
                    $rootScope.cart_total_price = price
                },
                function(response) {
                    console.log('failed');
                });
    };

}]);
