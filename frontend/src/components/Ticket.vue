<template>
<div>
  <section class="hero is-primary">
    <div class="hero-body">
      <div class="container has-text-centered">
        <h2 class="title">Lista de multas.</h2>
      </div>
    </div>
  </section>
  <section class="section">
    <div class="container">
      <div class="columns">
        <div class="column is-8 is-offset-2">

          <article class="message is-danger" v-if="tickets">
            <div class="message-header">
              <p>Hay multas registradas</p>
            </div>
            <div class="message-body">
              Se encontraron las siguientes infracciones relacionadas con el vehículo.
            </div>
          </article>
          <article class="message is-success" v-else>
            <div class="message-header">
              <p>No hay multas registradas</p>
            </div>
            <div class="message-body">
              No se encontró ninguna infracción registrada para ese vehículo.
            </div>
          </article>

        </div>
      </div>

      <div class="columns" v-for="ticket in tickets" v-bind:key="ticket.description">
        <div class="column is-8 is-offset-2">

          <div class="card">
            <div class="card-content">
              <p class="title">${{ ticket.due }}</p>
              <p class="subtitle">{{ ticket.number }}</p>
              <p class="lead">{{ ticket.description }}</p>
            </div>
          </div>

        </div>
      </div>

      <div class="columns">
        <div class="column is-8 is-offset-2">

          <div class="field">
            <div class="control">
              <button class="button is-link" @click="handleBack">Volver al inicio</button>
            </div>
          </div>

        </div>
      </div>

    </div>
  </section>
  <footer class="footer has-text-centered">
    <div class="container">
      <div class="columns">
        <div class="column is-8 is-offset-2">
          Made with <i class="has-text-danger"><font-awesome-icon icon="heart" /></i> from <a href="https://synx.co" target="_blank">Synx</a>.
        </div>
      </div>
    </div>
  </footer>
</div>
</template>

<script>
import { mapState } from 'vuex'
export default {
  name: 'Ticket',
  computed: mapState({
    tickets: state => state.tickets
  }),
  methods: {
    handleBack() {
      this.$router.push('/')
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
