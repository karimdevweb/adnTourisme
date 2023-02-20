<script>
    import DivComponent from '../DivComponent.vue';
    import { mapGetters , mapMutations, mapActions } from 'vuex';

    export default {
        name:'MlComponent',
        components:{
            DivComponent,
        },

        data() {
            return {
                text_area:'',
                ml_path:'http://127.0.0.1:5000/mlpredictionpath',
                no_description : false,
                loader:false,
                description:false,
                i : 0,
                text : '', 
                speed : 50, 

                
            }
        },

        methods: {

            ...mapActions(['getMLPredictionAction']),
          

           async submit_ml(){
                this.loader = true
                if(this.text_area.length > 0){
                    let ml_dict = {path : this.ml_path, description: this.text_area}
                    await this.getMLPredictionAction(ml_dict)
                    if(this.getMLPrediction !== undefined)
                    {
                        this.no_description = false
                        this.description = true
                    }
                    
                }else{
                    this.description = false
                    this.no_description = true
                }
                this.loader =false
                

            },
        },


        computed: {
            ...mapGetters(['getMLPrediction']),
            
            



        },  

        mounted() {
           
        },
        
    }
</script>


<!-- --------------------------- -->
<template>



    <div class="description_component">
        <DivComponent icon_props='chart-line' bg="bg_blue"  text="420 000" title="Nombre de POI" subTitle="description différente"></DivComponent>
        <DivComponent icon_props="map-location-dot" bg='bg_red' text="une seule, la description" title="Nombre de colonne" subTitle="NLP, Drop Stopwords et Spacy"></DivComponent>
        <DivComponent icon_props="chart-pie" bg='bg_green' text="11 categories" title="Nombre de Categorie" subTitle="assignation par critères"></DivComponent>
        <DivComponent icon_props="magnifying-glass-chart" bg='bg_orange' text="modèle de classification" title="Type de modèle" subTitle="LogisticRegression"></DivComponent> 
    </div>
     <!--------------- ML like ----------------------->
     <div class="main_graph_component"> 
        <div class="ml_main_div" >
            <div class="header_ml_div">
                <div class="salutation_div">
                    <p>Bonjour, Bienvenidos, Sayonara, Guten Morgen ! . . .  </p>
                    <div class="ia_img">
                        
                    </div>
                </div>
                
                <div class="img_div_chatgpt">
                    <div class="chatgpt_speech" id="'chatgpt_speech'">
                        <p>bonjour, je me présente,<br> <span class="gpt_name">chatte,  the bot</span>...hihihi ! <br> et vous ? </p>
                    </div>
                    <img class="chatgpt_img" src="../../assets/gpt.gif" alt="gpt_gif" srcset="">
                </div>
            </div>

            <div class="text_ml_div">

                <div class="text_area_container">
                    
                    <p> vous voulez connaitre votre categorie ,  s'il vous plaît entrer votre description: </p>
                    <textarea class="textarea_gpt" name="poi_description_ml" id="poi_description_ml" placeholder="here you can write your description" v-model="text_area"></textarea>
                    <div class="submit_button_div">
                            <span class="submit_button" @click="submit_ml()">submit</span>
                    </div>
                    
                </div>

                <div class="gpt_response">
                    <span class="loader" v-if="this.loader"></span>
                    <div >
                        <p class="no_description_p" v-if='this.no_description'>please, enter  a description!</p>
                        <transition name="slide-fade" >
                            <p   v-if="(this.description) && getMLPrediction?.data?.category" > d'après votre description, nous pouvons categoriser votre local dans la catégorie : 
                                    <span class="description"> {{getMLPrediction.data.category}} </span> with <span class="description"> {{this.getMLPrediction.data.quantity}}</span>
                                    others with same local throught the country.
                            </p>
                        </transition>                     
                    </div>
                </div>
            </div>
        </div>
     </div>
     
</template>



<!-- --------------------------- -->


<style setup>

    .ml_main_div{
        width: 100%;
        height: 100%;
        padding: 15px;
        margin: 0;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        border-radius: 10px;
        background-color: #f6f6f6;
    }
    .header_ml_div{
        width: 80%;
        height: 200px;
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        align-items:flex-start;
        padding: 15px;
        margin: 20px;
    }
    .salutation_div{
        font-size: 16px;
        text-align: left;
    }
    .ia_img{
        width: 150px;
        height: 150px;
    }
    .img_div_chatgpt{
        position: relative;
        width: 200px;
        height: 200px;
        border-radius: 10px;
    }
    .chatgpt_speech{
        position: absolute;
        top: -20px;
        left: -160px;
        padding: 10px;
        border-radius: 10px;
        background-color: #fff;
        line-height: 24px;
    }
    .chatgpt_speech:after{
        position: absolute;
        right: 0px;
        bottom: -1px;
        content: '';
        display: block;
        width: 0;
        height: 0;
        border-style: solid;
        border-width: 0 0 20px 20px;
        border-color: transparent transparent #0a0909 transparent;

    }
    .gpt_name{
        background-color: aqua;
        padding: 5px;
        border-radius: 4px;
    }
    .chatgpt_img{
        width: 100%;
        height: 100%;
    }



    .text_ml_div{
        width: 100%;
        display: flex;
        flex-direction: row;
        justify-content: space-around;
        align-items: center;
        margin: 10px;
    }
    .text_area_container{
        width: 50%;
        height: 100%;
        
    }
    .textarea_gpt{
        width: 650px;
        height: 250px;
        margin: 20px 20px 0px;
        border-radius: 10px;
        padding: 10px;
        box-shadow: 1px 1px 1px 1px inset #f6f6f6;
        font-weight: bolder;
        font-size: 18px;
        line-height: 24px;
    }
    .textarea_gpt:focus{
        border: none;
        outline: none;
    }
    .submit_button_div{
        width:90%;
        padding: 0 25px;
        text-align: right;
        display: flex;
        justify-content: end;
    }
    .submit_button{
        background-color: aqua;
        border: none;
        border-radius: 10%;
        padding: 10px 15px;
        cursor: pointer;
    }
    .gpt_response{
        width: 40%;
        text-align: left;
        line-height: 40px;
    }


    .no_description_p{
        background-color: #f5f5dc;
        text-align: center;
        width: 250px;
        padding: 10px;
        border-radius: 10px;
    }

    .description{
        background-color: aqua;
        text-align: center;
        width: fit-content;
        padding: 10px;
        margin: 5px;
        border-radius: 10px;
        font-size: 18px;
    }


    .slide-fade-enter-active {
        transition: all 0.3s ease-out;
    }

    .slide-fade-leave-active {
        transition: all 0.8s cubic-bezier(1, 0.5, 0.8, 1);
    }

    .slide-fade-enter-from,
    .slide-fade-leave-to {
        transform: translateX(20px);
        opacity: 0;
    }

   

</style>