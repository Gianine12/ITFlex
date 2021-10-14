import axios from "axios";

export default {
  ConsultaLista() {
    return axios
      .get("http://localhost:5000/")
      .then((response) => {
        console.log(response.data);
      })
      .catch(() => {
        console.log("error");
      });
  },
};
