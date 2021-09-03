<template>
    <div>
        Project with id {{this.$route.params.id}}
    </div>
</template>

<script lang='ts'>
import { Component, Vue } from 'vue-property-decorator';

@Component
export default class Project extends Vue {

}
</script>