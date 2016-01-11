(function () {
    var bol = angular.module('bolSide', ['ngResource']);
    bol.config(['$locationProvider', function ($locationProvider) {
        $locationProvider.html5Mode({
            enabled: true,
            requireBase: false
        });
    }]);
    bol.config(['$resourceProvider', function ($resourceProvider) {
        // Don't strip trailing slashes from calculated URLs
        $resourceProvider.defaults.stripTrailingSlashes = false;
    }]);
    bol.controller('BolCtrl', ['$scope', '$resource', '$location', function ($scope, $resource, $location) {
        var rest = $resource('/static/bol.json');
        $scope.varer = [];
        rest.query(function (data) {
            $scope.varer = data;
        });
        $scope.varefilter = $location.search();
        if ($scope.varefilter.kategori && !Array.isArray($scope.varefilter.kategori))$scope.varefilter.kategori = [$scope.varefilter.kategori];
        if (!$scope.varefilter.sortering) $scope.varefilter.sortering = "alkoholpris";

        $scope.$watch('varefilter', function (newValue, oldValue) {
            $location.search(newValue);
        }, true);

        $scope.changeSort = function (value) {
            if ($scope.varefilter.sortering === value) $scope.varefilter.sortering = '-' + value;
            else $scope.varefilter.sortering = value;
        };
        $scope.sortStatus = function (value) {
            if ($scope.varefilter.sortering === value) return '-asc';
            if ($scope.varefilter.sortering.substring(1) === value) return '-desc';
            return '';
        };

        $scope.systembolaget = function (url) {
            window.open('http://www.systembolaget.se/dryck/' + url);
        };
        $scope.kategoriToggle = function (kategori) {
            if ($scope.varefilter.kategori) {
                var i = $scope.varefilter.kategori.indexOf(kategori);
                if (i === -1) {
                    $scope.varefilter.kategori.push(kategori);
                } else {
                    $scope.varefilter.kategori.splice(i, 1);
                    if ($scope.varefilter.kategori.length === 0) delete $scope.varefilter.kategori;
                }
            } else {
                $scope.varefilter.kategori = [kategori];
            }
        };
        $scope.kategoriSelected = function (kategori) {
            return ($scope.varefilter.kategori && $scope.varefilter.kategori.indexOf(kategori) === -1 ? '' : '-check');
        };

        $scope.kategorier = [
            "ol",
            "sprit",
            "aperitif-dessert",
            "mousserande-viner",
            "roda-viner",
            "cider-och-blanddrycker",
            "vita-viner",
            "alkoholfritt",
            "roseviner"
        ]

    }]);
    bol.filter('bolFilter', function () {
        return function (items, filterData) {
            if (filterData == undefined)
                return items;

            var keys = Object.keys(filterData);
            var filtered = [];
            var populate = false;

            var nameFilter = new RegExp(filterData['navn'], 'i');
            var landFilter = new RegExp(filterData['land'], 'i');
            var produsentFilter = new RegExp(filterData['produsent'], 'i');


            for (var i = 0; i < items.length; i++) {
                populate = false;
                var item = items[i];

                if (filterData.kategori && item.kategori !== filterData.kategori) {
                    for (var j = 0; j < filterData.kategori.length; j++) {
                        if (item.kategori === filterData.kategori[j]) {
                            populate = true;
                        }
                    }
                } else {
                    populate = true;
                }

                if (filterData['navn'] && item['navn'].search(nameFilter) === -1) {
                    continue;
                }
                if (filterData['land'] && item['land'].search(landFilter) === -1) {
                    continue;
                }
                if (filterData['produsent'] && item['produsent'].search(produsentFilter) === -1) {
                    continue;
                }

                if (filterData['pris_min'] && item['pris'] < filterData['pris_min']) {
                    continue;
                }
                if (filterData['pris_maks'] && item['pris'] > filterData['pris_maks']) {
                    continue;
                }
                if (filterData['volum_min'] && item['volum'] < filterData['volum_min']) {
                    continue;
                }
                if (filterData['volum_maks'] && item['volum'] > filterData['volum_maks']) {
                    continue;
                }
                if (filterData['alkohol_min'] && item['alkohol'] < filterData['alkohol_min']) {
                    continue;
                }
                if (filterData['alkohol_maks'] && item['alkohol'] > filterData['alkohol_maks']) {
                    continue;
                }
                if (filterData['alkoholpris_min'] && item['alkoholpris'] < filterData['alkoholpris_min']) {
                    continue;
                }
                if (filterData['alkoholpris_maks'] && item['alkoholpris'] > filterData['alkoholpris_maks']) {
                    continue;
                }

                if (populate) {
                    filtered.push(item);
                }
            }
            return filtered;
        };
    });
    bol.directive('toNumber', function () {
        return {
            require: 'ngModel',
            link: function (scope, elem, attrs, ctrl) {
                ctrl.$parsers.push(function (value) {
                    if (!isNaN(parseFloat(value)) && isFinite(value)) return value;

                    return '';
                });
            }
        };
    });
})();