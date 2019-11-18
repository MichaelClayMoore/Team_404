import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'
import EventCreator from './views/eventCreator.vue'
import SearchEvent from './views/searchEvent.vue'
import Test from './views/test.vue'

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
      path: '/eventCreator',
      name: 'eventCreator',
      // route level code-splitting
      // this generates a separate chunk (about.[hash].js) for this route
      // which is lazy-loaded when the route is visited.
      component: EventCreator
    },
    {
      path: '/searchEvent',
      name: 'searchEvent',
      component: SearchEvent
    },
    {
    path: '/test',
      name: 'test',
      component: Test
    }
  ]
})
