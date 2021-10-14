<template>
  <div class="about">
    <List />
  </div>
</template>
<script>
// @ is an alias to /src
import List from "@/components/List.vue";

export default {
  name: "Home",
  components: {
    List,
  },
};
</script>
