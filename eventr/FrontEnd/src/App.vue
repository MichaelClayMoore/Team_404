<template>
  <v-app>
    <v-app-bar app v-if="currentUser">
      <v-toolbar-title class="headline text-uppercase">
        <span>Eventr</span>

      </v-toolbar-title>
      <div id="nav" class="ml-0 pl-4">
        <router-link to="/" :style="{'text-decoration':'none', 'color':'black'}"><span>Home</span></router-link>
        <router-link to="/event_creator" :style="{'text-decoration':'none', 'color':'black'}"> | Create Event</router-link>
        <router-link to="/searchEvent" :style="{'text-decoration':'none', 'color':'black'}"> | Search Event</router-link>
        <router-link to="/fh_All" :style="{'text-decoration':'none', 'color':'black'}"> | Friends</router-link>

      </div>
      <v-spacer></v-spacer>
    </v-app-bar>
    <v-content style="overflow-y:hidden;">
      <router-view/>
    </v-content>
  </v-app>
</template>

<script>
import HelloWorld from './components/HelloWorld';
import friendsHub from './views/friendsHub';
import {mapState} from 'vuex'

export default {
  name: 'App',
  computed : { ...mapState(['currentUser']) },
  components: {
    HelloWorld, friendsHub,
  },
  data: () => ({
    //
  }),

  beforeMount(){
    if(!this.currentUser){this.$router.push('/signUp')}
  }
};
</script>

<style>

/* visited link */
a:visited {
  color: black;
  text-decoration: none;
}

/* mouse over link */
a:hover {
  color: orange;
  text-decoration: none;
}

/* selected link */
a:active {
  color: orange;
  text-decoration: none;
}

</style>
