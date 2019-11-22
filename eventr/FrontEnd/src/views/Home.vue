<template>
  <div class="mapcontainer">
    <div class="mapbox" id="map" :style="{'height':'93vh', 'width':'100%', 'z-index':'0', 'overflow-y':'hidden'}"></div>
  </div>
</template>

<script>
import {mapState} from 'vuex'
import L from 'leaflet'

export default {
 computed : { ...mapState(['list_of_events']) },

 data () {
    return {
      map: null,
      eventMarkers: []
    }
 },
 mounted(){
  this.initMap();
  
  this.$store.dispatch('get_events')
    .then( (response) => { 
      console.log("in then: ", this.list_of_events)
      this.addEventsToMap();
    } )

 },
 watch: {

 },
 methods: {
    initMap(){
      this.map = L.map('map').setView([38.63, -90.23], 12);

      navigator.geolocation.getCurrentPosition( (location) => { this.map.panTo([location.coords.latitude,location.coords.longitude]) } );
      this.tileLayer = L.tileLayer(
        'https://cartodb-basemaps-{s}.global.ssl.fastly.net/rastertiles/voyager/{z}/{x}/{y}.png',
        {
          maxZoom: 18,
          attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>, &copy; <a href="https://carto.com/attribution">CARTO</a>',
        }
      );
      this.tileLayer.addTo(this.map);
    },
    addEventsToMap(){
      this.list_of_events.forEach( event => {
        console.log(event);
        var marker = L.marker([event.location.latitude, event.location.longitude]).addTo(this.map)
        this.eventMarkers.push( marker )
      } )
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
