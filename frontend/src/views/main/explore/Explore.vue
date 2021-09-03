<template>
  <v-container>
    <div class="text-h4">Projects list</div>
    <v-divider />
    <v-container>
      <v-row>
        <v-col cols="9">
          <project
            v-for="data in datas"
            :key="data.id"
            :project="data"
            class="my-2"
          />
        </v-col>

        <v-col>
          <v-card class="mt-2">
            <v-card-title>filter</v-card-title>
          </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-container>
</template>

<script lang='ts'>
import { Component, Vue } from "vue-property-decorator";
import project from "@/views/main/explore/ProjectItem.vue";

@Component({
  components: {
    project,
  },
})
export default class Explore extends Vue {
  datas = [
    {
      title: "string1",
      description: "Project 1 description",
      id: 0,
      owner_id: 0,
      members: [
        {
          user: {
            email: "user1@example.com",
            is_active: true,
            is_superuser: false,
            full_name: "user1",
            id: 0,
          },
          accepted: true,
        },
      ],
    },
    {
      title: "string2",
      description: "Project 2 description",
      id: 1,
      owner_id: 1,
      members: [
        {
          user: {
            email: "user1@example.com",
            is_active: true,
            is_superuser: false,
            full_name: "user1",
            id: 0,
          },
          accepted: true,
        },
        {
          user: {
            email: "user2@example.com",
            is_active: true,
            is_superuser: false,
            full_name: "user2",
            id: 1,
          },
          accepted: true,
        },
      ],
    },
  ];
}
</script>