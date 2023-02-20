<template>

    <carousel class="caroussel_component" :items-to-show="1" :itemsToScroll="1" :autoplay=2500 :mouseDrag=True wrapAround transition=2500>
        <slide class ='slider_component' v-for="(image, index) in images" :key= image.id>
               <div class="img_link_div">
                    <img class ='img' :src="getImage(image.url)" alt="image actualité"/>   
                    <div class="info_div_link">
                        <p>vous voulez en savoir plus...</p>
                        <span> trouvez toutes les infos sur la page officiel <a class="img_link" :href="image.url_img" target="_blank"> <button class="link_button"> <fa class='link_icon' icon="arrow-up-right-from-square"/></button></a></span>
                        
                    </div>  
               </div>
        </slide>
    
        
    </carousel>
  </template>
  
  <script>
  // If you are using PurgeCSS, make sure to whitelist the carousel CSS classes
  import 'vue3-carousel/dist/carousel.css'
  import { Carousel, Slide, Pagination, Navigation } from 'vue3-carousel'
  
  export default {
    name: 'App',
    components: {
      Carousel,
      Slide,
    //   Pagination,
    //   Navigation,
    },
    data() {
        return {
          
          images: [{id: 1,url:'./src/assets/noel-info.jpg', url_img:'https://www.adn-tourisme.fr/vacance-noel-2022/'}, 
                    {id: 2,url:'./src/assets/challenge-territoires.jpg', url_img:'https://www.adn-tourisme.fr/challenge-territoire-insoupconnes-edition-2/'}, 
                    {id: 3,url:'./src/assets/tourisme-sportif.jpeg',url_img:'https://www.adn-tourisme.fr/tourisme-sportif/'},
                    {id: 4,url:'./src/assets/projet-club-ingenierie.png',url_img:'https://www.adn-tourisme.fr/projets-ingenierie/'},
                    {id: 5,url:'./src/assets/dataTourisme-schema.png',url_img:'https://www.adn-tourisme.fr/datatourisme-pilotage/'}]
        }
    },
    methods: {
      getImage(imagePath) {
          return String(imagePath);
        }
    },  
}
  </script>



<!-- ---------------- -->

<style setup>
  .caroussel_component{
    height: 100%;
    width: 100%;
  }
  .slider_component{
    padding: 0;
    margin: 0;
    height: 350px !important;
    border-radius: 10px;
  }

  .img{
        width: 100%;
        height: 100%;
        padding: 0;
        margin: 0;
        border-radius: 10px;
    }
    .img_link_div{
      width: 100%;
      height: 100%;
      padding: 0;
      margin: 0;
      border-radius: 10px;
      position: relative;
      overflow: hidden;
    }
    .info_div_link{
      text-align: left;
      font-weight: lighter;
      color: #344767;
      font-family:'Times New Roman', Times, serif;
      font-size: 26px;
      line-height: 30px;
      position: absolute;
      bottom: 10px;
      padding: 10px;
      margin: 10px;
      border-radius: 10px;
      background-color: rgba(238, 235, 235, 0.575);
    }
    .info_div_link>p{
      padding: 0;
      margin: 0;
    }
    .info_div_link>span{
      font-size: 14px;
      padding: 0 15px;
    }
    .img_link{
      font-size: 16px;
      color: #fff;
      
      
    }
    .link_button{
      background-color: #fff;
      width: 35px;
      height: 35px;
      border: none;
      margin: 0 10px;
      border-radius: 100%;
      cursor: pointer;
    }
    .link_icon{
      font-size: 14px;
      color: #344767;
    }
</style>