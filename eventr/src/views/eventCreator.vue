<template>
  <div v-bind:style="{'display':'block'}">
    <h1>Create a Party</h1>
    <input id="name" v-model="eventName" placeholder="Enter your event name."></input>
    <select id="style" v-model="eventStyle">Select the event style.
      <option value="">--Please choose an option--</option>
    <option value="dog">Dog</option>
    <option value="cat">Cat</option>
    <option value="hamster">Hamster</option>
    <option value="parrot">Parrot</option>
    <option value="spider">Spider</option>
    <option value="goldfish">Goldfish</option>
    </select>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      eventName: "",
      eventStyle: ""
    }
  }
}
</script>

<style media="screen">
  .about{
    /* background: linear-gradient(to top right,#ffc000, #ff5004); */
    /* background: linear-gradient(to top right, #F2865E, #F2C641, #05C7F2, #049DD9, #F2167D); */
    /* background: linear-gradient(to top right, #FEEAF2, #FFCB1F, #12BAC2, #0BDBE6, #F01677, #ff1100); */
    /* height: 80vh; */
  }

  #name{
    border-radius: 150px;
    width: 250px;
    height: 40px;
    border: 2px solid #ff1100;
    text-align: center;
    margin: 5px;
    display: block;
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
