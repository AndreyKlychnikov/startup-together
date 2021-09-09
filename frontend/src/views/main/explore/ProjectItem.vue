<template>
  <v-card>
    <v-container>
      <v-card-title class="py-1">
        <router-link class="text-decoration-none" :to="'project/' + project.id.toString()">
          <div class="d-inline font-weight-light">
            {{project.members.find((member) => member.user.id === project.owner_id).user.full_name}}/</div>
          <div class="d-inline font-weight-bold">{{ project.title }}</div><v-icon color="orange">mdi-fire</v-icon>
        </router-link>
      </v-card-title>
      <v-card-text class="pb-3 pb-sm-0">
        <div class="text--primary">
          {{ project.description }}
        </div>
        <v-chip-group>
          <v-chip small v-for="category in project.categories" :key="category.value" color="primary">{{ category.value }}</v-chip>
        </v-chip-group>
      </v-card-text>
    </v-container>
  </v-card>
</template>

<script lang='ts'>
import { Component, Vue } from "vue-property-decorator";
import { IProject } from "@/interfaces";

@Component({
  props: ["project"],
})
export default class ProjectItem extends Vue {
  project!: IProject;
}
</script>
