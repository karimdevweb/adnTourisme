import { createRouter, createWebHistory} from 'vue-router';
import HomeComponent from '@/components/home/HomeComponent.vue';
import MainGraphComponent from '@/components/MainGraphComponent/MainGraphComponent.vue';
import MlComponent from '@/components/ml/MlComponent.vue'
import NotFoundComponent from '@/components/notFound/NotFoundComponent.vue'






const routes = [
    {
        name:'Home',
        path: '/',
        component:HomeComponent,
        meta: {
            title : 'home'
        }
    },

    {
        name:'Dashboard',
        path: '/dashboard',
        component:MainGraphComponent,
        meta: {
            title : 'dashboard'
        }
    },
    {
        name:'Machine Learning',
        path: '/machine_learning',
        component:MlComponent,
        meta: {
            title : 'Machine Learning'
        }
    },

    {
        name:'NotFound',
        path: '/:pathMatch(.*)',
        component:NotFoundComponent,
        meta: {
            title : '404'
        }
    },

];



const router = createRouter({
    history: createWebHistory(),
    routes,

})


export default router; 



