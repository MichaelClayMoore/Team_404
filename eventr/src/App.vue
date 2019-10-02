<template>
  <v-app>
    <v-app-bar
      :clipped-left="$vuetify.breakpoint.lgAndUp"
      app
      color="red darken-3"
      dark
    >
      <v-toolbar-title style="width: 300px" class="ml-0 pl-4" >
        <span class="hidden-sm-and-down">Eventr</span>
      </v-toolbar-title>
      
      <div class="flex-grow-1"></div>
      <v-btn icon>
        <v-icon>mdi-apps</v-icon>
      </v-btn>
      <v-btn icon>
        <v-icon>mdi-bell</v-icon>
      </v-btn>
      <v-btn
        icon
        large
      >
        <v-avatar
          size="32px"
          item
        >
          <v-img
            src=".\assets\headshot_002.jpg"
            alt="Vuetify"
          >
          </v-img></v-avatar>
      </v-btn>
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
