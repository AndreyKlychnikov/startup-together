<template>
  <v-app id="inspire">

    <toolbar />

    <v-main>
      
      <router-view />
      
    </v-main>

    <page-footer />

  </v-app>
</template>
<script lang="ts">
import { Component, Vue } from "vue-property-decorator";
import pageFooter from "@/components/PageFooter.vue";
import toolbar from "@/components/Toolbar.vue";

@Component({
  components: {
    pageFooter,
    toolbar,
  },
})
export default class Main extends Vue {
  
}
</script>
<style lang="">
</style>
