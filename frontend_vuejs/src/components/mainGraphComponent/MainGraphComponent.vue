<script >
    import DivComponent from '../DivComponent.vue'
    import SliderComponent from './mainGraphSubComponent/SliderComponent.vue'
    import FirstGraphComponent from './mainGraphSubComponent/FirstGraphComponent.vue';
    import FirstDetailComponent from './mainGraphSubComponent/FirstDetailComponent.vue';
    import SecondDetailComponent from './mainGraphSubComponent/SecondDetailComponent.vue';
    import SecondGraphComponent from './mainGraphSubComponent/SecondGraphComponent.vue';
    import { mapGetters , mapMutations, mapActions } from 'vuex';
   



    export default{
        name : 'MainGraphComponent',
        components : {
            SliderComponent,
            FirstGraphComponent,
            SecondGraphComponent,
            FirstDetailComponent,
            SecondDetailComponent,
            DivComponent,

           
        },
        data() {
            return {
                path : 'http://127.0.0.1:5000/',
                path_region : 'http://127.0.0.1:5000/region_departement_filter',
                asked_region:'',


                
            }
        },

        methods: {
            ...mapActions(['getAllInfoAction' ,'getRegionAndDepatementAction','getCategoryDistributionAction','getStatisticDistributionAction']),
            ...mapMutations(['']), 

            
            
            
            //  get all categories in a region for the table
            async getRegionCategories(){
                let get_departement_dic = {path : this.path_region, asked_region:  this.asked_region}
                
                await this.getRegionAndDepatementAction(get_departement_dic)
                
            },

           
        

            

           
            
        },
        computed: {
            


        },  

        async created(){
        
            // get all POIs for the map
            
            // this.getInfoAction()
            this.getRegionCategories()
           
           
            
        },
        

    }

    

</script>


<!-- ---------------------- -->
<template>



    <div class="description_component">
        <DivComponent icon_props='chart-line' bg="bg_blue"  text="420 000" title="Nombre de POI" subTitle="fichiers Josn avec structures différentes"></DivComponent>
        <DivComponent icon_props="map-location-dot" bg='bg_red' text="45 Jours" title="Jours sur le projet" subTitle="extraction, transformation et chargement"></DivComponent>
        <DivComponent icon_props="chart-pie" bg='bg_green' text="11 categories" title="Nombre de Categorie" subTitle="assignation par critères"></DivComponent>
        <DivComponent icon_props="magnifying-glass-chart" bg='bg_orange' text="13 + Guadeloupe / Réunion" title="Nombre de Region" subTitle="département/commune et s-commune"></DivComponent> 
        
    </div>
    <div class="main_graph_component"> 
        <div class="main_graph_div">
            <div class="main_first_graph">
                <FirstGraphComponent  >
                
                </FirstGraphComponent>
            </div>
            <div class="main_second_graph">  
                <SecondGraphComponent></SecondGraphComponent>
            </div>
        </div>
        <div class="detail_div">
            <div class="first_detail_table">
                <FirstDetailComponent></FirstDetailComponent>
            </div>
            <div class="second_detail_table">
                <SecondDetailComponent></SecondDetailComponent>
            </div>
            
        </div>

    </div>



    




   
    

    

</template>






<!-- ---------------------- -->

<style setup>

/* ***************************************** */
    
    
    .main_graph_div{
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: center;
        padding: 10px;
        height: 70%;
    }
    .main_first_graph{
        padding: 0px;
        border-radius: 10px;
        width: 60%;
        height: 350px;
        background-color: #faebd7;
        margin: 0 5px;
    }
    .main_second_graph{
        padding: 0px;
        border-radius: 10px;
        width: 40%;
        height: 350px;
        margin: 0 5px;
    }

    .detail_div{
        display: flex;
        flex-direction: row;
        justify-content: space-around;
        align-items: center;
        padding: 10px;
        
    }
    .first_detail_table{
        border-radius: 10px;
        width: 60%;
        height: 300px;
        margin: 0 5px;
    }
    .second_detail_table{
      
        border-radius: 10px;
        width: 40%;
        height: 300px;
        background-color: #faebd7;
        margin: 0 5px;
    }


</style>