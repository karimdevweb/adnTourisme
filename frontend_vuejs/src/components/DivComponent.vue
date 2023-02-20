<script setup>
  defineProps({
    icon_props: String,
    bg : String,
    text :String,
    title: String,
    subTitle: String
  })

</script>






<!-- -------------------------- -->

<template>
  <div class='div_component_container'>

    <div class='description_div_container'>
        <div class="description_div">
            <span>{{title}}</span>
            <span>{{text}}</span>
        </div>
        <div class='img_div color_white' :class=bg >
           <fa :icon=icon_props />
        
        </div>
    </div>

    <div class='footer_div'>
        <span>{{subTitle}} </span>
    </div>
  </div>
</template>

<!-- ---------------------------- -->

<style setup>
  



  .div_component_container{
    width: 360px;
    height: 80%;
    border-radius: 10px;
    padding: 10px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    background-color: #fff;
    
    
  }
  .description_div_container{
    display: flex;
    flex-direction: row;
    justify-content: space-between;
    align-items: center;
  }
  .description_div{
    font-size: 18px;
    display: flex;
    flex-direction: column;
    text-align: left;
  }
  .img_div{
    display: flex;
    justify-content: center;
    align-items: center;
    width: 50px;
    height: 50px;
    border-radius: 100%;
    background-color: antiquewhite;
    font-size: 22px;
  }

</style>