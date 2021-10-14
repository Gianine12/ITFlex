import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import store from "./store";

import "spectre.css/dist/spectre.min.css";
import "spectre.css/dist/spectre-icons.min.css";

Vue.config.productionTip = false;

new Vue({
  store,
  router,
  render: (h) => h(App),
}).$mount("#app");
