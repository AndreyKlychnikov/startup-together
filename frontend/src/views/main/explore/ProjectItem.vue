<template>
  <v-card>
    <v-card-title>
      <router-link class="text-decoration-none" :to="'project/id' + project.id.toString()">
        {{ project.title }}
      </router-link>
    </v-card-title>
    <v-card-subtitle>{{
      project.members.find((member) => member.user.id == project.owner_id).user
        .full_name
    }}</v-card-subtitle>
    <v-card-text>{{ project.description }}</v-card-text>
    <v-card-actions> </v-card-actions>
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