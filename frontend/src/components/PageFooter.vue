<template>
  <v-footer bottom absolute padless app>
    <v-col class="text-center" cols="12">
      {{ new Date().getFullYear() }} — <strong>StartUp-Together</strong>
    </v-col>
  </v-footer>
</template>

<script>
export default {
  data() {
    return {
      icons: [
        "mdi-instagram",
        "fab fa-twitter",
        "fab fa-google-plus",
        "fab fa-linkedin",
        "fab fa-instagram",
      ],
    };
  },
};
</script>

<style>
</style>
