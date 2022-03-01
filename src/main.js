import '@babel/polyfill';
import 'mutationobserver-shim';
// import './plugins/bootstrap-vue';
import { createApp } from 'vue';
import App from './App.vue';
import router from './router';

import 'bootstrap/dist/css/bootstrap.css';

createApp(App).use(router).mount('#app');
