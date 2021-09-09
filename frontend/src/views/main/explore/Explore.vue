<template>
  <v-container>
    <v-row class="mt-2">
      <v-col cols="3" class="mt-2">
        <v-card>
          <v-card-title>filter</v-card-title>
        </v-card>
      </v-col>
      <v-col cols="8">
        <project
            v-for="data in projects"
            :key="data.id"
            :project="data"
            class="my-2"
        />
      </v-col>
    </v-row>
  </v-container>
</template>

<script lang='ts'>
import { Component, Vue } from "vue-property-decorator";
import project from "@/views/main/explore/ProjectItem.vue";
import { readProjects } from '@/store/explore/getters';
import { dispatchGetProjects } from '@/store/explore/actions';

@Component({
  components: {
    project,
  },
})
export default class Explore extends Vue {

  get projects() {
    return readProjects(this.$store);
  }
  public async mounted() {
    await dispatchGetProjects(this.$store);
  }
}
</script>
