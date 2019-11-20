<template>
    <v-container fluid fill-height class="splash">

      <v-dialog v-model="signupDialog" max-width="50%">
      <v-card>

        <!-- title bar -->
        <v-card-title :style="{'background-color':'tomato','color':'white'}" class="title">Sign-up</v-card-title>

        <!-- input for the address -->
        <v-card-text>
          <v-layout row>
           <v-text-field v-model="eventProp['userinfo']['email']" class="input" label="email"></v-text-field>
          </v-layout>
          <v-layout row>
            <v-text-field v-model="eventProp['userinfo']['username']"  class="input" label="username"></v-text-field>
          </v-layout>
          <v-layout row>
            <v-text-field v-model="eventProp['userinfo']['password']"  class="input" label="password"></v-text-field>
          </v-layout>
          <v-layout row justify-center>
            <v-spacer/>
            <v-btn color="#ff6347"  :style="{'color':'#ffffff'}" @click="submitSignup()">Sign-up</v-btn>
          </v-layout>

        </v-card-text>
      </v-card>
      </v-dialog>

      <v-layout justify-center align-center column pa-6>
        <v-card color="cream">
          <div class="login">
          <v-card-title> Welcome to EventR </v-card-title>
          <v-text-field v-model="username" class="input" id="username" label="username" color="#ff6347"></v-text-field>
          <v-spacer/>
          <v-text-field  v-model="password" class="input" id="password" label="password" color="#ff6347"></v-text-field>
          <v-layout justify-center align-center>
            <v-btn color="#ff6347" :style="{'color':'#ffffff'}" @click="login()">Login</v-btn>
          </v-layout>
        </div>
        </v-card>
        <v-btn text small color="white" @click="signupDialog = true;">Don't have an account? Sign-up.</v-btn>
      </v-layout>
    </v-container>  
</template>

<script>
  export default {
    name: 'Signup',
    data() {
      return {
          username: "",
          password: "",
          eventProp:{
            'userinfo':{
              'email': "",
              'username': "",
              'password': ""
            }
          },
        signupDialog: false
      }
      
       
    },
    methods: {
      login() {
        if(this.username != ""  && this.password != ""){
          if(this.username == this.username ){
            
          }
        } 
      }
    }
}
</script>

<style scoped>
  .splash{ 
    background: url('https://images.unsplash.com/photo-1516450360452-9312f5e86fc7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80');
    background-size: cover;
    width: 100%;
    height: 100%;
    margin: 0px;
    padding: 0px;
  }

  .login{
    margin: 10px;
    padding: 10px;
  }

  .v-text-field{
    display: block;
  }
</style>

