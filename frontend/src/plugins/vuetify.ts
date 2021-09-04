import Vue from 'vue';
import Vuetify from 'vuetify';


Vue.use(Vuetify)

const vuetify = new Vuetify({
  iconfont: 'md',
  theme: {
    themes: {
      light: {
        primary: '#3f51b5',
        secondary: '#b0bec5',
        anchor: '#448aff',
      },
    },
  },
})

export default vuetify
