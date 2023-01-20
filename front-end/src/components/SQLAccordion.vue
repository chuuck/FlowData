<template>

    <div class="accordion" id="sql_accordion">
        <div class="accordion-item">
            <h2 class="accordion-header" id="headingOne">
            <button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#collapseOne" aria-expanded="true" aria-controls="collapseOne">
                SQL
            </button>
            </h2>
            <div id="collapseOne" class="accordion-collapse collapse show" aria-labelledby="headingOne" data-bs-parent="#accordionExample">
            <div class="accordion-body">
                <pre><code class="language-javascript" language="javascript">
function myFunction() {
  document.getElementById("demo").innerHTML = "Paragraph changed.";
}
                </code></pre>

            </div>
            </div>
        </div>
    </div>
</template>

<script>
import Prism from "prismjs";
import "prismjs/themes/prism.css";


export default {
  name: 'SQLAccordion',
  props: {
      query: String,
  },
  mounted() {
    window.Prism = window.Prism || {};
    window.Prism.manual = true;
    Prism.highlightAll(); // highlight your code on mount
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
#sql_accordion{
  margin-top:40px;
  width: 600px;
  margin-left: 50%;
  -ms-transform: translate(-50%, 0%);
  transform: translate(-50%, 0%);
  
}



</style>
