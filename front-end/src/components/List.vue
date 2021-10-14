<template>
  <div class="principal">
    <h1>Cadastrados</h1>
    <table class="table-hover table-scroll tb-header">
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
            <button @click="edit(item)" class="btn btn-action">
              <i class="icon icon-edit" />
            </button>
          </td>
          <Modal v-if="visible" />
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

    edit(item) {
      this.$store.dispatch("ModalVisible", true);
      this.$store.dispatch("setInfo", item);
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
.principal {
  text-align: center;
}
table {
  border: 1px solid #DFE3E6;
  border-collapse: collapse;
  width: 96%;
  margin: auto;
  /* padding: 8px; */
}

.tb-header {
  background: #DFE3E6;
}
.tb-header:hover {
  background: #DFE3E6;
}

th,
td {
  height: 32px;
  padding: 8px;
}

tr {
  border: 1px solid #DFE3E6;
}

tr:hover {
  background:#F9FAFB;
}

thead {
  background: white;
}
img {
  width: 30px;
}
</style>
