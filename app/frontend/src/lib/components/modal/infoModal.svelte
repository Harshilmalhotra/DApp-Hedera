<script>
    import { Button, Modal } from "carbon-components-svelte";

    export let heading = ""
    export let content = ""
  
    let open = true;
  </script>
  
  <Modal passiveModal bind:open modalHeading="{heading}" on:open on:close>
    <p>
     {content} </p>
  </Modal>
  