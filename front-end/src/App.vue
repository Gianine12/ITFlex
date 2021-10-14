<template>
  <div id="app">
    <div class="navbar backroung">
      <div class="navbar-section">
        <router-link class="btn btn-link navbar-brand mr-2" to="/">Cadastro</router-link> |
        <router-link class="btn btn-link navbar-brand mr-2" to="/list">Listagem</router-link>
      </div>
    </div>
    <router-view />
  </div>
</template>

<style>
.backroung {
  background: orange;
  color: aliceblue;
  display: flex;
}
#app {
  background: rgb(172,172,172);
  background: linear-gradient(90deg, rgba(172,172,172,1) 0%, rgba(132,132,136,1) 56%, rgba(83,87,88,1) 100%);
  width: 100%;
  height: 100%;
}
html {
  width: 100%;
  height: 100%;
}
body {
  margin: 0px;
  width: 100%;
  height: 100%;
}
</style>
