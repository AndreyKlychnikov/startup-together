<template>
  <div>
    {{ project.title }}
  </div>
</template>

<script lang='ts'>
import { Component, Vue } from "vue-property-decorator";
import { IProjectItem } from "@/interfaces";

@Component({
    props:[
        'project'
    ]
})
export default class ProjectItem extends Vue {
    project!: IProjectItem
}
</script>