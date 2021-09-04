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
            v-for="data in datas"
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

@Component({
  components: {
    project,
  },
})
export default class Explore extends Vue {
  datas = [
    {
      title: "fastapi",
      description: "FastAPI is a modern, fast (high-performance), web framework for building APIs with Python 3.6+ based on standard Python type hints.",
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
      categories: [
        {
          value: "Rest Api"
        }
      ]
    },
    {
      title: "django",
      description: "The Web framework for perfectionists with deadlines. ",
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
      categories: [
        {
          value: "Python"
        },{
          value: "Backend"
        },{
          value: "REST Api"
        },
      ]
    },
  ];
}
</script>
