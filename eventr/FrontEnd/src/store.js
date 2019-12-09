import Vue from 'vue'
import Vuex from 'vuex'
import axios from 'axios'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    list_of_events: [],
    list_of_friends: [],
    searchedEvents: [],
    searchedMyFriendsList: [],
    currentUser: null,
    attend: [],
    check_authentication: false,
    current_Event: {},
    name: ""
  },

  mutations: {
    add_event(state, event_to_add) {
      state.list_of_events.push(event_to_add);
    },
    add_to_friend_list(state, friend_to_add) {
      state.list_of_friends.push(friend_to_add);
    },
    set_name(state, name){
      state.name = name;
    },
    remove_event(state, eventId){
      let location = state.list_of_events.findIndex( event => event['id'] == eventId );
      if ( location >= 0 ) { state.list_of_events.splice(location, 1); }
      console.log(state.list_of_events)
    },
    add_comment_to_event(state, payload){
      console.log("payload: ", payload)
      let location = state.list_of_events.findIndex( event => event['id'] == payload['eventId'] );
      console.log(state.list_of_events[location])
      if ( location >= 0 ) { state.list_of_events[location].comments.push( payload['comment'] ); }
    },
    set_list_of_events(state, list){
      state.list_of_events = list;

      state.list_of_events.forEach( event => {
        let decider = ( Math.random() >= 0.5) ? 1 : -1;
        event.location.showLatitude = event.location.latitude + (decider * ( Math.random() * 0.007 ) );
        decider = ( Math.random() >= 0.5) ? 1 : -1;
        event.location.showLongitude = event.location.longitude + (decider * ( Math.random() * 0.007 ) );
      } )
    },
    set_searched_events(state, event_to_add){
      state.searchedEvents = event_to_add;
    },
    set_searched_friends(state, friend_to_add){
      state.searchedMyFriendsList = friend_to_add;
    },
    set_user(state, user){
      console.log(state)
      state.currentUser = user[0];
      console.log("The user is now:::: ", state.currentUser)
    },
    set_current_event(state, event){
      console.log("event is: ", event)
      state.current_Event = event
    },

    set_Attend(state, list){
      console.log("in set")
      state.attend = list
    }

  },

  actions: {

    get_test({commit, rootState}){
      return axios.get('http://127.0.0.1:5000/get_test')
      .then(response => {
        console.log("Response")
        console.log(response.data)
      }, (err) => {
        console.log(err)
      })
    },

    submit_comment({commit, rootState}, payload){
      return axios.post('http://127.0.0.1:5000/submit_comment',
        { params:{ comment: payload } } )
        .then(response => {
          console.log("Response")
          console.log(response.data)
          commit('add_comment_to_event', payload)
        }, (err) => {
          console.log(err)
        })
    },
    get_A_List({commit, rootState}, payload){
      return axios.post('http://127.0.0.1:5000/get_A_List',
      { params:{ event: payload } }
      )
      .then(response =>{
        console.log("Response from the store when attentd: ", response.data)
        commit('set_Attend', response.data)
      }, (err) => {
        console.log(err)
      })
    },

    save_event({commit, rootState}, payload){
      return axios.post('http://127.0.0.1:5000/save_event',
      { params:{ event: payload } }
      )
        .then(response => {
          console.log("Response")
          console.log(response.data)
          commit('add_event', response.data)
          commit('set_current_event',response.data)
        }, (err) => {
          console.log(err)
        })
    },

    addfriend_event({ commit, rootState }, payload) {
      console.log("before axios call")
      axios.post('http://127.0.0.1:5000/addfriend_event',
        { params: { name: payload, cUser: rootState.currentUser } }
      )
        .then(response => {
          console.log("AXIOS Response", response.data )
        }, (err) => {
        console.log("err", err)
      })
    },

    join_event({commit, rootState}, payload){
      return axios.post('http://127.0.0.1:5000/join_event',
      { params:{ event: payload } }
      )
      .then(response =>{
        console.log("Response: ", response.data)
      }, (err) => {
        console.log(err)
      })
    },

    delete_event({commit, rootState}, payload){
      return axios.post('http://127.0.0.1:5000/delete_event',
      { params:{ eventId: payload } }
      )
      .then(response => {
        console.log("Response: ", response.data)
        commit('remove_event', payload)
      }, (err) => {
        console.log(err)
      })
    },

    get_events({commit, rootState}){
      return axios.get('http://127.0.0.1:5000/get_events')
      .then(response => {
        console.log("Response")
        console.log(response.data)
        commit('set_list_of_events', response.data)
      }, (err) => {
        console.log(err)
      })
    },

    search_event({commit, rootState}, payload){
      return axios.post('http://127.0.0.1:5000/search_event', {
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

    search_my_friends({commit, rootState}, payload){
      return axios.post('http://127.0.0.1:5000/search_my_friends', {
        params: {friendProp: payload}
      })
      .then(response => {
        console.log("Response: ", response.data)
        commit('set_searched_friends', response.data)
        //resolve(response.data)
      }, (err) => {
        console.log(err)
      })
    },

    validate_user({commit, rootState}, payload){
      return axios.post('http://127.0.0.1:5000/validate_user', {
        params: {loginProp: payload}
      })
      .then(response => {
        console.log("Response: ", response.data)
        if (response.data){
          console.log("i am saving: ", response.data)

          commit('set_user', response.data)
        }

      }, (err) => {
        console.log(err)
      })
    },

    getName({commit, rootState}, id){
      return axios.post('http://127.0.0.1:5000/getName', {
        params: {id: id}
      })
      .then(response => {
        console.log("Response: ", response.data)
        if (response.data){
          console.log("i am saving: ", response.data)

          commit('set_name', response.data)
        }

      }, (err) => {
        console.log(err)
      })
    },

    save_user({commit, rootState}, payload){
      return axios.post('http://127.0.0.1:5000/save_user', {
        params: {signupProp: payload}
      })
      .then(response => {
        console.log("Response: ", response.data)

        if (response.data){
          console.log("i am saving: ", response.data)
          commit('set_user', response.data)
        }

      }, (err) => {
        console.log(err)
      })
    }
  }
})
