myApp.controller('MasterControllers', ['$scope', '$http', '$location','$routeParams','$rootScope', function($scope, $http, $location, $routeParams, $rootScope){
    $rootScope.products = [];
    $rootScope.cart_total_price = 0.0;
    $rootScope.cart_items = [];
    $rootScope.cart_item_count = 0;

    $http.get('/api/category/').success(function(data)
    {
        $scope.category = data
    });
    $rootScope.add_to_cart = function(item_id)
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
        $('#myModal').modal('show');
        console.log('success');
        $rootScope.cart_items = response.data.items;
        $rootScope.cart_item_count = response.data.items.length;
        var price = 0;
        for(i in response.data.items){
            price += response.data.items[i].price;
        }
        $rootScope.cart_total_price = price;
     }, function(response)
     {
        console.log('failed');
      });
    };
    $rootScope.discard_cart = function(item_id) {
        $http({
                url: '/cart/discard_cart/',
                method: "POST",
                data: $.param({
                    'item_id': item_id
                })
            })
            .then(function(response) {
                    $rootScope.cart_items = 0;
                    $rootScope.cart_item_count = 0;
                    $rootScope.cart_total_price = 0.0;
                },
                function(response) {
                    console.log('failed');
                });
    };

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

    $http.get('/cart/').success(function(data)
    {
        $rootScope.cart_items = data.items;
        $rootScope.cart_item_count = data.items.length;
        console.log($scope.cart_items);
        var price= 0;
        for(i in data.items)
        {
            price += data.items[i].price;
        }
        $rootScope.cart_total_price = price;
    });

}]);



