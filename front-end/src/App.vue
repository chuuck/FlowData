<template>
  
  <div id = "center_layout">
  
    <HelloWorld msg="Welcome to Your Vue.js App"/>
    <InputPrompt @submitPrompt="onClickChild"/>
    <SQLAccordion/>
    <ResponseTable/>

  </div>
</template>

<script>
import HelloWorld from './components/HelloWorld.vue'
import InputPrompt from './components/InputPrompt.vue'
import SQLAccordion from './components/SQLAccordion.vue'
import ResponseTable from './components/ResponseTable.vue'
import axios from 'axios'

export default {
  name: 'App',
  components: {
    HelloWorld, InputPrompt, SQLAccordion, ResponseTable
  },
  methods: {
      onClickChild (value) {

        /*
        console.log(value)
        const path = 'http://127.0.0.1:5000/ping';
        axios.get(path)
          .then((res) => {
            console.log(res.data);
            this.msg = res.data;
          })
          .catch((error) => {
            // eslint-disable-next-line
            console.error(error);
          });*/

        axios.post('http://127.0.0.1:5000/ping', {
          firstName: value,
          lastName: 'Williams'
        })
        .then((response) => {
          console.log(response);
        }, (error) => {
          console.log(error);
        });
      }
  }
}
</script>

<style>


#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}


#center_layout{

  margin-left: 15%;
  margin-right: 15%;

}


</style>
