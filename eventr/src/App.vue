<template>
  <v-app>
    <v-app-bar app>
      <v-toolbar-title class="headline text-uppercase">
        <span>Eventr</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
    </v-app-bar>
    <v-content>
      <div id="nav" class="ml-0 pl-4">
        <router-link to="/home">Home</router-link>
        <router-link to="/about"> | About</router-link>
        <router-link to="/eventCreator"> | Event Creator</router-link>
        <router-link to="/friendsHub"> | Friends</router-link>
      </div>
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
