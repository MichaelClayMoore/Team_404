<template>
  <v-container>
    <!--
    ______ allFriendsDialog _________________________________________________________________
    | this is the date dialog. this will appear when the date button.                  |
    | v-model = dateDialog                                                             |
    |     -> this is what allows this to be visible. if yes, it will be visible.       |
    |        otherwise it is hidden.                                                   |
    L__________________________________________________________________________________|
    -->

    <!-- this is where the full page starts -->
    <div flex justify-center align-center column>
      <!-- title line -->
      <h1 :style="{'display':'inline','font-weight':'700','font-size':'15px'}">
        <span class="heading">Friends</span>
      </h1>
      <div class="friendBar">
        <router-link to="/fh_Online">
          <span class="friendBar">| Online</span>
        </router-link>
        <router-link to="/fh_All">
          <span class="friendBar" :style="{'color':'orange'}">| All</span>
        </router-link>
        <router-link to="/fh_Pending">
          <span class="friendBar">| Pending</span>
        </router-link>
        <router-link to="/fh_AddFriend">
          <span class="friendBar">| Add Friend</span>
        </router-link>
      </div>
      <i
        class="material-icons"
        :style="{'font-size':'36px','position':'relative','top':'5px','color':'tomato'}"
      >whatshot</i>
      <!-- title line -->
      <v-card>
        <v-card-title :style="{'background-color':'tomato','color':'white'}">All My Friends</v-card-title>
        <v-divider></v-divider>
        <v-card-text style="height: 3000px;">
          <v-data-table
            :headers="headers"
            :items="searchedMyFriendsList"
            :items-per-page="10"
            class="elevation-3"
          ></v-data-table>
        </v-card-text>
        <v-divider></v-divider>
        <v-card-actions>
          <v-btn color="blue darken-1" text @click="eventDialog = false">Close</v-btn>
        </v-card-actions>
      </v-card>
      <div>
        {{searchedMyFriendsList}}
      </div>

      <!-- content section   -->
      <v-layout column></v-layout>
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

  computed: { ...mapState(["currentUser", "searchedMyFriendsList"]) },
  name: "fh_All",

  // all the initial data for the component.
  data() {
    return {
      // data that will be changed by the user
      friendProp: {
        Username: ""
      },

      headers: [
        {
          text: "All My Friends",
          align: "left",
          sortable: false,
          value: "name"
        },
        { text: "Username", value: "friendProp.Username" }
      ],
      Events: [],

      // used for displaying the date to the user
      eventLocation: "choose a location",
      eventDateString: "choose a date",

      // data used to control page flow
      locationDialog: false,
      dateDialog: false,
      allFriendsDialog: false
      // data used for the user to select from
    };
  },

  beforeMount() {
    this.searchMyFriendList();
  },

  watch: {
    // currently none
  },

  methods: {
    // this function is for finalizing the event object and pushing it to the
    // store. it currently does not do anything - we need to implement the store
    // first.
    createEvent() {
      console.info("i am submitting");
    },

    searchMyFriendList() {
      console.info("i am searching my friends list");
      this.$store.dispatch("search_my_friends", this.currentUser);
      //console.log("response: ", this.returnedEvents)
    }
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
