
<template>
<v-container>


    <v-dialog v-model="dateDialog" max-width="50%">
      <v-card>
        <v-card-title :style="{'background-color':'tomato','color':'white'}" class="title">When is it?</v-card-title>
        <v-card-actions>
          <v-date-picker range landscape full-width color="#ff6347" v-model="eventProp['date']" style="font-size:15px" v-on:input="updateDateString" ></v-date-picker>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <v-dialog v-model="locationDialog" max-width="50%">
      <v-card>

        <!-- title bar -->
        <v-card-title :style="{'background-color':'tomato','color':'white'}" class="title">Where is it?</v-card-title>

        <!-- input for the address -->
        <v-card-text>
          <v-layout row>
          <v-text-field v-model="eventProp['location']['city']"  class="input" label="City"></v-text-field>
          <v-text-field v-model="eventProp['location']['state']"  class="input" label="State"></v-text-field>
          <v-text-field v-model="eventProp['location']['zip']"  class="input" label="Zip"></v-text-field>
          </v-layout>
        </v-card-text>

        <!-- this is the or... on the card -->
        <v-card-text>
          <div class="d-flex flex-row align-content-space-between" >
            <v-spacer/>
            <span class="title">or...</span>
            <v-spacer/>
          </div>
        </v-card-text>

        <!-- this is the container for the map. it is currently under dev and not fully finished -->
        <v-card-text>
          <div>
            <p>you can also use this map...</p>
            <div style="background-image: linear-gradient(to bottom right, green, #f06d06); height:200px"></div>
          </div>
        </v-card-text>
        
      </v-card>
    </v-dialog>

<!-- Page Content -->
<div flex justify-center align-center column>

    <!-- title line -->
    <h1 :style="{'display':'inline','font-weight':'bold','font-size':'48px'}"><span class="heading">Search for an Event </span></h1>
    <i class="material-icons" :style="{'font-size':'36px','position':'relative','top':'5px','color':'tomato', 'padding-bottom': '25px'}">whatshot</i>

    <!-- content section   -->
    <v-layout column>
        <!-- event name field -->
        <v-text-field v-model="eventProp['name']" class="input" id="name" label="Event Name" outlined color="#ff6347"></v-text-field>
        <v-text-field v-model="eventProp['creator']" class="input" id="creator" label="Event Creator" outlined color="#ff6347"></v-text-field>

        <v-select v-model="eventProp['style']" :items="Events" multiple outlined class="input" label="Event Type" color="#ff6347"></v-select>

        <!-- Buttons -->
        <v-layout row style="margin-bottom:20px">
          <v-spacer/>
          <v-btn color="#ff6347" :style="{'color':'#ffffff'}" @click="dateDialog = true;">{{eventDateString}}</v-btn>
          <v-spacer/>
          <v-btn color="#ff6347" :style="{'color':'#ffffff'}" @click="locationDialog = true;">{{eventLocation}}</v-btn>
          <v-spacer/>
        </v-layout>
        

    </v-layout>

</div>
</v-container>
</template>

<script>
export default {
  // name of the file/component
  name: 'eventCreator',

  // all the initial data for the component.
  data () {
    return {
      // data that will be changed by the user
      eventProp:{
        'name': "",
        'creator': "",
        'location': {
          'city':"",
          'state':"",
          'zip':"",
          'lat':0,
          'long':0
        },
      },
        'date': ['2019-09-10', '2019-09-20'],

      

      // used for displaying the date to the user
      eventLocation: "search around your area",
      eventDateString: "choose a date range",

      // data used to control page flow
      locationDialog: false,
      dateDialog: false,

      // data used for the user to select from
      Events: [
        "Birthday",
        "Get Together",
        "Wedding",
        "Formal Event"
      ]
    }
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
      console.info("i am submitting")
    },

    // this function will run when the input event is emitted from the date
    // picker. it is responsible for changing the text on the button.
    updateDateString(){

      return this.date.join(' ~ ')
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
