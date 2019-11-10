<template>
    <div flex justify-center align-center column>

        <h1 :style="{'display':'inline','font-weight':'bold','font-size':'48px'}"><span class="heading">Join Event </span></h1>
        <v-text-field v-model="message" placeholder="Enter party text here"/>        
        <div>
            <v-btn block variant="primary">Join Button</v-btn>
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