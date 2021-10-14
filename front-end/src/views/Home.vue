<template>
  <div class="home">
    <Formulario msg="Cadastro" />
  </div>
</template>

<script>
// @ is an alias to /src
import Formulario from "@/components/Formulario.vue";

export default {
  name: "Home",
  components: {
    Formulario,
  },
};
</script>
