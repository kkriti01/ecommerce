angular.module('myApp')
  .controller('shopCtrl', ['$scope', '$http', '$location', function($scope, $http, $location){
    console.log('Shop Controller loaded');
    $scope.products = [];
    $scope.cart_total_price = 0.0;
    $scope.cart_items = [];
    $scope.cart_item_count = 0;

    $http.defaults.headers.post["Content-Type"] = "application/x-www-form-urlencoded";
    $http.get('/api/product/').success(function(data)
    {
        $scope.products = data;
    });
    $http.get('/api/category/').success(function(data)
    {
        $scope.category = data
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
