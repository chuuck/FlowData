<template>

    <div id="intro_rect">
      <h1 id="title">QData</h1>
      <p id="description_text">Whether you're a data scientist, business analyst, or just someone looking to extract insights from your data, QData allows you to ask questions to your data.</p>
      
      <div id="file_upload_area" @click="selectFile()" type="button">
        <input name="elephant" class="form-control" type="file" id="formFileMultiple" ref="uploaded_files" multiple @change="onFileChange" hidden>
        <svg xmlns="http://www.w3.org/2000/svg" width="48" height="48" fill="#fff" class="bi bi-file-earmark-arrow-up" viewBox="0 0 16 16" style="margin-top: 25px;">
          <path d="M8.5 11.5a.5.5 0 0 1-1 0V7.707L6.354 8.854a.5.5 0 1 1-.708-.708l2-2a.5.5 0 0 1 .708 0l2 2a.5.5 0 0 1-.708.708L8.5 7.707V11.5z"/>
          <path d="M14 14V4.5L9.5 0H4a2 2 0 0 0-2 2v12a2 2 0 0 0 2 2h8a2 2 0 0 0 2-2zM9.5 3A1.5 1.5 0 0 0 11 4.5h2V14a1 1 0 0 1-1 1H4a1 1 0 0 1-1-1V2a1 1 0 0 1 1-1h5.5v2z"/>
        </svg>

        <p style="color: #fff; margin-top: 15px; font-size:14px; font-weight: 600;">{{message}}</p>
        

      </div>

   
      
    </div>

</template>

<script>
export default {
  name: 'HelloWorld',
  props: {
    msg: String
  },
  data(){
    return{
      files: [],
      message: 'Click here to add CSV files',
    }
  },
  methods:{
    onFileChange(){
      this.message_changed(this.$refs.uploaded_files.files.length)
      this.$emit('fileChanged', this.$refs.uploaded_files.files)
      
    },

    selectFile() {
      let fileInputElement = this.$refs.uploaded_files;
      fileInputElement.click();
    },

    message_changed(file_list_length){
      console.log(file_list_length)
      if (file_list_length == 1){
        this.message = file_list_length.toString() + ' file added'
      }else{
        this.message = file_list_length.toString() + ' files added'
      }
    }

  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

#intro_rect{
  height: 370px;
  max-width:1000px;
  display: block;
  margin-left: auto;
  margin-right: auto;
  background: rgb(69,137,255);
  background: linear-gradient(45deg, rgba(69,137,255,1) 0%, rgba(8,189,186,1) 100%);
  border-radius: 25px;
}

#title{
  color:white;
  padding-top:40px;
}



#description_text{
  padding-top:20px;
  padding-left:100px;
  padding-right:100px;
  color:white;
}


#file_upload_area{

  border-width:3px;
  border-style:dashed;
  border-color:#FFF;
  height: 140px;
  margin-left: 120px;
  margin-right: 120px;
  margin-top: 30px;
}

#file_upload_area:hover{

  background-color: #b5d3f4;
}
</style>
