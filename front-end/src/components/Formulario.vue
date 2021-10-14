<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <form @submit="submit">
      <div class="form-group">
        <label class="form-label" for="input-example-1">Username</label>
        <input
          class="form-input"
          type="text"
          placeholder="Username"
          maxlength="30"
          v-model="item.username"
        />
      </div>
      <div class="form-group">
        <label class="form-label" for="input-example-1">Name</label>
        <input
          class="form-input"
          type="text"
          placeholder="Name"
          v-model="item.name"
        />
      </div>
      <div class="form-group">
        <label class="form-label" for="input-example-3">Description </label>
        <textarea
          class="form-input"
          placeholder="Textarea"
          rows="3"
          maxlength="255"
          v-model="item.description"
        />
      </div>
      <div class="form-group">
        <label class="form-label" for="input-example-1">Groups</label>
        <select class="form-select" v-model="item.groups">
          <option value="1">Adm</option>
          <option value="15">Comercial</option>
          <option value="30">RH</option>
        </select>
      </div>
      <div class="form-group">
        <label class="form-label" for="input-example-1">Expiration </label>
        <input
          class="form-input"
          type="number"
          placeholder="Expiration"
          v-model="item.expiration"
        />
      </div>
      <button class="btn">Cadastrar</button>
    </form>
  </div>
</template>

<script>
import axios from "axios";

export default {
  name: "Formulario",
  data() {
    return {
      item: {
        username: "",
        name: "",
        description: "",
        groups: "",
        expiration: "",
      },
    };
  },
  props: {
    msg: String,
  },
  methods: {
    submit() {
      axios
        .post("http://localhost:5000/api/create", {
          username: this.item.username,
          name: this.item.name,
          description: this.item.description,
          groups: this.item.groups,
          expiration: this.item.expiration,
          expirated_at: (Date.now() + (this.item.expiration * 86400000)) / 1000,
          created_at: Date.now() / 1000,
          updated_at: Date.now() / 1000,
        })
        .then(() => {})
        .catch((error) => {
          console.log(error);
        });
    },
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
form {
  width: 95%;
  border: 1px solid lavender;
  padding: 10px;
  border-radius: 15px;
  background: #fff;
  margin: auto;
}

h1 {
  text-align: center;
}
/* @media (min-width: 500px) {
  form {
    width: 90%;
  }
} */
</style>
