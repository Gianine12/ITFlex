<template>
  <div>
    <h1>Cadastrados</h1>
    <table class="table table-striped table-hover table-scroll">
      <thead>
        <tr>
          <th>Name</th>
          <th>Username</th>
          <th>Expiration</th>
          <th>Expirated</th>
          <th>Created</th>
          <th></th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="item in items" :key="item.id">
          <td>{{ item.name }}</td>
          <td>{{ item.username }}</td>
          <td>{{ item.expiration }}</td>
          <td>{{ item.expirated_at }}</td>
          <td>{{ item.created_at }}</td>
          <td>
            <button @click="deleteList(item.id)" class="btn btn-action">
              <i class="icon icon-delete" />
            </button>
            <button @click="edit()" class="btn btn-action">
              <i class="icon icon-edit" />
            </button>
          </td>
          <Modal v-if="visible" v-bind:item="item" />
        </tr>
      </tbody>
    </table>
  </div>
</template>
<script>
import axios from "axios";
import Modal from "./Modal.vue";

export default {
  name: "List",
  data() {
    return {
      items: {},
      data: {},
    };
  },
  components: {
    Modal,
  },
  created: function () {
    this.consultaLista();
  },
  mounted: function () {
    window.setInterval(() => {
      this.consultaLista();
    }, 30000);
  },
  methods: {
    consultaLista() {
      axios
        .get("http://localhost:5000/api/list")
        .then((response) => {
          this.items = response.data;
        })
        .catch(() => {
          console.log("error");
        });
    },

    edit() {
      this.$store.dispatch("ModalVisible", true);
    },

    deleteList(id) {
      axios
        .delete(`http://localhost:5000/api/delete/${id}`)
        .then(() => {})
        .catch((erro) => {
          console.log(erro);
        });
    },
  },
  computed: {
    visible() {
      return this.$store.state.isModalVisible;
    },
  },
};
</script>
<style scoped>
table {
  min-width: 1000px;
}
img {
  width: 30px;
}
</style>
