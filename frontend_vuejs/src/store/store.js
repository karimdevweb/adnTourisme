import { createStore } from 'vuex' 

//  you have to import  the store simply in main.js and add it into our  app, .use(store)


export default createStore(
    {
        state:{
            name: 'koko',
            buttonValue:'',
            poi : {
                name: 'hhh',
                description: 'hhhhyy',
                adresse: 'hhh',
                lat:'hhh',
                long:'hhh',
                category:'hhh',
                last_updated:'hhh',

            },
            info: null,
            list_proposal: {},

            // get the status of the search engine
            search_engine_visibility : false,
            // get the status if to show the region table or no
            departementAndRegionVisibility: true, 

            // region_category variable
            getRegionVariable: {},

            // departement variable
            departementAndRegionVariable : {},
            // commune  variable
            communeVariable : {},

            //  graph distribution variable
            graph_distribution_info : {},

            //  captor distribution variable
            captor_distribution_info : {},
         
            // MLPrediction
            MLPrediction:{},



        },
    
        getters:{
            // get  all  POIs at beginning
            getInfo(state) {
                
                 return state.info
            },
            getPoi(state){
                return state.poi
            },
            // get only searched info, through searchnEngine
            getListProp(state){
                
                return state.list_proposal
            },

            // search engine visibility
            getSearchEnginVisibility(state){
                return state.search_engine_visibility
            },

            //  get region with categories
            getRegionVariable(state){
                return state.getRegionVariable
            },

            // getllDepartementVariable
            getDepartementAndRegion(state){
                return state.departementAndRegionVariable
            },

            // getllDepartementVariable
            getCommuneInDepartement(state){
                return state.communeVariable
            },

            // get getDepartementAndRegionVariable 
            getDepartementAndRegionVariable(state){
                return state.departementAndRegionVisibility
            },

            //  get graph distribution info variable
            getGraphDistributionVariable(state){
                return state.graph_distribution_info
            },

            //  get captors distribution info variable
            getCaptorDistributionVariable(state){
                return state.captor_distribution_info
            },

            
            // get state.MLPrediction
            getMLPrediction(state){
                return state.MLPrediction
            }
            
        },
    
        mutations:{
            changeInfo(state, payload){
                
                state.info ={data : payload.data}
                
            },

            changePoi(state, payload){
                state.poi.name = payload.name
                state.poi.description =  payload.description
                state.poi.adresse = payload.adresse 
                state.poi.lat = payload.lat
                state.poi.long =payload.long
                state.poi.category = payload.category
                state.poi.last_updated  = payload.last_updated

            },
            changeListProp(state, payload){
                state.list_proposal = { data : payload.data}
                
            },

            // display or close the searchEngin
            changeSearchEnginVisibility_toTrue(state, payload){
                state.search_engine_visibility = payload.visibility
            },

            // display or close the searchEngin
            changeSearchEnginVisibility_toFalse(state, payload){
                state.search_engine_visibility = payload.visibility
            },

            // assing into my region variable data from py
            changeregionDict(state, payload)
            {
                state.getRegionVariable = { data : payload.data}
              
            },

            // assing data into my departement variable
            changeDepartementDict(state, payload){
                state.departementAndRegionVariable = {data :  payload.data}
            },


            
            // assing data into my departement variable
            changeCommuneDict(state, payload){
                state.communeVariable = {data :  payload.data}
            },

            // display or not region / departemtnt table
            changeDepartementAndRegionVisibility(state, payload){
                state.departementAndRegionVisibility = payload.visibility
            },

            // changeGraphDistribution display categories on graph 
            changeGraphDistribution(state, payload){
                state.graph_distribution_info = {data : payload.data}
                
            },

            // changeCaptorDistribution display statistics for captors 
            changeCaptorDistribution(state, payload){
                state.captor_distribution_info = {data : payload.data}
                
            },
            
            

            // changeMLPrediction
            changeMLPrediction(state, payload)
            {
                state.MLPrediction = {data : payload.data}
            }
           

        },
    
        actions:{
            // get all pois info lat / long ...
            getAllInfoAction(context, path){
                
                axios.get(path, {headers:{'content-type':'application/json'}})
                     .then((res)=>{
                        
                        context.commit('changeInfo', {data : res.data})
                        // Save the data to local storage
                        localStorage.setItem('info', JSON.stringify(res.data))
                     })
                     .catch((err)=>{
                        console.log(err)
                     })
            },


           
            // getproposition into search engin ...
            getOnePoiAction(context,res_dict  ){
            
                axios.post(res_dict.path+'/resto', { categories: res_dict.categories, regions: res_dict.regions, query: res_dict.query} , {headers:{'content-type':'application/json'}})
                      .then((res)=>{

                        //  to continues here with adressee ...
                        let categories  = res.data.categories
                        let query  = res.data.query
                        
                        context.commit('changeListProp', {data: res.data})
                      })
                      .catch((err) => {
                        console.log(err.response +' here the err')
                      })
            },


            
            // get all commune in one departement 
            getCommuneAction(context, get_commune_dic){
               
                axios.post(get_commune_dic.path,{asked_departement: get_commune_dic.asked_departement}, {headers:{'content-type':'application/json'}})
                     .then((res)=>{
                        
                        context.commit('changeCommuneDict', {data : res.data})
                        
                     })
                     .catch((err)=>{
                        console.log(err)
                     })
            },


            // get all departement in one region 
            getRegionAndDepatementAction(context, get_departement_dic){
               
                axios.post(get_departement_dic.path,{asked_region: get_departement_dic.asked_region}, {headers:{'content-type':'application/json'}})
                     .then((res)=>{
                     
                        context.commit('changeDepartementDict', {data : res.data})
                        
                     })
                     .catch((err)=>{
                        console.log(err)
                     })
            },


            // get category distribution data for graph
            getCategoryDistributionAction(context, get_graph_needed_info){
               
                axios.post(get_graph_needed_info.path,{graph_query: get_graph_needed_info.graph_query, locality_name : get_graph_needed_info.locality_name}, {headers:{'content-type':'application/json'}})
                     .then((res)=>{
                       
                        context.commit('changeGraphDistribution', {data : res.data})
                        
                     })
                     .catch((err)=>{
                        console.log(err)
                     })
            },



             // get statistics distribution data for captors
             getStatisticDistributionAction(context, get_stats_needed_info){
                
                axios.post(get_stats_needed_info.path,{graph_query: get_stats_needed_info.graph_query, locality_name : get_stats_needed_info.locality_name}, {headers:{'content-type':'application/json'}})
                     .then((res)=>{
                       
                        context.commit('changeCaptorDistribution', {data : res.data})
                        
                     })
                     .catch((err)=>{
                        console.log(err)
                     })
            },





            // get ml prediction 
            getMLPredictionAction(context, get_description_poi){
                
                axios.post(get_description_poi.path,{ml_description: get_description_poi.description}, {headers:{'content-type':'application/json'}})
                .then((res)=>{
                   
                    context.commit('changeMLPrediction', {data : res.data})
                
                })
                .catch((err)=>{
                    console.log(err)
                })
            }
                
        }
    }
)