// Create a function called `createMap` that will take in `bikestations` as an argument.
// function to create the initial map layer
function createMap(charityHqs) {

    // Create the tile layer that will be the background
    var lightmap = L.tileLayer("https://api.mapbox.com/styles/v1/mapbox/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
        attribution: "Map data &copy; <a href=\"https://www.openlightmap.org/\">Openlightmap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
        maxZoom: 18,
        id: "light-v10",
        // id: "streets-v11"
        accessToken: API_KEY
    });

    // Create a baseMaps object to hold the lightmap layer
    var baseMaps = {
        "Street Map": lightmap
    };

    // Create an overlayMaps object to hold the charity headquarters layer
    var overlayMaps = {
        "Charity Headquarters": charityHqs
    }

    // Create the map object with options
    var map = L.map("map", {
        center: [37.09, -95.71],
        zoom: 3,
        layers: [lightmap, charityHqs]
    });

    // Create a "layer control", pass in baseMaps and overlayMaps & add this to the map object we just created above
    L.control.layers(baseMaps, overlayMaps, {
        collapsed: false
    }).addTo(map);

}


function createMarkers(response) {
    // print "hello" to ensure this function is running
    console.log("hello");

    // Pull the "charities" property off of response.data
    // var charities = response[0];
    // console.log(charities);
    // for (var i = 0; i < charities.length; i++) {
    //     var charityInfo = charities[i];


    // Initialize an array to hold bike markers
    var charitiesArray = [];

    // Loop through the charities array
    for (var i = 0; i < response.length; i++) {
        var charityInfo = response[i];
        if (charitycharityInfo.lat && charityInfo.lng)
        {
        // For each charityInfo, create a marker and bind a popup with the charityInfo's name
        // Using the response from a future d3 call loop through the charities and create a marker to represent each charityInfo.
        var charityMarker = L.marker([charityInfo.lat, charityInfo.lng])
            // Give each marker a popup to display the name and capacity of its charityInfo.
            .bindPopup("Charity Name: " + charityInfo.charity_name + "<br></br>" + "City: " + charityInfo.city)

        // Add the marker to the charitiesArray array
        charitiesArray.push(charityMarker);
        }
    }

    createMap(L.layerGroup(charitiesArray));

}

// // Perform a GET request using D3 to the [Citi Bike Station Information Endpoint](https://gbfs.citibikenyc.com/gbfs/en/station_information.json) that will call the `createMarkers` function.
// Call on the createMarkers function and call on the API -- able to do them both within the d3.json execution
d3.json("location", createMarkers);
