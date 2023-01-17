<template>

    <div id="intro_rect">
      <h1 id="title">QData</h1>
      <p id="description_text">Whether you're a data scientist, business analyst, or just someone looking to extract insights from your data, QData allows you to ask questions to your data.</p>
      <div id="file_upload_area">
        <input name="elephant" class="form-control" type="file" id="formFileMultiple" ref="uploaded_files" multiple @change="onFileChange">
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
    }
  },
  methods:{
    onFileChange(){
      
      this.$emit('fileChanged', this.$refs.uploaded_files.files[0])
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

#intro_rect{
  height: 300px;
  max-width:1000px;
  display: block;
  margin-left: auto;
  margin-right: auto;
  background: rgb(130,106,252);
  background: linear-gradient(90deg, rgba(130,106,252,1) 0%, rgba(130,106,252,1) 0%, rgba(235,136,252,1) 100%);
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

  padding-top:40px;
  padding-left:200px;
  padding-right:200px;
}
</style>
