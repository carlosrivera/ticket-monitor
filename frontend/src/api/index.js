import axios from 'axios'

const API_URL = 'http://localhost/api'

export function postFetchTicket(data) {
  return axios.post(`${API_URL}/ticket`, { data })
}
