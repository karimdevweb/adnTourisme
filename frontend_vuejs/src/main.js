import { createApp } from 'vue'
import { FontAwesomeIcon } from '@fortawesome/vue-fontawesome' 
import { library } from '@fortawesome/fontawesome-svg-core'
import { fas } from '@fortawesome/free-solid-svg-icons'
import  axios from 'axios'

//  you have to import  the store simply here and add it into our  app, use(store)
import store from './store/store'
import router from './router'




import App from './App.vue'
import './assets/main.css'

// leaflet css
import 'leaflet/dist/leaflet.css';




window.axios = axios;
window.axios.defaults.headers.common['X-Requested-With'] = 'XMLHttpRequest';
axios.defaults.headers.common["X-CSRFToken"] = "{{ csrf_token() }}";
let r =document.head.querySelector('meta[name="csrf-token"]')
window.axios.defaults.headers.common["X-CSRF-TOKEN"]=r.content,




library.add(fas)
createApp(App)
.use(store)
.use(router)
.component('fa' , FontAwesomeIcon)
.mount('#app')


