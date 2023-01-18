<template>

    
    <!-- Table where the response from Codex is displayed -->
    <div id = "table_box">

    <button id = "download_button" type="button" class="btn btn-info" @click="dowload_action">Download</button>

        <table id="response_table" class="table">
          <thead>
            <tr>
              <th v-for="column in columns" :key="column">{{ column }}</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="person in people" :key="person">
              <td v-for="person_data in person" :key="person_data">{{ person_data }}</td>
            </tr>
          </tbody>
        </table>
    </div>

</template>

<script>
export default {
  name: 'ResponseTable',
  props: {
    msg: String,
    people: Array,
    columns: Array
  },
  methods: {
    dowload_action(){
      console.log("Downloading table as CSV")
    }
  },
  data(){
    return{

    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

#table_box{

  margin-top:40px;
  margin-left: 50%;
  -ms-transform: translate(-50%, 0%);
  transform: translate(-50%, 0%);
}

#prompt_start_button{

  
}

#download_button{
  
  margin-left: 100%;

}

#response_table{
  margin-top:1vw;
  margin-left: 50%;
  -ms-transform: translate(-50%, 0%);
  transform: translate(-50%, 0%);
  margin-bottom: 5vw;
}


</style>
