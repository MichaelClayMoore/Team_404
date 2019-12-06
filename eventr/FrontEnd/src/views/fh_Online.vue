<template>
<v-container>
  <div flex justify-center align-center column>
    <v-card color="transparent">
            <v-avatar color="#ff6347" size="62">
                <v-icon dark>mdi-account-circle</v-icon>
            </v-avatar>
            <v-card-title  >{{currentUser}}</v-card-title>
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
                        v-for="item in items"
                        :key="item.title"
                        @click=""
                      >
                        <v-list-item-icon>
                          <v-icon v-if="item.icon" color="pink">mdi-star</v-icon>
                        </v-list-item-icon>

                        <v-list-item-content>
                          <v-list-item-title v-text="item.title"></v-list-item-title>
                        </v-list-item-content>

                        <v-list-item-avatar>
                          <v-img :src="item.avatar"></v-img>
                        </v-list-item-avatar>
                      </v-list-item>
                    </v-list>
                  </v-layout>
                  <v-layout row justify-center>
                     <v-btn text small color="#ff6347" @click="addFriend()">Add Friend</v-btn>
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
                        v-for="item in searchedEvents"
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

  computed : { ...mapState(['currentUser', 'searchedEvents']) },
  // all the initial data for the component.
  data () {
    return {
      userProp:[
        { text: 'username', value: 'user.username' }
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
    addFriend(){
      this.$router.push('/fh_AddFriend')
    },
    addEvent(){
      this.$router.push('/event_Creator')
    },
    eventPage(e){
      console.log("works: ", e)
      this.$store.commit('set_current_event', e)
      this.$router.push('/eventPage')
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
