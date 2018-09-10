<template>
<div>
  <section class="hero is-primary">
    <div class="hero-body">
      <div class="container has-text-centered">
        <h2 class="title">Verifica tus multas.</h2>
      </div>
    </div>
  </section>
  <section class="section">
    <div class="container">
      <div class="columns">
        <div class="column is-6 is-offset-3">
          <article class="">
            <div class="">
              <p>Verifica el estado de tu vehículo y recibe notificaciones cuando tengas una nueva multa, para comenzar ingresa tu placa, los últimos 5 digitos del número de serie, y un correo para recibir notificaciones.</p>
            </div>
          </article>
        </div>
      </div>
      <div class="columns">
        <div class="column is-6 is-offset-3">

          <article class="message is-danger" v-if="error">
            <div class="message-header">
              <p>Error</p>
            </div>
            <div class="message-body">
              Existió un error al solicitar tus datos, verifica que la información sea correcta e intenta nuevamente.
            </div>
          </article>

          <div class="field">
            <label class="label">Placa</label>
            <div class="control">
              <input class="input" type="text" placeholder="Placa del vehículo" v-model="plate">
            </div>
          </div>

          <div class="field">
            <label class="label">Número de serie</label>
            <div class="control">
              <input class="input" type="text" placeholder="Número de serie" v-model="serial">
            </div>
          </div>

          <div class="field">
            <label class="label">Email</label>
            <div class="control">
              <input class="input" type="text" placeholder="Email" v-model="email">
            </div>
          </div>

          <div class="field">
            <div class="control">
              <label class="checkbox">
                <input type="checkbox">
                 Notificarme cuando reciba una infracción<a href="#" v-model="update">.</a>
              </label>
            </div>
          </div>

          <div class="field is-grouped">
            <div class="control">
              <button class="button is-link" @click="handleSubmit">Enviar</button>
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
import { postFetchTicket } from '@/api'

export default {
  name: 'Home',
  data () {
    return {
      plate: '',
      serial: '',
      email: '',
      update: '',
      error: false
    }
  },
  methods: {
    handleSubmit() {
      postFetchTicket({
          plate: this.plate,
          serial: this.serial,
          email: this.email,
          update: this.update
        })
        .then((response) => {
            this.$store.commit('setTickets', { tickets: response });
            this.$router.push('/tickets');
        }, (error)  => {
          this.error = true;
        })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
