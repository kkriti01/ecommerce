myApp.controller('checkoutCtrl', ['$scope', '$http', '$location', function($scope, $http, $location) {
    $('#cartModal').modal('hide');
    $(".navbar-default").hide();
    $('body').removeClass('modal-open');
    $('.modal-backdrop').remove();
    $scope.submit = function() {
        console.log('submitted');
        console.log($scope.checkout.name, $scope.checkout.email);
        $http({
                url: '/checkout/',
                method: "POST",
                data: $.param({
                    'name': $scope.checkout.name,
                    'email': $scope.checkout.email,
                    'mobile': $scope.checkout.mobile,
                    'address': $scope.checkout.address,
                    'city': $scope.checkout.city,
                    'state': $scope.checkout.state,
                    'pin': $scope.checkout.pin,
                    'payment_option': $scope.checkout.payment_option
                })
            })
            .then(function(response) {
                    console.log(response);
                    console.log('hellos');
                    $scope.cart_items = 0;
                    $scope.cart_item_count = 0;
                    $scope.cart_total_price = 0;
                    alert('Order was sucessfull!')
                    $location.url('/');
                    console.log('failed to route!')
                },
                function(response) {
                    console.log('failed');
                });
    }
}]);
