<script>
    import DivComponent from '../DivComponent.vue';
    import SliderComponent from '../mainGraphComponent/mainGraphSubComponent/SliderComponent.vue';
    import { mapGetters , mapMutations, mapActions } from 'vuex';


  export default{
    name:'HomeComponent',
    components: {
      SliderComponent,
      DivComponent,
      
    },
    data(){
      return{
        path : 'http://127.0.0.1:5000/',
      }
    },
    methods: {
      ...mapActions(['getAllInfoAction' ,'getRegionAndDepatementAction','getCategoryDistributionAction']),


      // get pois from the store action
      async getInfoAction(){
                await this.getAllInfoAction(this.path)
                
            },
    },

    async created() {
      // get all POIs for the map
            
            this.getInfoAction()

    },

    computed: {
      
    },
  
  }

</script>





<!-- -------------------------- -->

<template>

        <div class="description_component">
            <DivComponent icon_props='chart-line' bg="bg_blue"  text="1 202" title="Structures adhérentes" subTitle="+ 7% en 2021"></DivComponent>
            <DivComponent icon_props="map-location-dot" bg='bg_red' text="13 500 (84% de droit privé)" title="Masse salariale" subTitle="77% femmes - 23% hommes"></DivComponent>
            <DivComponent icon_props="chart-pie" bg='bg_green' text="7 commissions" title="Nombre de Commissions" subTitle="grantissant la qualité et le suivie budgétaire"></DivComponent>
            <DivComponent icon_props="magnifying-glass-chart" bg='bg_orange' text="+ 25 associatifs et publique" title="Nombre de Partenaires" subTitle="promouvoir le tourisme national et régional"></DivComponent> 
        </div>
        <div class="main_graph_component">
            <div class="main_graph_div">
                <div class="main_first_graph">
                  <div class="diagrame_div">
                      <img class="diagrame_adn" src="../../assets/diagrame_project_4.png" alt="diagrame_project_4">
                    </div>
                    
                </div>
                <div class="main_second_graph">  
                    <SliderComponent>
                        
                    </SliderComponent>
                </div>
            </div>
            <div class="detail_div">
                <div class="first_detail_table">
                  <div class="project_description_div">
                        <h1>Developpement d'un dashboard pour le groupement ADN Tourisme</h1>
                        <div class="objectif_description_div">
                            <h3>les Objectifs sont:</h3>
                            <ol>
                              <li>Application de recherche d’établissement pour les propriétaires</li>
                              <li>Amélioration de la qualité de la base de données</li>
                              <li>A partir de 450 000 points d’intérêt local accessibles par Open data au format JSON :
                                <ul>
                                  <li>Proposer un prototype d’interface web qui permet une recherche d’un établissement dans la base actualisée, et retourne l’ensemble des informations associées à cet établissement.</li>
                                  <li>Le but est que les propriétaires d’établissement puissent accéder facilement à ce qui est stocké.</li>
                                  <li>Proposer un tableau de bord géographique permettant d’accéder aux informations touristiques (par ville, département ou région)</li>                                  
                                  <li>Créer un modèle de classification (Machine Learning) pour prédire la catégorie en fonction de la description de l’établissement.</li>
                                </ul>
                              </li>
                            </ol>
                        </div>
                    </div>
                </div>
                <div class="second_detail_table">
                  
                    <div class="tech_used_div">
                      <h3 class="tech_title">Technologies utilisées : </h3>
                        <div class="tech_one_div"><img class='tech_img' src="../../assets/axios.png" alt="axios" srcset=""></div>
                        <div class="tech_one_div"><img class='tech_img' src="../../assets/mysql.png" alt="mysql" srcset=""></div>
                        <div class="tech_one_div"><img class='tech_img' src="../../assets/nlp.jpg" alt="axios" srcset=""></div>
                        <div class="tech_one_div"><img class='tech_img' src="../../assets/pandas.png" alt="pandas" srcset=""></div>
                        <div class="tech_one_div"><img class='tech_img' src="../../assets/vuejs.png" alt="vuejs" srcset=""></div>
                        <div class="tech_one_div"><img class='tech_img' src="../../assets/python.png" alt="python" srcset=""></div>
                        <div class="tech_one_div"><img class='tech_img' src="../../assets/sklearn.png" alt="sklearn" srcset=""></div>
                    </div>
                </div>
              
            </div>
        </div>

</template>

<!-- ---------------------------- -->
<style setup>
  .project_description_div{
    width: 100%;
    height: 100%;
    padding: 20px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    
    background-color: #faebd7;
    border-radius: 10px;

  }
  .objectif_description_div{
    font-size: 14px;
    padding: 0;
    margin: 0;
    text-align: left;
    
  }
  .diagrame_div{
    width: 100%;
    height: 100%;
    display: flex;
    flex-direction: column;
    justify-content: center;
    align-items: center;
    background-color: #fff;
    border-radius: 10px;
  }
  .diagrame_adn{
    width: 65%;
    height: 95%;
  
  }
  .tech_used_div{
    width: 100%;
    height: 100%;
    padding: 15px;
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    align-items: center;
    background-color: #fff;
  }
  .tech_one_div{
    width: 85px;
    height: 85px;
    margin: 10px 15px;
    border-radius: 10px;
  }
  .tech_title{
    width: 100%;
    padding: 10px;
    font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
  }
  .tech_img{
    width: 100%;
    height: 100%;
    border-radius: 10px;
  }
</style>
