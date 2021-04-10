var portfolioApp = angular.module('portfolioApp',[]);

portfolioApp.controller('GalleryListCtrl', function($scope)
{
    $scope.galleries = 
    [
        { 'title':'Supra MK4',
        'when':'10-06-1999',
        'thumbnailUrl':'img/1.jpg'
        },
        { 'title':'Charger 70',
        'when':'02-07-1970',
        'thumbnailUrl':'img/2.jpg'
        },
        { 'title':'488 Pista',
        'when':'12-09-2019',
        'thumbnailUrl':'img/3.jpg'
        },
        { 'title':'DB 11',
        'when':'15-06-2018',
        'thumbnailUrl':'img/4.jpg'
        },
        { 'title':'Chellanger Hellcat Redeye',
        'when':'24-08-2020',
        'thumbnailUrl':'img/5.jpg'
        },
        { 'title':'S4 b6',
        'when':'23-05-2003',
        'thumbnailUrl':'img/5.png'
        }
    ];
    $scope.galleries.length;
});