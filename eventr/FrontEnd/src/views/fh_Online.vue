<template>
<v-container>

    <v-dialog v-model="addfriendDialog" max-width="500px" style='width:500px' >
      <!-- this is where the full page starts -->
        <!-- title line -->

        <!-- content section   -->
          <v-card>
            <v-img
              class="white--text align-end"
              height="200px"
              src="https://cdn.vuetifyjs.com/images/cards/docks.jpg"
            >
              <v-card-title>Add Friend</v-card-title>
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
                @click="AddFriendThing"
              >Add Friend</v-btn>
            </v-card-actions>
          </v-card>
    </v-dialog>

    <div flex justify-center align-center column>
    <v-card color="transparent">
            <v-avatar color="#ff6347" size="62">
                <v-icon dark>mdi-account-circle</v-icon>
            </v-avatar>
            <v-card-title  >{{name[0]}}</v-card-title>
            <v-layout row justify-center>
              <div class="friends">

                <v-card >
                <v-layout justify-center>
                <v-card-title justify-center>Friends</v-card-title>
                </v-layout>
                  <div class="content">
                  <v-layout justify-center>
                    <v-list>
                      <v-list-item
                        v-for="item in searchedMyFriendsList"
                      >
                        <v-list-item-icon>
                          <v-icon color="pink">mdi-star</v-icon>
                        </v-list-item-icon>

                        <v-list-item-content>
                          <v-list-item-title v-text="item"></v-list-item-title>
                        </v-list-item-content>

                        <v-list-item-avatar>
                          <v-img :src="item.avatar"></v-img>
                        </v-list-item-avatar>
                      </v-list-item>
                    </v-list>
                  </v-layout>
                  <v-layout row justify-center>
                     <v-btn text small color="#ff6347" @click="addFriend">Add Friend</v-btn>
                  </v-layout>
                  </div>
                </v-card>
              </div>
              <div class="friends">

                <v-card scrollable>
                  <v-layout justify-center>
                <v-card-title justify-center>Events</v-card-title>
                </v-layout>
                  <div class="content">
                  <v-layout justify-center>
                    <v-list>
                      <v-list-item
                        v-for="item in events"
                        :key="item.name"
                        @click="eventPage(item)"
                      >
                        <v-list-item-avatar color="#ff6347">
                          <v-icon >mdi-party-popper</v-icon>
                        </v-list-item-avatar>
                        <v-list-item-content>
                          <v-list-item-title v-text="item.name"></v-list-item-title>
                        </v-list-item-content>
                      </v-list-item>
                    </v-list>
                  </v-layout>
                  <v-layout row justify-center padding="10">
                     <v-btn text small color="#ff6347" @click="addEvent()">Add Event</v-btn>
                  </v-layout>
                  </div>
                </v-card>
              </div>
            </v-layout>
    </v-card>
  </div>
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
  name: 'userProfile',

  computed : { ...mapState(['currentUser', 'searchedEvents','searchedMyFriendsList','name']) },
  // all the initial data for the component.
  data () {
    return {
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
      addFriendProp: {
        userID: ""
      },
      userProp:[
        { text: 'username', value: 'user.username' }
      ],
      events: [],
      addfriendDialog: false

    }
  },

  // this section is to watch variables. Anytime a variable with a corresponding
  // name changes value, the function will run. the val that is passed into
  // every function is the new value that will be set.
  watch :{
    // currently none
  },

  beforeMount(){
    if (!this.currentUser){this.$router.push('/signUp')}
    this.searchEvent();
    this.searchMyFriendList();
    this.getUsername(this.currentUser);

  },

  // this is the methods portion. This is used to hold functions that our
  // page will use.
  methods :{
    addFriend(){
      this.addfriendDialog = true
    },
    AddFriendThing() {
      console.info("Vue adding friend function flag");
      this.$store.dispatch("addfriend_event", this.addFriendProp);
      this.addfriendDialog = false;
    },
    addEvent(){
      this.$router.push('/event_Creator')
    },
    eventPage(e){
      console.log("works: ", e)
      this.$store.commit('set_current_event', e)
      this.$router.push('/eventPage')
    },
    searchEvent(){
      console.info("i am searching")
      this.$store.dispatch('search_event', this.searchProp)
      //console.log("response: ", this.returnedEvents)

      .then(response => {
        for(var i = 0; i < this.searchedEvents.length; i++){
          if(this.currentUser == this.searchedEvents[i].attendees){
            this.events.push(this.searchedEvents[i])
          }

          var hey = parseInt(this.searchedEvents[i].attendees);
          console.log("atendees", this.currentUser);
        }
      })
    },
    searchMyFriendList() {
      console.info("i am searching my friends list");
      this.$store.dispatch("search_my_friends", this.currentUser);
      //console.log("response: ", this.returnedEvents)
    },
    getUsername( id ){
      console.log("id: ", id)
      this.$store.dispatch('getName', id);

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
  .friends{
    margin: 10px;
    padding: 10px;
  }

  .content{
    margin: 10px;
    padding: 10px;
  }
</style>
