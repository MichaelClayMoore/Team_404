<template>
<v-container>

      <v-card>
        <v-card-title :style = "{'background-color':'tomato','color':'white'}">Searched Parties</v-card-title>
        <v-divider></v-divider>
        <v-card-text style="height: 3000px;">

          <v-data-table
            :headers="headers"
            :items="events"
            :items-per-page="10"
            class="elevation-3"
            @click:row="eventPage"

          ></v-data-table>

        </v-card-text>
      </v-card>
</v-container>
</template>


<script>
import {mapState} from 'vuex'

export default {
  // name of the file/component
  name: 'fh_Pending',

  computed : { ...mapState(['currentUser', 'searchedEvents']) },

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

      events: []
    }
  },

  beforeMount(){
    if (!this.currentUser){this.$router.push('/signUp')}
    this.searchEvent();
    this.searchMyFriendList();
  },

  watch :{

  },

  methods :{

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
