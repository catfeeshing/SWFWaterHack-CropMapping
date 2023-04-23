const apiKey = "AAPK4f83dfd4f97a45659546acc4a7ea5b6d6gDlw1rHh5jPLhHcUC-FOD-m2lxhBm9TdaocEAO4zmx_xzwgygklAnnp4Es0OpAd";

var cropIcon = L.Icon.extend({
    options: {
        iconUrl: "img/acorn.png",
        iconSize:     [30, 50],
        iconAnchor:   [22, 94],
        popupAnchor:  [-3, -76]
    }
});

var acorn = new cropIcon({iconUrl: "src/crop.png"});

L.icon = function (options) {
    return new L.Icon(options);
};

let items = [
    [119.9177271, 36.0338361, "ET: 50 <br> Kettleman City <br> Type: X", cropIcon],
    [30, 180, "ET: 15 <br> County: Stanislaus", cropIcon],
    [180, 3, "ET: 45 <br> County: Tuolome", cropIcon],
    [-118.699213, 36.540753, "ET", cropIcon]
    
  ];
      const map = L.map("map").setView([38.0297, -119.9741], 15);

      L.esri.Vector.vectorBasemapLayer("ArcGIS:Imagery", {
        apikey: apiKey
      }).addTo(map);

        //Creating a Layer object
       var layer = new L.TileLayer('https://tiles.arcgis.com/tiles/wx8u046p68e0iGuj/arcgis/rest/services/summer_classification_v2_simplified/MapServer?f=pjson&cacheKey=8f79fc35be60b1ee');
         
         //Adding layer to the map
        map.addLayer(layer);
         
         // Creating a marker

        for (let i = 0; i < items.length; i++) {
            makeMarkers(items[i][0], items[i][1], items[i][2], items[i][3]);
        }

function makeMarkers(lat, long, msg, img){
    L.marker([lat, long]).addTo(map).bindPopup(msg);
}