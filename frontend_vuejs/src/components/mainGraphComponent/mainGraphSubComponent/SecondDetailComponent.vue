<script>
    
    import { mapGetters , mapMutations, mapActions } from 'vuex';

    import { Bar } from 'vue-chartjs'
    import { Chart as ChartJS, Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale } from 'chart.js'
    
    
    ChartJS.register(Title, Tooltip, Legend, BarElement, CategoryScale, LinearScale)


   

    export default{
        name:'SecondDetailComponent',
        components:{
                    Bar,
            },

        data() {
            return {
              
                graph_path:'http://127.0.0.1:5000/graph_path',
                graph_query : '',
                locality_name:'',
                


                chartOptions: {
                        responsive: true,
                        plugins: {
                                title: {
                                    display: true,
                                    text: 'Distribution par categorie sur la region',
                                    padding: {
                                        top: 10,
                                        bottom: 30
                                    }
                                }
                            }
                    },

                    
                    


            
            }
        },



        methods: {
            ...mapActions(['getCategoryDistributionAction']),
        

            async getGraphDistributionMethod()
                    {    
                        let graph_dict  = { path : this.graph_path,
                                            graph_query : this.graph_query, 
                                            locality_name : this.locality_name
                                        }
                        await this.getCategoryDistributionAction(graph_dict)
                        
                       

                    },





            },


        computed: {
                ...mapGetters(['getGraphDistributionVariable']),

                customChart() {
                        let category_tab = [];
                        let category_count = [];

                        if (this.getGraphDistributionVariable.data !== undefined) {
                           
                            this.getGraphDistributionVariable.data.forEach((element) => {
                                category_tab.push(element.category);
                                category_count.push(element.category_number);
                            });
                        } else {
                            console.log('you have an error, the graph donnt get any data');
                        }

                    return {
                        labels: category_tab,
                        datasets: [
                            {
                                label: 'categories',
                                backgroundColor: '#e20a52',
                                data: category_count,
                            },
                        ],
                    };
                },
            },
            
            

            


            
       

            
                
                    
 
        async mounted() {
            

            await this.getGraphDistributionMethod()
            

           

        },
        

       
    }

</script>

<!-- ------------------------------- -->

<template>
    <div class="graph_img_div">
    

       <Bar class="bar_chart"
        id="my-chart-id"
        :options="chartOptions"
        :data="customChart" 
        />
        
        
            
            <!-- <img class="not_found_img" src="../../assets/undraw_not_found.png" alt="undraw_not_found.png"> -->
    </div>
</template>





<!-- ------------------------------- -->
<style setup>
    .graph_img_div{
        width: 100%;
        height: 100%;
    }
    .not_found_img{
        width: 100%;
        height: 100%;
    }

    .bar_chart{
        width: 100% ;
        height: 100% ;
    }


</style>