<template>
  <v-app>
    <v-app-bar app>
      <v-toolbar-title class="headline text-uppercase">
        <span>EVENT</span>
        <span>R</span>
      </v-toolbar-title>
      <v-spacer></v-spacer>
      <v-btn
        text
        href="https://github.com/MichaelClayMoore/Team_404"
        target="_blank"
      >
        <span class="mr-2">Github Link</span>
      </v-btn>
    </v-app-bar>
    
    <v-content>
      <div id="nav">
        <router-link to="/about">About</router-link>
        <router-link to="/eventCreator"> | Event Creator</router-link>
        <router-link to="/friendsHub"> | Add Friend</router-link>
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
