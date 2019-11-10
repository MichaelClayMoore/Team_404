import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    list_of_events: []
  },
  mutations: {
    add_event(state, event_to_add){
      state.list_of_events.push(event_to_add);
    },
    set_list_of_events(state, list){
      state.list_of_events = list;
    }
  },
  actions: {

    get_test({commit, rootState}){
      axios.get('http://127.0.0.1:5000/get_test')
      .then(response => {
        console.log("Response")
        console.log(response.data)
      }, (err) => {
        console.log(err)
      })
    },
    save_event({commit, rootState}, payload){
      axios.post('http://127.0.0.1:5000/save_event',
      { params:{ event: payload } }
      )
      .then(response => {
        console.log("Response")
        console.log(response.data)
        commit('add_event', payload)
      }, (err) => {
        console.log(err)
      })
    },

    get_events({commit, rootState}){
      axios.get('http://127.0.0.1:5000/get_events')
      .then(response => {
        console.log("Response")
        console.log(response.data)
        commit('set_list_of_events', response.data)
      }, (err) => {
        console.log(err)
      })
    }

  }
})
