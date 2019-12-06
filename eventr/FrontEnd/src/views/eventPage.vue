<template>
  <v-container fluid>
   <v-card>
    <v-container>
      <v-row >
        <v-col cols="auto">
          <v-img
            height="400"
            width="400"
            src="https://www.sxsw.com/wp-content/uploads/2019/06/SXSW-Party-photo-by-aaron-rogosin.png"
          ></v-img>
        </v-col>
        <v-col
          cols="auto"
          class="text-center pl-0"
        >
          <v-row
            class="flex-column ma-0 fill-height"
            justify="right"
          >
            <v-col class = "px-0">
              <h1 :style="{'display':'inline','font-weight':'bold','font-size':'50px'}"><span class="heading">{{ current_Event.name }}</span></h1>
              <i class="material-icons" :style="{'font-size':'36px','position':'relative','top':'5px','color':'tomato'}">whatshot</i>
            </v-col>

            <v-col class="px-0">
              <v-card-title> Location: {{current_Event.location.address1}} {{current_Event.location.city}}, {{current_Event.location.state}} </v-card-title>
            </v-col>

            <v-col class ="px-0">
              <v-card-title>Date: {{current_Event.date}} </v-card-title>
            </v-col>

            <v-col class ="px-0">
              <v-card-title>Description : {{current_Event.description}}</v-card-title>
            </v-col>
            <v-col class ="px-0">
              <v-card-title>Attendees : {{current_Event.attendees}}</v-card-title>
            </v-col>

            <v-col class ="px-0">
              <v-card-title>Attendees : {{listAtt}}</v-card-title>
            </v-col>
            <v-btn color="#ff6347" :style="{'color':'#ffffff'}" @click="joinEvent">JOIN</v-btn>

           </v-row>
        </v-col>
      </v-row>
    </v-container>

  </v-card>
      <div style="margin-top:25px">
        <h1 class="heading" :style="{'font-weight':'bold','font-size':'25px'}">Comments:</h1>
        <v-textarea v-model="comment" filled></v-textarea>
        <v-btn color="#ff6347" :style="{'color':'#ffffff', 'width':'100%', 'margin-bottom':'10px'}" @click="submit_comment"> Submit Comment</v-btn>
        <v-card style="margin-bottom:10px" v-for="c in current_Event.comments">
          <v-card-text style="color:black">{{c}}</v-card-text>
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

      comment: "",
      listAtt: [],
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
    joinEvent(){
      console.info("i am adding user num to party list", this.eventProp)
      let payload = { 'eventId':this.current_Event.id, 'user':this.currentUser}
      console.log(payload)
      this.$store.dispatch('join_event', payload )
     },

    submit_comment(){
      let payload = { 'eventId':this.current_Event.id, 'comment':this.comment}
      this.$store.dispatch( 'submit_comment', payload )
      this.comment = ""
    }

  },
  getAttendList(){
    console.info("fetching data from attend list", this.eventProp)
    let payload = { 'eventId':this.current_Event.id}
    console.log(payload)
    this.$store.dispatch('get_A_List', payload)
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
