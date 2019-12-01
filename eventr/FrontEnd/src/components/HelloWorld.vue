<template>
  <div class="mapcontainer">
    <div class="mapbox" id="map" :style="{'height':'93vh', 'width':'100%', 'z-index':'0', 'overflow-y':'hidden'}"></div>
  </div>
</template>

<script>
import L from 'leaflet'

export default {
 data () {
    return {
      map: null
    }
 },
 mounted(){
   console.log("I am mounted")
   this.initMap();
 },
 methods: {
    initMap(){
     console.log("I am called")
     this.map = L.map('map').setView([38.63, -90.23], 12);

    let context = this
    navigator.geolocation.getCurrentPosition(function(location) {
      context.map.panTo([location.coords.latitude,location.coords.longitude])
    });
    this.tileLayer = L.tileLayer(
      'https://cartodb-basemaps-{s}.global.ssl.fastly.net/rastertiles/voyager/{z}/{x}/{y}.png',
      {
        maxZoom: 18,
        attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>, &copy; <a href="https://carto.com/attribution">CARTO</a>',
      }
    );
    this.tileLayer.addTo(this.map);
    }
  }
 }
</script>

<style scoped>
  .mapcontainer{
    background-color: red;
    width: 100%;
    margin-left: 0px;
    margin-right: 0px;
    overflow-y: hidden
  }
</style>
