<template>
<v-container>


    <v-dialog v-model="testDialog" max-width="50%">
      <v-card>
        <v-card-title :style="{'background-color':'tomato','color':'white'}" class="title">{{searchedEvents}}</v-card-title>
      </v-card>
    </v-dialog>

  <v-dialog v-model="eventDialog" scrollable max-width="3000px">  
      <v-card>
        <v-card-title :style = "{'background-color':'tomato','color':'white'}">Searched Parties</v-card-title>
        <v-divider></v-divider>
        <v-card-text style="height: 3000px;">

                <v-data-table 
                  :headers="headers"
                  :items="searchedEvents"
                  :items-per-page="3"
                  class="elevation-3"
                  
                > </v-data-table>
 
          

        </v-card-text>
        <v-divider></v-divider>
        <v-card-actions>
          <v-btn color="blue darken-1" text @click="eventDialog = false">Close</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>


    <v-dialog v-model="dateDialog" max-width="50%">
      <v-card>
        <v-card-title :style="{'background-color':'tomato','color':'white'}" class="title">When is it?</v-card-title>
        <v-card-actions>
          <v-date-picker landscape multiple full-width color="#ff6347" v-model="searchProp['date']" style="font-size:15px" v-on:input="updateDateString" ></v-date-picker>
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
          <v-text-field v-model="searchProp['location']['city']"  class="input" label="City"></v-text-field>
          <v-text-field v-model="searchProp['location']['state']"  class="input" label="State"></v-text-field>
          <v-text-field v-model="searchProp['location']['zip']"  class="input" label="Zip"></v-text-field>
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
        <v-text-field v-model="searchProp['name']" class="input" id="name" label="Event Name" outlined color="#ff6347"></v-text-field>
        <v-text-field v-model="searchProp['creator']" class="input" id="creator" label="Event Creator" outlined color="#ff6347"></v-text-field>

        <v-select v-model="searchProp['style']" :items="Events" multiple outlined class="input" label="Event Type" color="#ff6347"></v-select>

        <!-- Buttons -->
        <v-layout row style="margin-bottom:20px">
          <v-spacer/>
          <v-btn color="#ff6347" :style="{'color':'#ffffff'}" @click="dateDialog = true;">{{eventDateString}}</v-btn>
          <v-spacer/>
          <v-btn color="#ff6347" :style="{'color':'#ffffff'}" @click="locationDialog = true;">{{eventLocation}}</v-btn>
          <v-spacer/>
        </v-layout>
        
        <v-btn color="#ff6347" :style="{'color':'#ffffff'}" @click="searchEvent">Submit</v-btn>
    </v-layout>
</div>
</v-container>
</template>


<script>
import {mapState} from 'vuex'

export default {
  // name of the file/component
  name: 'searchEvent',

  computed : { ...mapState(['searchedEvents']) },

  // all the initial data for the component.
  data () {
    return {
      // data that will be changed by the user
      searchProp:{
        'name': "",
        'location': {
          'address1':"",
          'address2':"",
          'city':"",
          'state':"",
          'zip':"",
          'lat':0,
          'long':0
        },
        'date': [],
        'style': [],
        'description': "",
        'rsvp': false,
        'creator': "",
        'attendees': []
      },
      headers: [
          {
            text: 'Current Events',
            align: 'left',
            sortable: false,
            value: 'name',
          },
          { text: 'Location', value: 'location.address1' },
          { text: 'State', value: 'location.state' },
          { text: 'Date', value: 'date' },
          { text: 'Description', value: 'description'},
          { text: 'Style', value: 'style'},
        
        ],
        Events: [
         
        ],
  
      // used for displaying the date to the user
      eventLocation: "search around your area",
      eventDateString: "choose a date range",

      // data used to control page flow
      locationDialog: false,
      dateDialog: false,
      testDialog: false,
      eventDialog: false,

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

  },

  // this is the methods portion. This is used to hold functions that our page will use.
  methods :{

    updateDateString(){
      let i;
      let eventsAmu = 0;

      for (i = 0; i < this.searchProp.date.length; i++){
        eventsAmu++;
      }

      // gets the new date that was chosen
      let tempDate = new Date(this.searchProp.date);
      tempDate.setDate( tempDate.getDate() + 1 );

      // sets the display variable so the user can see what they chose
      this.eventDateString = tempDate.toDateString();
      
    },

    searchEvent(){
      console.info("i am searching")
      this.$store.dispatch('search_event', this.searchProp); 
      //console.log("response: ", this.returnedEvents)
      this.searchedEvents;
      this.testDialog = false;
      this.eventDialog = true;

    }
  }
}
</script>


<style scoped>
  .title{
    text-align: center;
    font-family: 'Montserrat', sans-serif;
    font-size: 24px;
    font-weight: bold;
    margin-bottom: 0px;
  }

  .input{
    margin-left: 5px;
    margin-right: 5px;
  }

  .heading{
    text-align: center;
    font-family: 'Montserrat', sans-serif;
    font-size: 24px;
    margin-bottom: 0px;
  }

</style>
