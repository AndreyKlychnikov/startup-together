<template>
  <v-app-bar absolute color="#6A76AB" dark app>
    <!-- <v-app-bar-nav-icon></v-app-bar-nav-icon> -->

    <v-app-bar-title>StartUp Together</v-app-bar-title>

    <v-spacer></v-spacer>

    <v-tabs centered>
      <v-tab to="explore">Explore</v-tab>
      <v-tab to="ideas">Ideas</v-tab>
      <v-tab>Projects</v-tab>
    </v-tabs>

    <v-spacer />

    <v-menu left bottom>
      <template v-slot:activator="{ on, attrs }">
        <v-btn icon v-bind="attrs" v-on="on">
          <v-avatar size="36">
            <img src="https://cdn.vuetifyjs.com/images/john.jpg" alt="John" />
          </v-avatar>
        </v-btn>
      </template>

      <v-list>
        <v-list-item-group>
          <v-list-item>
            <v-list-item-content>
              <v-list-item-title 
                >My projects
              </v-list-item-title>
            </v-list-item-content>
          </v-list-item>
          <v-list-item>
            <v-list-item-content>
              <v-list-item-title>Profile </v-list-item-title>
            </v-list-item-content>
          </v-list-item>
          <v-list-item>
            <v-list-item-content>
              <v-list-item-title>Settings </v-list-item-title>
            </v-list-item-content>
          </v-list-item>
          <v-list-item>
            <v-list-item-content>
              <v-list-item-title @click="logout">LogOut </v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-menu>
  </v-app-bar>
</template>

<script lang='ts'>
import { Component, Vue } from "vue-property-decorator";
import { dispatchUserLogOut } from "@/store/main/actions";

@Component
export default class Toolbar extends Vue {
  public async logout() {
    await dispatchUserLogOut(this.$store);
  }
}
</script>