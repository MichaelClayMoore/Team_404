<template>
    <div flex justify-center align-center column>

        <h1 :style="{'display':'inline','font-weight':'bold','font-size':'48px'}"><span class="heading">Join Event </span></h1>
        <v-text-field v-model="message" placeholder="Enter party text here"/>
        <v-text-field v-model="message" placeholder="Enter party location "/>
        <div>
            <v-btn color="#ff6347" :style="{'color':'#ffffff'}" @click="joinEvent">Submit</v-btn>

        </div>
        <v-row justify="center">


    <v-dialog v-model="dialog" scrollable max-width="3000px">
      <template v-slot:activator="{ on }">
        <v-btn color="primary" dark v-on="on">Search Button</v-btn>
      </template>
      <v-card>
        <v-card-title>Searched Parties</v-card-title>
        <v-divider></v-divider>
        <v-card-text style="height: 3000px;">

          <v-radio-group v-model="dialogm1" column>
            <v-radio label="Bahamas, The" value="bahamas"></v-radio>
            
             
                <v-data-table
                  :headers="headers"
                  :items="Event"
                
                > </v-data-table>
          
          </v-radio-group>

        </v-card-text>
        <v-divider></v-divider>
        <v-card-actions>
          <v-btn color="blue darken-1" text @click="dialog = false">Close</v-btn>
          <v-btn color="blue darken-1" text @click="dialog = false">Save</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </v-row>

        <v-data-table
        :headers="headers"
        :items="Event"
        :items-per-page="3"
        class="elevation-1"
        >
        <template v-slot:item.location="{ item }">
       <v-chip :color="getColor(item.location)" dark>{{ item.location }}</v-chip>
       </template>

        </v-data-table>
        
    </div>

<!--

    eventProp:{
        'name': "",
        'location': {
          'address1':"",
          'address2':"",
          'city':"",
          'state':"",
          'zip':"",
          'lat':0,
          'long':0
        },
        'date': new Date().toISOString().substr(0,10),
        'style': "",
        'description': "",
        'rsvp':false,
        'attendees': []
      },

-->

</template>

<script>
export default {
    mounted(){
        console.log("I am mounted!")
    },
    
       dataDialog () {
      return {
        dialogm1: '',
        dialog: false,
      }
    },

    data(){
        return{
        headers: [
          {
            text: 'Current Events',
            align: 'left',
            sortable: false,
            value: 'name',
          },
          { text: 'Location', value: 'location' },
          { text: 'Address', value: 'Address' },
          { text: 'Type', value: 'Type' },
          { text: 'Date', value: 'Date' },
        
        ],
        Event: [
          {
            name: 'Benson Party',
            location: 159,
            Address: 6.0,
            Type: 24,
            Date: 4.0,
          
          },
          {
            name: 'Fran P',
            location: 237,
            Address: 9.0,
            Type: 37,
            Date: 4.3,
            
          }
        ]
    }
    },
    methods: {
      getColor (location) {
        if (location > 200) return 'red'
        else if (location > 100) return 'orange'
        else return 'green'
      },
    }

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
