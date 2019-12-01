<template>
  <v-container>
    <div flex justify-center align-center column>

      <!-- title line -->
      <h1 :style="{'display':'inline','font-weight':'bold','font-size':'48px'}"><span class="heading">{{ current_Event.name }}</span></h1>
      <i class="material-icons" :style="{'font-size':'36px','position':'relative','top':'5px','color':'tomato'}">whatshot</i>

      <v-card>
        
        <v-card-title>Location: {{current_Event.location.address1}} {{current_Event.location.city}}, {{current_Event.location.state}} </v-card-title>
      </v-card>
    </div>

  </v-container>
</template>


<script>
import {mapState} from 'vuex'

export default {
  // name of the file/component
  name: 'eventPage',

  computed : { ...mapState(['currentUser', 'current_Event']) },

  // all the initial data for the component.
  data () {
    return {
      // data that will be changed by the user
      eventProp:{
        'name': "",
        'location': {
          'address1':"",
          'address2':"",
          'city':"",
          'state':"",
          'zip':"",
          'latitude':0,
          'longitude':0
        },
        'date': new Date().toISOString().substr(0,10),
        'style': "",
        'host': 0,
        'description': "",
        'rsvp':false,
        'creator': "",
        'attendees': []
      },

      // used for displaying the date to the user
      eventLocation: "choose a location",
      eventDateString: "choose a date",

      // data used to control page flow
      locationDialog: false,
      dateDialog: false,

      // data used for the user to select from
      Events: [
        "Birthday",
        "Get Together",
        "Wedding",
        "Formal Event",
        "Other"
      ]
    }
  },

  mounted(){
    this.$store.dispatch('get_test')
    this.eventProp['creator'] = this.currentUser;
  },

  // this section is to watch variables. Anytime a variable with a corresponding
  // name changes value, the function will run. the val that is passed into
  // every function is the new value that will be set.
  watch :{
    // currently none
  },

  // this is the methods portion. This is used to hold functions that our
  // page will use.
  methods :{

    
  }
}
</script>


<style scoped>

  /* style for elements that have the title clas */
  .title{
    /* sets text to center and a bold 24px Montserrat font */
    text-align: center;
    font-family: 'Montserrat', sans-serif;
    font-size: 24px;
    font-weight: bold;

    /* removes bottom margin */
    margin-bottom: 0px;
  }

  /* style for imput class */
  .input{
    /* adds 5px to left and right of element */
    margin-left: 5px;
    margin-right: 5px;
  }

  /* style for heading class */
  .heading{
    /* sets text to center and a 24px Montserrat font*/
    text-align: center;
    font-family: 'Montserrat', sans-serif;
    font-size: 48px;

    /* removes margins from the bottom */
    margin-bottom: 0px;
  }

</style>
