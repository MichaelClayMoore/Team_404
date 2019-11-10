import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import EventCreator from './views/eventCreator.vue'
import JoinParty from './views/joinParty.vue'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/about',
      name: 'about',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/About.vue')
    },
    {

      path: '/joinParty',
      name: 'joinParty',

      component: JoinParty
    },
    {

      path: '/event_creator',
      name: 'eventCreator',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/eventCreator.vue')
    },
    {
      path: '/friendsHub',
      name: 'friendsHub',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/friendsHub.vue')
    },
    {
      path: '/fh_AddFriend',
      name: 'fh_AddFriend',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/fh_AddFriend.vue')
    },
    {
      path: '/fh_Online',
      name: 'fh_Online',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/fh_Online.vue')
    },
    {
      path: '/fh_All',
      name: 'fh_All',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/fh_All.vue')
    },
    {
      path: '/fh_Pending',
      name: 'fh_Pending',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/fh_Pending.vue')
    },
    {
      path: '/searchEvent',
      name: 'searchEvent',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: () => import(/* webpackChunkName: "about" */ './views/searchEvent.vue')
    }
  ]
})
