<template>

    <div class="input-group mb-3" id="prompt_form">
      <input id="prompt_input" type="text" class="form-control" placeholder="Enter your prompt..." aria-label="Recipient's username" aria-describedby="basic-addon2" v-model="prompt_value">
      <div class="input-group-append" id = "prompt_start_button">
          <button class="btn btn-outline-secondary" type="button" @click="submit_prompt">Go</button>
      </div>
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
      this.$emit('submitPrompt', this.prompt_value)
    }
  },
  data(){
    return{
      prompt_value: '',
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

#prompt_form{

  margin-top:125px;
  width: 800px;
  left: 50%;
  -ms-transform: translate(-50%, 0%);
  transform: translate(-50%, 0%);
}

#prompt_start_button{

  
}

</style>
