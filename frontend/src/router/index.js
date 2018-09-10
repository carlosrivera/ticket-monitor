import Vue from 'vue'
import Router from 'vue-router'
import Home from '@/components/Home'
import Ticket from '@/components/Ticket'

Vue.use(Router)

export default new Router({
  routes: [
    {
      path: '/',
      name: 'Home',
      component: Home
    }, {
      path: '/tickets',
      name: 'Ticket',
      component: Ticket
    }
  ]
})
