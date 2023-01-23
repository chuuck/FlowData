<template>

    <div class="input-group mb-3" id="prompt_form">


      <input id="prompt_input" type="text" class="form-control" placeholder="Enter your prompt..." 
      aria-label="Recipient's username" aria-describedby="basic-addon2" v-model="prompt_value">

      <button id="prompt_start_button" class="btn btn-primary" type="button" @click="submit_prompt">
        <span class="spinner-border spinner-border-sm" role="status" aria-hidden="true" v-if="seen_loading"></span>
        <span class="sr-only" v-if="seen_text">Go</span>
      </button>

    </div>

   
</template>

<script>
export default {
  name: 'InputPrompt',
  props: {
    msg: String,
  },
  methods: {
    submit_prompt(){
      console.log(this.prompt_value)
      this.$emit('submitPrompt', this.prompt_value)
    },
   
    switch_loading_state(is_loading){
      if (is_loading){
        this.seen_loading = true
        this.seen_text = false
      }else{
        this.seen_loading = false
        this.seen_text = true
      }
    }
  },
  data(){
    return{
      prompt_value: '',
      seen_loading: false,
      seen_text: true
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

#prompt_form{

  margin-top:100px;
  width: 800px;
  left: 50%;
  -ms-transform: translate(-50%, 0%);
  transform: translate(-50%, 0%);
}

#prompt_start_button{

  background-color:#33A2DD;
}

#prompt_input{

 height: 50px;
}


</style>
