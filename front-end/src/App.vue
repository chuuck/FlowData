<template>
  
  <div id = "center_layout">
  
    <HelloWorld @change="fileChanged" msg="Welcome to Your Vue.js App"/>
    <InputPrompt @submitPrompt="onClickChild"/>
    <SQLAccordion/>
    <ResponseTable :people="people" :columns="columns"/>

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
  data(){
    return{
      files: '',

      columns: ['name', 'age', 'address'],

      people: [['John Doe', 30, '123 Main St' ],
              [ 'Jane Smith', 105, '456 Park Ave' ],
              [ 'Bob Johnson', 35, '789 Elm St' ]],


      // people: [{ 'name': 'John Doe', 'age': 30, 'address': '123 Main St' },
      //         { 'name': 'Jane Smith', 'age': 105, 'address': '456 Park Ave' },
      //         { 'name': 'Bob Johnson', 'age': 35, 'address': '789 Elm St' }],
    }
  },
  methods: {
      onClickChild () {
        
        let formData = new FormData();
        formData.append("file", this.files);
        
        axios.post('http://127.0.0.1:8000/upload-csv-test',
          formData, {
            headers: {
              'Content-Type': 'multipart/form-data'
            }
        }).then((response) => {
          
          this.columns = Object.keys(response.data[0])
          this.people = response.data
          console.log(response)
        
          
        }, (error) => {
          console.log(error);
        });
        

        /* Posting a string
        axios.post('http://127.0.0.1:5000/ping', {
          firstName: value,
          lastName: 'Williams'
        })
        .then((response) => {
          console.log(response);
        }, (error) => {
          console.log(error);
        });*/

      },

      fileChanged(uploaded_files){

        this.files = uploaded_files.target.files[0]
        
        
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
