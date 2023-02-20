<script>
  
  
  import SideBarComponent from './SideBarComponent.vue';
  import MainGraphComponent from './mainGraphComponent/MainGraphComponent.vue';
  import SearchEnginComponent from './SearchEnginComponent.vue';
  import { mapGetters , mapMutations, mapActions } from 'vuex';


  export default{
    name:'Dashboard',
    components: {
      SearchEnginComponent,
      MainGraphComponent,
      SideBarComponent,
    },
    data(){
      return{
        button_value:'',
        path :'http://127.0.0.1:5000/',
      }
    },
    methods: {
      ...mapActions(['getAllInfoAction']),
      ...mapMutations(['changeSearchEnginVisibility_toTrue']),

      // changeSearchEnginVisibility_toTrue
      SearchEnginMethod($event){
        
        this.changeSearchEnginVisibility_toTrue({visibility : true})
      }
    },

    created() {
      

    },

    computed: {
      ...mapGetters(['getSearchEnginVisibility']),

      currentRouteName() {
          return this.$route.name;
      }
    },
  
  }

</script>






<!-- -------------------------- -->

<template>
  
    <section class='dashboard_container'>

      <div class="sidbar_container">
        <SideBarComponent></SideBarComponent>
      </div>

      <div class="description_container">
        <div class="header_div">
          <div class="location_div">
            <div> Pages <span class='color_white'> / {{currentRouteName}}</span></div>
            <div class="color_white_bolder">{{currentRouteName}}</div>
          </div>
          <div class="search_div">
            <input class="search_input" type="search" name="search_input" placeholder="Point of interest here..." @click="SearchEnginMethod">
            <span class="search_icon"><fa icon="search"/></span>
          </div>
        </div>
        <!-- --------------------- -->

        
          <router-view/>

     

        <!-- ------------------------------- -->
      </div>
      <div class="searchbar_component" v-if="getSearchEnginVisibility">
        <SearchEnginComponent>

        </SearchEnginComponent>

      </div>



    </section>

</template>

<!-- ---------------------------- -->

<style setup>
  .dashboard_container{
    position: relative;
    width: 100%;
    max-height:100%;
    display: flex;
    flex-direction: row;
    justify-content: space-around;
    align-items:flex-start;

  }
  .sidbar_container{
    width: 13%;
    height: 100%;
    position: sticky;
    top: 20px;
    
  }
  /* ************ */
  .description_container{
    display: flex;
    flex-direction: column;
    justify-content: space-around;
    align-items: center;
    width: 85%;
    height: 100%;
  }

  .header_div{
    width: 100%;
    height: 10%;
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
    padding: 5px;
  }
  .location_div{
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    font-size: 14px;
  }
  .color_white{
    color: #fff;
  }
  .color_white_bolder{
    color: #fff;
    font-weight: bolder;
    font-size: 16px;
  }
  .search_div{
    padding: 0;
    background-color: #fff;
    border-radius: 10px;
  }
  .search_input{
    padding: 15px;
    border-radius: 10px;
    border: none;

  }
  .search_input:focus{
    border: none;
    outline: none;
  }
  .search_icon{
    padding: 10px;
    background-color: #fff;
    border-radius: 10px;
    cursor: pointer;
  }

   /* ************ */
  .description_component{
    width: 100%;
    height: 120px;
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    align-items:center;
  }

   /* ************ */
  .main_graph_component{
    position: relative;
    width: 100%;
    height: 70%;
  }

  .searchbar_component{
    position: absolute;
    width: 80%;
    height: 90%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    margin: 10px;
    padding: 10px;
    z-index: 5;
  }


</style>