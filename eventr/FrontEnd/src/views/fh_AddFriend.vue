<template>
  <v-container>

    <v-dialog v-model="addfriendDialog" scrollable max-width="3000px">
      <v-card>
        <v-card-title :style = "{'background-color':'tomato','color':'white'}">Searched Parties</v-card-title>
        <v-divider></v-divider>
        <v-card-text style="height: 3000px;">

                <v-data-table


                > </v-data-table>



        </v-card-text>
        <v-divider></v-divider>
        <v-card-actions>
          <v-btn color="blue darken-1" text @click="eventDialog = false">Close</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>

    <!-- this is where the full page starts -->
    <div flex justify-center align-center column>
      <!-- title line -->

      <h1 :style="{'display':'inline','font-weight':'700','font-size':'15px'}">
        <span class="heading">Friends </span>
      </h1>
      <div class="friendBar">
        <router-link to="/fh_Online">
          <span class="friendBar"> | Online </span>
        </router-link>
        <router-link to="/fh_All">
          <span class="friendBar">| All </span>
        </router-link>
        <router-link to="/fh_Pending">
          <span class="friendBar">| Pending </span>
        </router-link>
        <router-link to="/fh_AddFriend">
          <span class="friendBar" :style="{'color':'orange'}">| Add Friend</span>
        </router-link>
      </div>
      <i
        class="material-icons"
        :style="{'font-size':'36px','position':'relative','top':'5px','color':'tomato'}"
      >whatshot</i>

      <!-- content section   -->
      <v-row dense>
        <v-card class="mx-auto" max-width="400">
          <v-img
            class="white--text align-end"
            height="200px"
            src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
          >
            <v-card-title>Send a Friend Request</v-card-title>
          </v-img>

          <v-card-text class="text--primary">
            <v-layout column>
              <!-- event name field -->
              <v-text-field
                v-model="addFriendProp['userID']"
                class="input"
                id="userID"
                label="Enter a Username"
                color="#ff6347"
              ></v-text-field>

              <!-- both the location and date buttons. -->
              <v-layout row style="margin-bottom:40px"></v-layout>
            </v-layout>
          </v-card-text>

          <v-card-actions>
            <v-btn
              color="#ff6347"
              :style="{'color':'#ffffff'}"
              @click="AddFriend"
            >Add Friend</v-btn>
          </v-card-actions>
        </v-card>
      </v-row>
    </div>
  </v-container>
</template>

<!--
______ script portion ______________________________________________________________
| this is the portion of the file that has to deal with all the javascript.        |
L__________________________________________________________________________________|
-->
<script>
import { mapState } from "vuex";

export default {
  // name of the file/component
  name: "fh_AddFriend",

  // all the initial data for the component.
  data() {
    return {
      // data that will be changed by the user
      addFriendProp: {
        userID: ""
      },

      addUserProp: {
        userID2: ""
      },

      // used for displaying the date to the user
      friendID: "Invite Friend",

      // data used to control page flow
      addfriendDialog: false
    };
  },

  mounted() {
    this.$store.dispatch("get_test");
  },

  // this section is to watch variables. Anytime a variable with a corresponding
  // name changes value, the function will run. the val that is passed into
  // every function is the new value that will be set.
  watch: {
    // currently none
  },

  // this is the methods portion. This is used to hold functions that our
  // page will use.
  methods: {
    // this function is for finalizing the event object and pushing it to the
    // store. it currently does not do anything - we need to implement the store
    // first.
    AddFriend() {
      console.info("Vue adding friend function flag");
      this.$store.dispatch("addfriend_event", this.addFriendProp);
      this.addfriendDialog = false;
    }
    // this function will run when the input event is emitted from the date
    // picker. it is responsible for changing the text on the button.
  }
};
</script>

<!--
______ style _portion ______________________________________________________________
| this is the portion of the file that has to deal with all the defined css styles.|
| the scoped prop says that any style defined here is only defined here.           |
L__________________________________________________________________________________|
-->
<style scoped>
/* style for elements that have the title clas */
.title {
  /* sets text to center and a bold 24px Montserrat font */
  text-align: center;
  font-family: "Montserrat", sans-serif;
  font-size: 24px;
  font-weight: bold;

  /* removes bottom margin */
  margin-bottom: 0px;
}

/* style for imput class */
.input {
  /* adds 5px to left and right of element */
  margin-left: 5px;
  margin-right: 5px;
}

/* style for heading class */
.heading {
  /* sets text to center and a 24px Montserrat font*/
  text-align: center;
  font-family: "Montserrat", sans-serif;
  font-size: 24px;

  /* removes margins from the bottom */
  margin-bottom: 0px;
}
.friendBar {
  /* sets text to center and a 24px Montserrat font*/
  display: inline;
  text-align: center;
  font-weight: 700;
  font-family: "Montserrat", sans-serif;
  font-size: 15px;
  text-decoration: none;
}
.friendBar a:link {
  color: black;
  text-decoration: none;
}

/* visited link */
.friendBar a:visited {
  color: black;
  text-decoration: none;
}

/* mouse over link */
.friendBar a:hover {
  color: orange;
  text-decoration: none;
}

/* selected link */
.friendBar a:active {
  color: orange;
  text-decoration: none;
}
</style>
