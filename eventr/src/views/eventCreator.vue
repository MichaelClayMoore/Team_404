<template>
  <v-container>
    <v-dialog
      v-model="dialog"
      max-width="50%"
    >
      <v-card>
        <v-card-title class="tilte">When is it?</v-card-title>
        <v-card-actions>
          <v-date-picker landscape full-width color="#ff6347" v-model="eventDate" :style="{'font-size':'15px'}"></v-date-picker>
        </v-card-actions>
      </v-card>
    </v-dialog>
    <v-flex flex justify-center align-center column>
    <h1 :style="{'display':'inline','font-weight':'bold','font-size':'48px'}"><span class="heading">Create a Event </span></h1>
    <i class="material-icons" :style="{'font-size':'36px','position':'relative','top':'5px','color':'tomato'}">whatshot</i>
    <v-layout column>
      <!-- <Span class="heading"> The essentials.</Span>
      <v-divider/>
      <br/> -->
      <v-text-field class="input" id="name" label="Event Name" color="#ff6347"></v-text-field>
      <v-btn color="#ff6347" :style="{'color':'#ffffff'}" @click="dialog = true;">{{test}}</v-btn>
      <div class="d-flex flex-row align-content-space-between" >
        <v-spacer/>
        <v-checkbox class="flex-grow-1 flex-shrink-0" label="RSVP Required" color="#ff6347"></v-checkbox>
        <v-checkbox class="flex-grow-1 flex-shrink-0" label="Condition 2" color="#ff6347"></v-checkbox>
        <v-checkbox class="flex-grow-1 flex-shrink-0" label="Condition 3" color="#ff6347"></v-checkbox>
        <v-checkbox class="flex-grow-1 flex-shrink-0" label="Condition 4" color="#ff6347"></v-checkbox>
      </div>
      <Span class="heading"> Tell us a little about it.</Span>
      <v-textarea filled clearable></v-textarea>
      <v-select v-model="eventName" :items="Events" filled rounded class="input" id="test" label="Event Type" color="#ff6347"></v-select>

      <v-container>
        <v-layout row>
          <v-text-field label="What do you need?"></v-text-field>
          <v-spacer/>
          <v-text-field label="What do you want?"></v-text-field>
        </v-layout>
      </v-container>
      <v-text-field label="Invite people" hint="Enter the username of your friend or someone you know."></v-text-field>
    </v-layout>
  </v-flex>
  <!-- v-layout row>
     <v-text-field label="What do you need?"></v-text-field>
    <v-spacer/>
    <v-text-field label="What do you want?"></v-text-field> 
    <v-spacer/>
    <v-btn color="#ff6347" :style="{'color':'#ffffff'}" @click="">
      <i class="material-icons">
        arrow_back_ios
      </i>
      Back
    </v-btn>
    <v-spacer/>
    <v-btn color="#ff6347" :style="{'color':'#ffffff'}" @click="">Next
      <i class="material-icons">
        arrow_forward_ios
      </i>
    </v-btn>
    <v-spacer/>
  </v-layout -->
</v-container>
</template>

<script>
export default {
  name: 'eventCreator',
  data () {
    return {
      eventName: "",
      dataDia: false,
      test: "choose a date",
      dialog: false,
      eventStyle: "",
      eventDate: new Date().toISOString().substr(0,10),
      Events: [
        "Birthday",
        "Get Together",
        "Wedding",
        "Formal Event"
      ]
    }
  },
  watch :{
    eventDate(val){
      this.dialog = false;
      let tempDate = new Date(val);
      this.test = tempDate.toDateString();
    }
  },
  methods :{
    showDatePicker(){
      console.log("test");
      this.dialog = true;
    }
  }
}
</script>

<style scoped>
  .about{
    /* background: linear-gradient(to top right,#ffc000, #ff5004); */
    /* background: linear-gradient(to top right, #F2865E, #F2C641, #05C7F2, #049DD9, #F2167D); */
    /* background: linear-gradient(to top right, #FEEAF2, #FFCB1F, #12BAC2, #0BDBE6, #F01677, #ff1100); */
    /* height: 80vh; */
  }

  .v-text-field{
    display: block;
  }

  .title{
    /* 'text-align':'center', 'font-family':'\"Times New Roman\"\, Times\, serif' */
    text-align: center;
    font-family: 'Montserrat', sans-serif;
    font-weight: bold;
    margin-bottom: 0px;
    font-size: 24px;
  }

  .timeLine{
    align-self: center;
  }

  .heading{
    text-align: center;
    font-family: 'Montserrat', sans-serif;
    margin-bottom: 0px;
    font-size: 24px;
  }

  #test{
    margin-top: 0px;
    width: 50vw;
    display: inline;
  }

  #style{
    width: 250px;
    height: 40px;
    background-color: #F44336;
    color: #ffffff;
    align-items: center;
    margin: 5px;
    display: block;
  }

</style>
