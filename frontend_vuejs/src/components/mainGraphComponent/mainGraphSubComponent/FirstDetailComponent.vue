<script>
    import { stringifyExpression } from '@vue/compiler-core';
    import { mapGetters , mapMutations, mapActions } from 'vuex';


    export default{
        name:'FirstDetailComponent',
        components : {
           
        },
        data() { 
            return {
                // info_variable_detail:{},
                // region_variable : {},
                // departement_variable : {},
                // show_depat:false,

                // graph variables
                graph_path: 'http://127.0.0.1:5000/graph_path',
                statistic_path: 'http://127.0.0.1:5000/statistic_func',
                graph_query : String,
                locality_name:String,
                
            }
        },



        methods: {
            ...mapActions(['getCategoryDistributionAction', 'getStatisticDistributionAction']),

            // assign(){
                
            //     this.info_variable_detail =  this.getInfo
            //     this.region_variable  = this.getDepartementAndRegion
            //     this.departement_variable = this.getCommuneInDepartement
                
            // },

            get_event($event, value){
                
                if (value.region !=undefined){
                    this.graph_query = 'region',
                    this.locality_name = value.region
                }
                else if(value.departement !=undefined)
                {
                    this.graph_query = 'departement',
                    this.locality_name = value.departement

                }
                else{
                    this.graph_query = 'commune',
                    this.locality_name = value.commune
                    
                }

                
                
                this.getGraphDistributionMethod()
                this.getStatiscticDistributionMethod()
                
            },

            async getGraphDistributionMethod()
                {    
                    let graph_dict  = { path : this.graph_path,
                                        graph_query : this.graph_query, 
                                        locality_name : this.locality_name
                                       }
                    await this.getCategoryDistributionAction(graph_dict)

                },

            async getStatiscticDistributionMethod()
            {    
                let statistic_dict  = { path : this.statistic_path,
                                    graph_query : this.graph_query, 
                                    locality_name : this.locality_name
                                    }
                await this.getStatisticDistributionAction(statistic_dict)

            }
            
        },


        computed: {
           ...mapGetters(['getDepartementAndRegion' ,'getCommuneInDepartement' ,'getDepartementAndRegionVariable']),
            
            
        },

        created() {
            
        },
        mounted() {
            
            
            
        },
       updated(){
         
            
        }
    }

</script>

<!-- ------------------------------- -->

<template>
    <div class="region_table_div">
        
        <div class="header_table">
            <div class="category_number_header">
                <fa class="locality_icon" icon="map-location-dot"/>
                <!-- <p>n-POI / circonscription </p> -->
            </div>
            <p class="category_header"> Categories</p>
        </div> 
      


        <!-- ---------------loader waiting data for map-------------------- -->
        <div class="no_data_for_map" v-if="!getDepartementAndRegionVariable">
            <p>it's can take more time, if browser storage is not accessing  :</p>
            <p><span class="loader"></span></p>
        </div>
        <!-- ---------------loader waiting data for map-------------------- -->



        <div class="region_container"  v-if="getDepartementAndRegionVariable">
            <div class="region_table" v-for="(region, reg_idx) in getDepartementAndRegion.data" :key="reg_idx" 
                                    @click="get_event($event, region )" >

                <div class="one_region_div" v-show=" region.region" >
                    {{ region.region }}
                </div>
                <div class="one_region_div" v-show="region.departement" >
                    {{ region.departement }}
                </div> 

                <!-- -------------------- -->
             
                
                <!-- -------------------- -->
                <div class="category_div" v-for="(cat, cat_reg_idx) in region.u_cat" :key="cat_reg_idx" v-if="region.u_cat">
                    {{  cat }}
                </div>
                <div class="category_div" v-for="(cat_dep, cat_dep_idx) in region.u_dep_cat" :key="cat_dep_idx" v-else>
                    {{  cat_dep }}
                </div>
            </div>
       </div> 

       <!-- ----------------------------- -->
       <div class="region_container"  v-if="(!getDepartementAndRegionVariable) & (getCommuneInDepartement != undefined)">
            <div class="region_table" v-for="(commune, commune_indx) in getCommuneInDepartement.data" :key="commune_indx" 
                                    @click="get_event($event, commune )" >
                <div class="one_region_div" v-show=" commune.commune" >
                    {{ commune.commune }}
                </div>
                
               
                



         
                 
                
                <!-- -------------------- -->
                <div class="category_div" v-for="(cat_commune, cat_commune_idx) in commune.u_commune_cat" :key="cat_commune_idx" >
                    {{  cat_commune }}
                </div>
                
            </div>
       </div> 
       



            
    </div>
</template>





<!-- ------------------------------- -->
<style setup>

    .region_table_div{
        height: 100%;
        display: flex;
        flex-direction: column;
        justify-content: center;
        color: black;
        
        font-family:'Courier New', Courier, monospace
    }
    .region_container{
        height: 100%;
        min-width: 100%;
        overflow: auto;
        display: flex;
        flex-direction: column;
        justify-content: start;
        align-items: flex-start;
        background-color: #f6f9fc;
    }
    .region_table{
        width: 100%;
        text-align: left;
        font-size: 14px;
        display: flex;
        flex-direction: row;
        justify-content: start;
        align-items: center;
        background-color: #f6f9fc;
        padding: 10px;
        cursor: pointer;
        
    }
    .header_table{
        height: 15%;
        width: 100%;
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items: flex-start;
        background-color: rgb(85, 167, 167);
        border-radius: 10px;
        padding: 10px;
        font-weight: bolder;
        color: #fff;
    }

    .category_number_header{
        width: 20%;
        display: flex;
        flex-direction: row;
        justify-content: space-around;
        justify-items: center;
    }
    .locality_icon{
        font-size: 24px;
        color: #ffffffc0;
    }
    .category_header{
        width: 50%;
    }

    .one_region_div{
        width: 300px;
        height: 100%;
        cursor: pointer;
        text-align: left;
        margin: 0 10px 0 0;
        background-color: #f6f9fc;
    }
    .number_cat{
        font-weight: bolder;
        padding: 0 5px;
      
    }
    .category_div{
        padding: 5px 7px;
        text-align: left;
        margin: 0 10px;
        background-color: aqua;
        border-radius: 10px;
        
    }



</style>