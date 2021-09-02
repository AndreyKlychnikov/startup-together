<template>
  <div>
    <v-row class="mt-6" no-gutters>
      <v-col></v-col>

      <v-col cols="6">
        <project-item v-for="data in datas" :key="data.id" :project="data" />
      </v-col>

      <v-col class="center--text"> filter column </v-col>
    </v-row>
  </div>
</template>

<script lang='ts'>
import { Component, Vue } from "vue-property-decorator";
import projectItem from "@/views/main/explore/ProjectItem.vue";

@Component({
  components: {
    projectItem,
  },
})
export default class Explore extends Vue {
  datas = [
    {
      title: "string1",
      description: "string",
      id: 0,
      owner_id: 0,
      members: [
        {
          user: {
            email: "user@example.com",
            is_active: true,
            is_superuser: false,
            full_name: "string",
            id: 0,
          },
          accepted: true,
        },
      ],
    },{
      title: "string2",
      description: "string",
      id: 0,
      owner_id: 0,
      members: [
        {
          user: {
            email: "user@example.com",
            is_active: true,
            is_superuser: false,
            full_name: "string",
            id: 0,
          },
          accepted: true,
        },
      ],
    },
  ];
}
</script>