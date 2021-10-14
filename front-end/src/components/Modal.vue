<template>
  <div class="modal active" id="modal-id">
    <a href="#close" class="modal-overlay" aria-label="Close"></a>
    <div class="modal-container">
      <div class="modal-header">
        <a
          @click="close()"
          class="btn btn-clear float-right"
          aria-label="Close"
        ></a>
        <div class="modal-title h5">Editar</div>
      </div>
      <div class="modal-body">
        <div class="content">
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
            <button class="btn">Salvar</button>
          </form>
        </div>
      </div>
      <div class="modal-footer">...</div>
    </div>
  </div>
</template>
<script>
export default {
  name: "Modal",
  methods: {
    close() {
      this.$store.dispatch("ModalVisible", false);
    },
    update() {
      console.log("update");
    },
  },
  props: {
    item: Object,
  },
};
</script>
