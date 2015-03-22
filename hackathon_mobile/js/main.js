/*
 * Google Maps documentation: http://code.google.com/apis/maps/documentation/javascript/basics.html
 * Geolocation documentation: http://dev.w3.org/geo/api/spec-source.html
 */
var defaultLatLng = new google.maps.LatLng(34.0983425, -118.3267434);  // Default to Hollywood, CA when no geolocation support
var map;
var myOptions;
var userMarker;
var userInfo;
var markers = [];
var colors = ['red', 'orange', 'green', 'yellow', 'purple'];
var markerColors = {
    red: null,
    blue: null,
    green: null,
    black: null
};
var ecoStyles = {
    good: [
        {
            "featureType": "administrative.country",
            "elementType": "labels",
            "stylers": [
                {
                    "visibility": "off"
                }
            ]
        },
        {
            "featureType": "administrative.province",
            "elementType": "labels",
            "stylers": [
                {
                    "visibility": "off"
                }
            ]
        },
        {
            "featureType": "administrative.locality",
            "elementType": "labels",
            "stylers": [
                {
                    "visibility": "off"
                }
            ]
        },
        {
            "featureType": "administrative.neighborhood",
            "elementType": "labels",
            "stylers": [
                {
                    "visibility": "off"
                }
            ]
        },
        {
            "featureType": "administrative.land_parcel",
            "elementType": "labels",
            "stylers": [
                {
                    "visibility": "off"
                }
            ]
        },
        {
            "featureType": "landscape",
            "elementType": "all",
            "stylers": [
                {
                    "visibility": "on"
                }
            ]
        },
        {
            "featureType": "landscape",
            "elementType": "labels",
            "stylers": [
                {
                    "visibility": "off"
                }
            ]
        },
        {
            "featureType": "landscape.man_made",
            "elementType": "geometry",
            "stylers": [
                {
                    "hue": "#C3E0B0"
                },
                {
                    "saturation": 23
                },
                {
                    "lightness": -12
                },
                {
                    "visibility": "simplified"
                }
            ]
        },
        {
            "featureType": "landscape.natural",
            "elementType": "geometry",
            "stylers": [
                {
                    "hue": "#7DC45C"
                },
                {
                    "saturation": 37
                },
                {
                    "lightness": -41
                },
                {
                    "visibility": "simplified"
                }
            ]
        },
        {
            "featureType": "poi",
            "elementType": "all",
            "stylers": [
                {
                    "hue": "#A19FA0"
                },
                {
                    "saturation": -98
                },
                {
                    "lightness": -20
                },
                {
                    "visibility": "off"
                }
            ]
        },
        {
            "featureType": "poi",
            "elementType": "labels",
            "stylers": [
                {
                    "visibility": "off"
                }
            ]
        },
        {
            "featureType": "road",
            "elementType": "all",
            "stylers": [
                {
                    "visibility": "off"
                }
            ]
        },
        {
            "featureType": "road",
            "elementType": "geometry",
            "stylers": [
                {
                    "hue": "#FFFFFF"
                },
                {
                    "saturation": -100
                },
                {
                    "lightness": 100
                },
                {
                    "visibility": "simplified"
                }
            ]
        },
        {
            "featureType": "transit",
            "elementType": "all",
            "stylers": [
                {
                    "visibility": "off"
                }
            ]
        },
        {
            "featureType": "water",
            "elementType": "geometry",
            "stylers": [
                {
                    "hue": "#71ABC3"
                },
                {
                    "saturation": -10
                },
                {
                    "lightness": -21
                },
                {
                    "visibility": "simplified"
                }
            ]
        }
    ],
    bad: [{
        "featureType": "water",
        "elementType": "geometry",
        "stylers": [{"color": "#ffdfa6"}]
    }, {
        "featureType": "landscape",
        "elementType": "geometry",
        "stylers": [{"color": "#b52127"}]
    }, {
        "featureType": "poi",
        "elementType": "geometry",
        "stylers": [{"color": "#c5531b"}]
    }, {
        "featureType": "road.highway",
        "elementType": "geometry.fill",
        "stylers": [{"color": "#74001b"}, {"lightness": -10}]
    }, {
        "featureType": "road.highway",
        "elementType": "geometry.stroke",
        "stylers": [{"color": "#da3c3c"}]
    }, {
        "featureType": "road.arterial",
        "elementType": "geometry.fill",
        "stylers": [{"color": "#74001b"}]
    }, {
        "featureType": "road.arterial",
        "elementType": "geometry.stroke",
        "stylers": [{"color": "#da3c3c"}]
    }, {
        "featureType": "road.local",
        "elementType": "geometry.fill",
        "stylers": [{"color": "#990c19"}]
    }, {
        "elementType": "labels.text.fill",
        "stylers": [{"color": "#ffffff"}]
    }, {
        "elementType": "labels.text.stroke",
        "stylers": [{"color": "#74001b"}, {"lightness": -8}]
    }, {
        "featureType": "transit",
        "elementType": "geometry",
        "stylers": [{"color": "#6a0d10"}, {"visibility": "on"}]
    }, {
        "featureType": "administrative",
        "elementType": "geometry",
        "stylers": [{"color": "#ffdfa6"}, {"weight": 0.4}]
    }, {"featureType": "road.local", "elementType": "geometry.stroke", "stylers": [{"visibility": "off"}]}],
    medium: [{
        "featureType": "water",
        "elementType": "geometry",
        "stylers": [{"color": "#ffdfa6"}]
    }, {
        "featureType": "landscape",
        "elementType": "geometry",
        "stylers": [{"color": "#b52127"}]
    }, {
        "featureType": "poi",
        "elementType": "geometry",
        "stylers": [{"color": "#c5531b"}]
    }, {
        "featureType": "road.highway",
        "elementType": "geometry.fill",
        "stylers": [{"color": "#74001b"}, {"lightness": -10}]
    }, {
        "featureType": "road.highway",
        "elementType": "geometry.stroke",
        "stylers": [{"color": "#da3c3c"}]
    }, {
        "featureType": "road.arterial",
        "elementType": "geometry.fill",
        "stylers": [{"color": "#74001b"}]
    }, {
        "featureType": "road.arterial",
        "elementType": "geometry.stroke",
        "stylers": [{"color": "#da3c3c"}]
    }, {
        "featureType": "road.local",
        "elementType": "geometry.fill",
        "stylers": [{"color": "#990c19"}]
    }, {
        "elementType": "labels.text.fill",
        "stylers": [{"color": "#ffffff"}]
    }, {
        "elementType": "labels.text.stroke",
        "stylers": [{"color": "#74001b"}, {"lightness": -8}]
    }, {
        "featureType": "transit",
        "elementType": "geometry",
        "stylers": [{"color": "#6a0d10"}, {"visibility": "on"}]
    }, {
        "featureType": "administrative",
        "elementType": "geometry",
        "stylers": [{"color": "#ffdfa6"}, {"weight": 0.4}]
    }, {"featureType": "road.local", "elementType": "geometry.stroke", "stylers": [{"visibility": "off"}]}],
    neutral: []
};
function drawMap(latlng) {
    myOptions = {
        styles: ecoStyles.neutral,
        zoom: 20, //23
        center: latlng,
        mapTypeId: google.maps.MapTypeId.ROADMAP,
        zIndex: 1,
        scrollwheel: false,
        navigationControl: false,
        mapTypeControl: false,
        scaleControl: false,
        draggable: false,
        streetViewControl: false,
        zoomControl: false,
        mapTypeControlOptions: {
            mapTypeIds: [google.maps.MapTypeId.ROADMAP, 'good', google.maps.MapTypeId.ROADMAP,
                'bad', google.maps.MapTypeId.ROADMAP, 'medium']
        }

    };

    map = new google.maps.Map(document.getElementById("map-canvas"), myOptions);

    // Add an overlay to the map of current lat/lng
    userMarker = new google.maps.Marker({
        position: latlng,
        map: map,
        title: "This is you!"
    });

    var good = new google.maps.StyledMapType(
        ecoStyles.good, myOptions);
    map.mapTypes.set('good', good);
    var bad = new google.maps.StyledMapType(
        ecoStyles.bad, myOptions);
    map.mapTypes.set('bad', bad);
    var medium = new google.maps.StyledMapType(
        ecoStyles.medium, myOptions);
    map.mapTypes.set('medium', medium);
}
function appSetLocation(lat, long) {
    var location = new google.maps.LatLng(lat, long);
    userMarker.setPosition(location);
    map.setCenter(location)

}
function getUserStats() {
    $.ajax({
        url: "http://backend.mediahackday.gehekt.nl/api/v1.0/user/1/?format=json",
        method: "GET",
        data: {},
        cache: false,
        dataType: 'json'
    }).done(function (user) {
        userInfo = user;
        var position = user.previous_known_position;
        appSetLocation(position.latitude, position.longitude);


    });

}

function switchTheme(rating) {
    map.setMapTypeId(rating);

}
function createMarkers(nearByUsers) {

    for (var i = 0; i < nearByUsers.length; i++) {

        var user = nearByUsers[i];
        var userId = user.id;
        var position = user.previous_known_position;
        var userLocation = new google.maps.LatLng(position.latitude, position.longitude);
        var username = user.username;
        var image = 'img/bender-small.jpg';
        if (markers[userId] == undefined) {
            markers[userId] = new google.maps.Marker({
                map: map,
                position: userLocation,
                title: username,
                icon: image,
                user: user
            });
            google.maps.event.addListener(markers[userId], 'click', function () {
                userMenu(markers[userId].user);
            });
        }

    }
}
function getNearbyUsers(lat, long) {

    $.ajax({
        url: "http://backend.mediahackday.gehekt.nl/api/v1.0/nearby-cars?format=json",
        method: "GET",
        data: {},
        cache: false,
        dataType: 'json'
    }).done(function (info) {

        createMarkers(info);

    });


}
function isLoggedIn() {

}
function userMenu(user) {
    console.log(user);
    $('.menu__bottom').addClass('open');
    $('.reply-menu').attr('data-id', user.id);


}
function sendMessage(user, msg) {
    $.ajax({
        url: "test.json",
        method: "POST",
        data: {user: user, msg: msg},
        cache: false,
        dataType: 'json'
    }).done(function () {
        alert('message send');

    });
}
function checkForNotifications() {
    $.ajax({
        url: "test.json",
        method: "POST",
        data: {user: user},
        cache: false,
        dataType: 'json'
    }).done(function () {
        getLastNotifications();
    });
}
function getLastNotifications() {
    $.ajax({
        url: "test.json",
        method: "POST",
        data: {user: user},
        cache: false,
        dataType: 'json'
    }).done(function () {
        getLastMessage();
    });
}


$(document).on("pageinit", "#map-page", function () {


    if (navigator.geolocation) {
        function success(pos) {
            // Location found, show map with these coordinates
            drawMap(new google.maps.LatLng(pos.coords.latitude, pos.coords.longitude));
        }

        function fail(error) {
            drawMap(defaultLatLng);  // Failed to find location, show default map
        }

        // Find the users current position.  Cache the location for 5 minutes, timeout after 6 seconds
        navigator.geolocation.getCurrentPosition(success, fail, {
            maximumAge: 500000,
            enableHighAccuracy: true,
            timeout: 6000
        });
    } else {
        appSetLocation(defaultLatLng);  // No geolocation support, show default map
    }


});
$(document).ready(function () {
    $('#map-canvas').click(function () {

        if (navigator.geolocation) {
            function success(pos) {

                // Location found, show map with these coordinates
                appSetLocation(pos.coords.latitude, pos.coords.longitude);
                getNearbyUsers(pos.coords.latitude, pos.coords.longitude);
            }

            function fail(error) {
                console.log(error);  // Failed to find location, show default map
            }

            // Find the users current position.  Cache the location for 5 minutes, timeout after 6 seconds
            navigator.geolocation.getCurrentPosition(success, fail, {
                maximumAge: 500000,
                enableHighAccuracy: true,
                timeout: 6000
            });
        }

    });
    $('.reply-menu__option').click(function () {
        var recipient = $(this).parent().attr('data-id');
        var msg = $(this).attr('data-msg');

        console.log(recipient, msg);
        $('.menu__bottom').removeClass('open');
    });
    setInterval(function () {
        getUserStats();
        switchTheme('good');
        getNearbyUsers('asdad', 'asdasd');


    }, 3000);

});
if (window.app) {
    /* Note: Callback functions need to be global. */
    app.setGestureCallback("onGesture");
    app.setLocationCallback("onLocation");

    var b = document.getElementById("b");
    b.onclick = function () {
        app.showMessage("You clicked the button.");
    };
}