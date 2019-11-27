<template>
  <v-container>
    <v-card>
      <v-card-title>test: {{current_Event.name}} </v-card-title>
    </v-card>
  </v-container>
</template>

<!--
______ script portion ______________________________________________________________
| this is the portion of the file that has to deal with all the javascript.        |
L__________________________________________________________________________________|
-->
<script>
import {mapState} from 'vuex'

export default {
  // name of the file/component
  name: 'eventCreator',

  computed : { ...mapState(['current_Event']) },

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

    // this function is for finalizing the event object and pushing it to the
    // store. it currently does not do anything - we need to implement the store
    // first.
    createEvent(){
      console.info("i am submitting: ", this.eventProp)
      this.$store.dispatch('save_event', this.eventProp)
      let context = this
      setTimeout( () => {
        context.$store.dispatch('get_events')
      }, 2000)
    },

    // this function will run when the input event is emitted from the date
    // picker. it is responsible for changing the text on the button.
    updateDateString(){

      // hide the dialog because they have choosen now.
      this.dateDialog = false;

      // gets the new date that was chosen
      let tempDate = new Date(this.eventProp.date);
      tempDate.setDate( tempDate.getDate() + 1 )

      // sets the display variable so the user can see what they chose
      this.eventDateString = tempDate.toDateString();
    },

    submitLocation(){

      // if they have all the Required fields
      if( this.eventProp.location.address1 && this.eventProp.location.city &&
        this.eventProp.location.state && this.eventProp.location.zip){

        // sets display string to the city they chose.
        this.eventLocation = this.eventProp.location.city;

        // clases the dialog
        this.locationDialog = false;

      }

    }
  }
}
</script>

<!--
______ style _portion ______________________________________________________________
| this is the portion of the file that has to deal with all the defined css styles.|
| the scoped prop says that any style defined here is only defined here.           |
L__________________________________________________________________________________|
-->
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
    font-size: 24px;

    /* removes margins from the bottom */
    margin-bottom: 0px;
  }

</style>
