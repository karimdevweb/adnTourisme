<script>
    import { mapGetters , mapMutations, mapActions } from 'vuex';

    export default {
        name:'SecondGraphComponent',
        data() {
            return {
                statistic_path: 'http://127.0.0.1:5000/statistic_func',
                graph_query : '',
                locality_name:'',
            }
        },

        methods: {
            ...mapActions(['getStatisticDistributionAction']),

            async getCaptorDistributionMethod()
                {    
                    let statistic_dict  = { path : this.statistic_path,
                                    graph_query : this.graph_query, 
                                    locality_name : this.locality_name
                                    }
                    await this.getStatisticDistributionAction(statistic_dict)
                    
                    

                },
            
        },

        computed: {
            ...mapGetters(['getCaptorDistributionVariable']),


        },

        mounted() {
            
           this.getCaptorDistributionMethod()


        },
        

    }
</script>


<!-- -------------------------------------- -->

<template>
    <div class="statistic_container_div">
        <div class="no_data_alternative" v-if="!getCaptorDistributionVariable.data">
            <img class="not_found_img" src="../../../assets/undraw_not_found.png" alt="undraw_not_found.png">
        </div>
        
        <div class="statistics_captor_div" v-else>
            <div class="main_territory_div">
                <h3 class="statistics_title">sur le territoire <em :class="{'no_reseigned_data':getCaptorDistributionVariable.data.main_territory == 'non renseignée'}">{{ getCaptorDistributionVariable.data.main_territory }}</em></h3>
                <div class="captor_div">
                    <h4 class="title_statistic">circonscriptions: </h4>
                    <span class="result_statistic">{{ getCaptorDistributionVariable.data.circonscription_number }}</span>
                </div>

                <div class="captor_div">
                    <h4 class="title_statistic"> POIs: </h4>
                    <span class="result_statistic">{{ getCaptorDistributionVariable.data.poi_number }}</span>
                </div>

                <div class="top_region_bg">
                    <h4 class="title_statistic">top région: </h4>
                    <span class="result_statistic">{{ getCaptorDistributionVariable.data.top_circon }}</span>
                </div>

                <div class="flop_region_bg">
                    <h4 class="title_statistic">flop région: </h4>
                    <span class="result_statistic">{{ getCaptorDistributionVariable.data.flop_circon }}</span>
                </div>
            </div>
            <div class="top_territory_div">
                <h3 class="statistics_title">sur la top cirsconscription <em :class="{'no_reseigned_data':(getCaptorDistributionVariable.data.top_circon == 'non renseignée')}">{{ getCaptorDistributionVariable.data.top_circon }}</em></h3>
                <div class="captor_div">
                    <h4 class="title_statistic">nbr de POI: </h4>
                    <span class="result_statistic">{{ getCaptorDistributionVariable.data.cat_num_in_circ }}</span>
                </div>

                <div class="top_region_bg">
                    <h4 class="title_statistic">top categorie: </h4>
                    <span class="result_statistic">{{ getCaptorDistributionVariable.data.top_category }}</span>
                </div>

                <div class="captor_div">
                    <h4 class="title_statistic">nbr top categorie: </h4>
                    <span class="result_statistic">{{ getCaptorDistributionVariable.data.num_for_top_cat }}</span>
                </div>
            </div>

            

           

            

            
        </div>
    </div>
</template>







<!-- -------------------------------------- -->

<style setup>
    .statistic_container_div{
        width: 100%;
        height: 100%;
        background-color: #faebd7;
    }
    .no_data_alternative{
        width: 100%;
        height: 100%;
    }
    .statistics_captor_div{
        width: 100%;
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: flex-start;
        align-items: center;
    }
    .main_territory_div, .top_territory_div{
        width: 100%;
        height: 40%;
        margin: 10px 5px;

        display: flex;
        flex-wrap: wrap;
        justify-content: space-around;
        align-items: center;
        font-family: 'Lucida Sans', 'Lucida Sans Regular', 'Lucida Grande', 'Lucida Sans Unicode', Geneva, Verdana, sans-serif;

    }
    .statistics_title{
        width: 100%;
        padding: 5px;
        font-weight: bolder;
    }
    


    .captor_div{
        padding: 10px;
        border-radius: 10px;
        text-align: center;
        background-color: #f6f9fce3;
        border: 2px solid #b8894d;

    }
    .top_region_bg{
        padding: 10px;
        border-radius: 10px;
        text-align: center;
        border: 2px solid #05ad0d;
        background-color: #77b67a5d;
    }
    .flop_region_bg{
        padding: 10px;
        border-radius: 10px;
        text-align: center;
        border: 2px solid #cc130d;
        background-color: #dda4a28f;
    }




</style>