<template>
  <v-row>
        <v-date-picker v-model="dates" range></v-date-picker>
    </v-row>
</template>

<script>
  export default {

      name: 'test',
      
    data: () => ({
    dates: ['2019-09-10', '2019-09-20'],
  }),
  computed: {
    dateRangeText () {
      return this.dates.join(' ~ ')
    },
  },
  }
</script>