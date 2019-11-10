<template>
    <div flex justify-center align-center column>

        <h1 :style="{'display':'inline','font-weight':'bold','font-size':'48px'}"><span class="heading">Join Event </span></h1>
        <v-text-field v-model="message" placeholder="Enter party text here"/>        
        <div>
            <v-btn color="#ff6347" :style="{'color':'#ffffff'}" @click="joinEvent">Submit</v-btn>

        </div>

        <v-data-table> what ?</v-data-table>
    </div>

    

</template>

<script>
export default {
    mounted(){
        console.log("I am mounted!")
    },
    methods: {}
}
</script>


<style scoped>

    
</style>

<!--

   join_event({commit, rootState},payload){
      axios.post('http://127.0.0.1:5000/join_event',
      { params:{event: payload}}
      )
      .then(response=> {
        console.log("Respoonse")
        console.log(response.data)
        commit('join_event' , payload)
      }, (err) => {
        console.log(err)
      })
    },


in event router

@event_router.route("join_event", methods=['POST'])
def save_join_event():
    print(request.get_json()['params']['event'])
    return "Join success"


  joinEvent(){
      console.info("i am joining \"sending data\" ")
      this.$store.dispatch('join_event', this.eventProp)
    }
-->
