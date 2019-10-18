<template>
  <v-container>

    <!--
    ______ date dialog _________________________________________________________________
    | this is the date dialog. this will appear when the date button.                  |
    | v-model = dateDialog                                                             |
    |     -> this is what allows this to be visible. if yes, it will be visible.       |
    |        otherwise it is hidden.                                                   |
    L__________________________________________________________________________________|
    -->
    <v-dialog v-model="dateDialog" max-width="50%">
      <v-card>
        <v-card-title :style="{'background-color':'tomato','color':'white'}" class="title">When is it?</v-card-title>
        <v-card-actions>
          <v-date-picker landscape full-width color="#ff6347" v-model="eventDate" :style="{'font-size':'15px'}"></v-date-picker>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!--
    ______ location dialog _____________________________________________________________
    | this is the location dialog. this will appear when the location button.          |
    | v-model = locationDialog                                                         |
    |     -> this is what allows this to be visible. if yes, it will be visible.       |
    |        otherwise it is hidden.                                                   |
    L__________________________________________________________________________________|
    -->
    <v-dialog v-model="locationDialog" max-width="50%">
      <v-card>
        <!-- title bar -->
        <v-card-title :style="{'background-color':'tomato','color':'white'}" class="title">Where is it?</v-card-title>

        <!-- input for the address -->
        <v-card-text>
          <v-layout row>
          <v-text-field class="input" label="Address 1"></v-text-field>
          <v-text-field class="input" label="Address 2 (optional)"></v-text-field>
          <v-text-field class="input" label="City"></v-text-field>
          <v-text-field class="input" label="State"></v-text-field>
          <v-text-field class="input" label="Zip"></v-text-field>
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

    <!-- this is where the full page starts -->
    <v-flex flex justify-center align-center column>
      <!-- title line -->
      <h1 :style="{'display':'inline','font-weight':'bold','font-size':'48px'}"><span class="heading">Create a Event </span></h1>
      <i class="material-icons" :style="{'font-size':'36px','position':'relative','top':'5px','color':'tomato'}">whatshot</i>

      <!-- content section   -->
      <v-layout column>

        <!-- event name field -->
        <v-text-field v-model="eventName" class="input" id="name" label="Event Name" color="#ff6347"></v-text-field>

        <!-- both the location and date buttons. -->
        <v-layout row>
          <v-spacer/>
          <v-btn color="#ff6347" :style="{'color':'#ffffff'}" @click="dateDialog = true;">{{eventDateString}}</v-btn>
          <v-spacer/>
          <v-btn color="#ff6347" :style="{'color':'#ffffff'}" @click="locationDialog = true;">{{eventLocation}}</v-btn>
          <v-spacer/>
        </v-layout>

        <!-- rsvp checkbox -->
        <div class="d-flex flex-row align-content-space-between" >
          <v-spacer/>
          <v-checkbox class="flex-grow-1 flex-shrink-0" label="RSVP Required" color="#ff6347"></v-checkbox>
        </div>

        <!-- tell us a little about section -->
        <Span class="heading"> Tell us a little about it.</Span>
        <v-textarea filled clearable></v-textarea>

        <!--
        ______ Event style selector ________________________________________________________
        | this is the style selector. the user will only be able to select one of the      |
        | provided items in the Events variable.                                           |
        | v-model = eventStyle                                                             |
        |     -> this is what hold the value of what they select. originally set to the    |
        |        empty string. it will be replaced with whatever value they select.        |
        L__________________________________________________________________________________|
        -->
        <v-select v-model="eventStyle" :items="Events" filled rounded class="input" label="Event Type" color="#ff6347"></v-select>

        <!-- this hold the 'where is it' input -->
        <v-container>
          <v-layout row>
            <v-text-field label="Where is it?"></v-text-field>
          </v-layout>
        </v-container>

        <!--
         ______ invite people field ________________________________________________________
        | this is where they will be able to invite friends.                               |
        | this is something to be implemented when friends are added to our site           |
        | as well as our database.                                                         |
        L__________________________________________________________________________________|
        -->
        <v-text-field label="Invite people" hint="Enter the username of your friend or someone you know."></v-text-field>
      </v-layout>
  </v-flex>
</v-container>
</template>

<!--
______ script portion ______________________________________________________________
| this is the portion of the file that has to deal with all the javascript.        |
L__________________________________________________________________________________|
-->
<script>
export default {
  // name of the file/component
  name: 'eventCreator',

  // all the initial data for the component.
  data () {
    return {
      // data that will be changed by the user
      eventName: "",
      eventLocation: "choose a location",
      eventDate: new Date().toISOString().substr(0,10),
      eventStyle: "",

      // used for displaying the date to the user
      eventDateString: "choose a date",

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

    // if the eventDate variable changes, they are trying to select a date
    eventDate(val){
      // hide the dialog because they have choosen now.
      this.dateDialog = false;

      // gets the new date that was chosen
      let tempDate = new Date(val);
      tempDate.setDate( tempDate.getDate() + 1 )

      // sets the display variable so the user can see what they chose
      this.eventDateString = tempDate.toDateString();
    }
  },

  // this is the methods portion. This is used to hold functions that our
  // page will use.
  methods :{
    // currently none
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
