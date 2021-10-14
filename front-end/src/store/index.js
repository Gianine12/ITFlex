import Vue from "vue";
import Vuex from "vuex";
// import axios from "axios";

Vue.use(Vuex);

export default new Vuex.Store({
  state: {
    lista: [],
    isModalVisible: false,
    info: {},
  },
  mutations: {
    ModalVisible(state, payload) {
      state.isModalVisible = payload;
    },
    setInfo(state, payload) {
      state.info = payload;
    }
  },
  actions: {
    ModalVisible({ commit }, value) {
      return new Promise(() => {
        commit("ModalVisible", value);
      });
    },
    setInfo({ commit }, value) {
      commit("setInfo", value);
    }
  },
  modules: {},
});
