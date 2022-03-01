import { createRouter, createWebHistory } from 'vue-router';

const routes = [
  {
    path: '/',
    name: 'Books',
    component: () => import('../components/Books.vue'),
  },
  {
    path: '/get',
    name: 'Get',
    component: () => import('../views/Get.vue'),
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
