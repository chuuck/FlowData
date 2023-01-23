<template>

    
    <!-- Table where the response from Codex is displayed -->
    <div id = "table_box">

    <button id = "download_button" type="button" class="btn btn-primary" @click="dowload_action">Download</button>

        <table id="response_table" class="table table-striped">
          <thead id="table_thread">
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

import Papa from 'papaparse';

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

      console.log(this.people)

      // combine columns and rows
      let data = [this.columns, ...this.people];

      // convert array to csv
      let csv = Papa.unparse(data);

      // download csv file
      let blob = new Blob([csv], { type: 'text/csv;charset=utf-8;' });
      let link = document.createElement("a");
      let url = URL.createObjectURL(blob);
      link.setAttribute("href", url);
      link.setAttribute("download", "data.csv");
      link.style.visibility = 'hidden';
      document.body.appendChild(link);
      link.click();
      document.body.removeChild(link);

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

.btn-primary:hover, .btn-primary:focus, .btn-primary:active, .btn-primary.active, .open>.dropdown-toggle.btn-primary {
    color: #fff;
    background-color: #00b3db;
    border-color: #285e8e; /*set the color you want here*/
}

.btn:focus,.btn:active:focus,.btn.active:focus,
.btn.focus,.btn:active.focus,.btn.active.focus {
    outline: none;
}

#download_button{

  margin-left: 100%;
  background: #fff;
  color: #626b73;  
}

#download_button:hover{
  background: #33A2DD;
  color: #fff;
}

#table_thread{

  color: white;
  background: #33A2DD;
}

#response_table{
  margin-top:1vw;
  margin-left: 50%;
  -ms-transform: translate(-50%, 0%);
  transform: translate(-50%, 0%);
  margin-bottom: 5vw;
}


</style>
