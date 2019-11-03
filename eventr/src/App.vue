<template>
  <v-app>
    <v-app-bar app>
      <v-toolbar-title class="headline text-uppercase">
        <span>Eventr</span>
        
      </v-toolbar-title>
      <div id="nav" class="ml-0 pl-4">
        <router-link to="/home" :style="{'text-decoration':'none', 'color':'black'}"><span>Home</span></router-link>
        <router-link to="/about" :style="{'text-decoration':'none', 'color':'black'}"> | About</router-link>
        <router-link to="/eventCreator" :style="{'text-decoration':'none', 'color':'black'}"> | Create Event</router-link>
        <router-link to="/friendsHub" :style="{'text-decoration':'none', 'color':'black'}"> | Friends</router-link>
      </div>
      <v-spacer></v-spacer>
    </v-app-bar>
    <v-content>
      
      
      <router-view/>
     
    </v-content>
  </v-app>
</template>

<script>
import HelloWorld from './components/HelloWorld';
import friendsHub from './views/friendsHub';
export default {
  name: 'App',
  components: {
    HelloWorld, friendsHub,
  },
  data: () => ({
    //
  }),
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