<template>
  <div class="mapcontainer">
    <div class="mapbox" id="map" :style="{'height':'93vh', 'width':'100%', 'z-index':'0', 'overflow-y':'hidden'}"></div>
  </div>
</template>

<script>
import {mapState} from 'vuex'
import L from 'leaflet'

export default {
 computed : { ...mapState(['currentUser', 'list_of_events']) },

 data () {
    return {
      map: null,
      eventMarkers: [],
      testButtons: []
    }
 },
 beforeMount(){
   if (!this.currentUser){this.$router.push('/signUp')}
 },
 mounted(){
  this.initMap();

  if ( this.list_of_events.length == 0 ){
    this.$store.dispatch('get_events')
    .then( (response) => {
      console.log("in then: ", this.list_of_events)
      this.addEventsToMap();
    } )
  }
  else{
    this.addEventsToMap();
  }

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
        var customPopup = "<p>Click on this card to learn more about the following event:</p>";
        customPopup += "<p>Name: " + event.name + "</p>";
        customPopup += "<p>Style: " + event.style + "</p>"
        customPopup += "<button class='event_page_button' style='background-color:tomato; align-self:center; justify-self:center; margin:auto;display:flex;color:white; font-weight: 500; font-size: 0.875rem; cursor:porinter; text-transform:uppercase;border-radius: 4px; padding:8px; box-shadow: 0px 3px 1px -2px rgba(0, 0, 0, 0.2), 0px 2px 2px 0px rgba(0, 0, 0, 0.14), 0px 1px 5px 0px rgba(0, 0, 0, 0.12);' data=" + event.id +"> click for more details</button>"
        // specify popup options
        var customOptions = {
        'maxWidth': '500',
        'className' : 'custom'
        }

        var marker = L.circle([event.location.showLatitude, event.location.showLongitude], 1000, {color:'tomato'})
          .bindPopup(customPopup,customOptions).openPopup().addTo(this.map).on('click', this.updateOnclick)
        this.eventMarkers.push( marker )
      } );
    },
    updateOnclick(){
      this.$nextTick( () => {
        let btns = document.querySelectorAll('.event_page_button')
        for( let x = 0; x < btns.length; x++){
          btns[x].onclick = this.sendToEventPages
        }
      } )
    },
    
    sendToEventPages(){
      let btns = document.querySelector('.event_page_button')
      let data = btns.getAttribute("data")
      this.$store.commit('set_current_event',this.list_of_events.find( event => event.id == data ))
      this.$router.push('/eventPage')
    },
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

  /* css to customize Leaflet default styles  */
  .custom .leaflet-popup-tip,
  .custom .leaflet-popup-content-wrapper {
    background: #e93434;
    color: #ffffff;
  }

  .custom {
    background: #e93434;
    color: #ffffff;
  }
</style>
