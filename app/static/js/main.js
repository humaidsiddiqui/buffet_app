async function initMap() {
    // Create a map centered at a specific location
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 8,
        center: { lat: -34.397, lng: 150.644 },
        colorScheme: ColorScheme.DARK,
        mapId: "YOUR_MAP_ID"
    });
}
