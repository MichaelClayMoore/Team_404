import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    list_of_events: [],
    searchedEvents: [],
    currentUser: 0,
    check_authentication: false
  },

  mutations: {
    add_event(state, event_to_add) {
      state.list_of_events.push(event_to_add);
    },
    remove_event(state, eventId){
      let location = state.list_of_events.findIndex( event => event['id'] == eventId );
      if ( location >= 0 ) { state.list_of_events.splice(location, 1); }
      console.log(state.list_of_events)
    },
    set_list_of_events(state, list){
      state.list_of_events = list;
    },
    set_searched_events(state, event_to_add){
      state.searchedEvents = event_to_add;
    },
    autenticated_user(state, bool_check){
      state.check_authentication = bool_check;
    },
    set_user(state, user){
      state.currentUser = user;
    }
  },

  actions: {

    get_test({ commit, rootState }) {
      axios.get('http://127.0.0.1:5000/get_test')
        .then(response => {
          console.log("Response")
          console.log(response.data)
        }, (err) => {
          console.log(err)
        })
    },

    save_event({ commit, rootState }, payload) {
      axios.post('http://127.0.0.1:5000/save_event',
        { params: { event: payload } }
      )
        .then(response => {
          console.log("Response")
          console.log(response.data)
          commit('add_event', payload)
        }, (err) => {
          console.log(err)
        })
    },

    addfriend_event({ commit, rootState }, payload) {
      axios.post('http://127.0.0.1:5000/addfriend_event',
        { params: { name: payload } }
      )
        .then(response => {
          console.log("Response")
          console.log(response.data)
          commit('addfriend_event', payload)
        })
      .then(response => {
        console.log("Response: ", response.data)
        commit('add_event', response.data)
      }, (err) => {
        console.log(err)
      })
    },

    delete_event({commit, rootState}, payload){
      axios.post('http://127.0.0.1:5000/delete_event',
      { params:{ eventId: payload } }
      )
      .then(response => {
        console.log("Response: ", response.data)
        commit('remove_event', payload)
      }, (err) => {
        console.log(err)
      })
    },

    savefriend_event({ commit, rootState }, payload) {
      axios.post('http://127.0.0.1:5000/savefriend_event',
        { params: { friend: payload } }
      )
        .then(response => {
          console.log("Response")
          console.log(response.data)
          commit('savefriend_event', payload)
        })
    },


    get_events({ commit, rootState }) {
      axios.get('http://127.0.0.1:5000/get_events')
        .then(response => {
          console.log("Response")
          console.log(response.data)
          commit('set_list_of_events', response.data)
        }, (err) => {
          console.log(err)
        })
    },

    search_event({ commit, rootState }, payload) {
      axios.post('http://127.0.0.1:5000/search_event', {
        params: {searchProp: payload}
      })
      .then(response => {
        console.log("Response: ", response.data)
        commit('set_searched_events', response.data)
        //resolve(response.data)
      }, (err) => {
        console.log(err)
      })
    },

    validate_user({commit, rootState}, payload){
      axios.post('http://127.0.0.1:5000/validate_user', {
        params: {searchProp: payload}
      })
      .then(response => {
        console.log("Response: ", response.data)
        commit('authenticated_user', response.data)
        //resolve(response.data)
      }, (err) => {
        console.log(err)
      })
    }
  }
})
