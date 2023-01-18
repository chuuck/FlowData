<template>
  
  <div id = "center_layout">
  
    <HelloWorld @change="fileChanged" msg="Welcome to Your Vue.js App"/>
    <InputPrompt @submitPrompt="update_prompt"/>
    <SQLAccordion :query="query"/>
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

      prompt: '',

      query: 'EMPTY'
    }
  },
  methods: {
      onClickChild () {
      
        let formData = new FormData()

        console.log(this.files);

        for (let index = 0; index < this.files.length; index++) {
          formData.append('file', this.files[index])
        }
      
        formData.append('prompt', this.prompt)
        
        axios.post('http://127.0.0.1:8000/upload-csv-test',
          formData, {
            headers: {
              'Content-Type': 'multipart/form-data'
            }
        }).then((response) => {

          this.query = response.data['query']
          let table_object = JSON.parse(response.data['table']);
          this.columns = Object.keys(table_object[0])
          this.people = table_object
          
          
        }, (error) => {
          console.log(error);
        });

      },

      fileChanged(uploaded_files){

        this.files = uploaded_files.target.files
      },

      update_prompt(prompt){
        this.prompt = prompt;
        this.onClickChild();
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
