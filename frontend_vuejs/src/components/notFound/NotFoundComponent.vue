<script>

    import DivComponent from '../DivComponent.vue';

export default {
    name:'NotFoundComponent',
    components: {
     
      DivComponent,
      
    },
    
    }
</script>




<!-- ------------------------- -->
<template>
    <div class="description_component">
        <DivComponent icon_props='chart-line' bg="bg_blue"  text="1 202" title="Structures adhérentes" subTitle="+ 7% en 2021"></DivComponent>
        <DivComponent icon_props="map-location-dot" bg='bg_red' text="13 500 (84% de droit privé)" title="Masse salariale" subTitle="77% femmes - 23% hommes"></DivComponent>
        <DivComponent icon_props="chart-pie" bg='bg_green' text="7 commissions" title="Nombre de Commissions" subTitle="grantissant la qualité et le suivie budgétaire"></DivComponent>
        <DivComponent icon_props="magnifying-glass-chart" bg='bg_orange' text="+ 25 associatifs et publique" title="Nombre de Partenaires" subTitle="promouvoir le tourisme national et régional"></DivComponent> 
    </div>
    <div class="not_found_div_container">
        <h2>The page you  are looking for does not exist</h2>
        <p><img class="img" src="../../assets/undraw_not_found.png" alt="undraw_not_found" ></p>
    </div>
</template>



<!-- ------------------------- -->
<style setup>
    .not_found_div_container{
        width: 500px;
        height: 500px;
        padding: 20px;
        margin: 20px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
    }
</style>