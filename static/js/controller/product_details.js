angular.module('myApp')
  .controller('product_detailsCtrl', ['$scope', '$http', '$location', '$routeParams',
    function($scope, $http, $location, $routeParams){
           $http.get('/api/product/' +$routeParams.product_id + '/').success(function(data)
    {
        $scope.product = data
    });
    $scope.add_to_cart = function(item_id)
    {
      $http({
        url: '/cart/',
        method: "POST",
        data: $.param({
            'item_id': item_id
        }),
        headers: {'Content-Type': 'application/x-www-form-urlencoded'}
      }).then(function(response)
      {
         console.log('success');
          $scope.cart_items = response.data.items;
                    $scope.cart_item_count = response.data.items.length;
                    var price = 0;
                    for(i in response.data.items){
                        price += response.data.items[i].price;
                    }
                    $scope.cart_total_price = price;
     }, function(response)
     {
        console.log('failed');
      });
    };
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

    $scope.discard_cart = function(item_id) {
        $http({
                url: '/cart/discard_cart/',
                method: "POST",
                data: $.param({
                    'item_id': item_id
                })
            })
            .then(function(response) {
                    $scope.cart_items = 0;
                    $scope.cart_item_count = 0;
                    $scope.cart_total_price = 0.0;
                },
                function(response) {
                    console.log('failed');
                });
    };

    $scope.remove_cart_item = function(item_id) {
        $http({
                url: '/cart/remove_item/',
                method: "POST",
                data: $.param({
                    'item_id': item_id
                })
            })
            .then(function(response) {
                    $scope.cart_items = response.data.items;
                    $scope.cart_item_count = response.data.items.length;
                    var price = 0;
                    for(i in response.data.items){
                        price += response.data.items[i].price;
                    }
                    $scope.cart_total_price = price
                },
                function(response) {
                    console.log('failed');
                });
    };
}]);
