import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

const state = {
  // single source of data
  tickets: []
}

const actions = {
  // asynchronous operations
}

const mutations = {
  // isolated data mutations
  setTickets(state, payload) {
    state.tickets = payload.tickets.data.data
  }
}

const getters = {
  // reusable data accessors
}

const store = new Vuex.Store({
  state,
  actions,
  mutations,
  getters
})

export default store
