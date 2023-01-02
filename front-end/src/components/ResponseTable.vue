<template>

    
    <!-- Table where the response from Codex is displayed -->
    <div id = "table_box">

    <button id = "download_button" type="button" class="btn btn-info" @click="dowload_action">Download</button>

        <table id="response_table" class="table">
          <thead>
            <tr>
              <th scope="col">#</th>
              <th scope="col">First</th>
              <th scope="col">Last</th>
              <th scope="col">Handle</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <th scope="row">1</th>
              <td>Mark</td>
              <td>Otto</td>
              <td>@mdo</td>
            </tr>
            <tr>
              <th scope="row">2</th>
              <td>Jacob</td>
              <td>Thornton</td>
              <td>@fat</td>
            </tr>
            <tr>
              <th scope="row">3</th>
              <td>Larry</td>
              <td>the Bird</td>
              <td>@twitter</td>
            </tr>
          </tbody>
        </table>
    </div>

</template>

<script>
export default {
  name: 'ResponseTable',
  props: {
    msg: String
  },
  methods: {
    dowload_action(){
      console.log("Downloading table as CSV")
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

  display: block;
  margin-left: auto;
  margin-right: 0;

}

#response_table{
  margin-top:1vw;

}


</style>
