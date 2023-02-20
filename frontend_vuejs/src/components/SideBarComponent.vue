<script>
    import { mapGetters , mapMutations, mapActions } from 'vuex';

    export default{
        name: 'SideBarComponent',
        data() {

            return {

            }
        },



        methods: {
            ...mapMutations([]), 

            
        },

        computed: {
            ...mapGetters([''])
        },


    }


</script>


<!-- --------------------- -->

<template>
    <div class="side_bar_div">
        <div class="firma_name">
            <div class="logo_div">
                <a class='img_logo' href="https://www.adn-tourisme.fr/" target="_blank" rel="noopener noreferrer"><img class='img_logo' src="../assets/logo_adn.png" alt="logo_adn"></a>
            </div>
            <span>ADN Tourisme</span>
        </div>
        <div class="menu_div">
            <router-link to="/" class="menu_selection">
                <span class="icon_menu_selection"><fa class="color_blue" icon="tv"/></span>
                <span>Acceuil</span>
            </router-link>

            <router-link to="/dashboard" class="menu_selection">
                <span class="icon_menu_selection"> <fa class="color_red"  icon="table-list"/></span>
                <span>Dashboard</span>
            </router-link>

            <router-link to="/machine_learning" class="menu_selection">
                <span class="icon_menu_selection"><fa class="color_green"  icon="robot" /></span>
                 <span>M Learning</span>
            </router-link>
            
        </div>
        <div class="need_help_container">
            <a href="https://www.adn-tourisme.fr/contact-page/" target="_blank" class="need_help_img">
                <img class="img" src="../assets/need_help.png" alt="need_help" >
            </a>
            <h3>Need help ?</h3>
            <span class="contact_help_span">please, contact us</span>
        </div>
    </div>
</template>

<!-- --------------------- -->


<style setup>
    .side_bar_div{
        height: 100%;
        width: 100%;
        background-color: #ffffff;
        padding: 10px;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        align-items: center;
        border-radius: 10px;
        
    }
    .firma_name{
        padding: 5px;
        font-size: 20px;
        display: flex;
        flex-wrap: wrap;
        justify-content: space-around;
        align-items: center;
    }
    .firma_name::after{
        margin: 20px;
        content: " ";
        display: block;
        width: 100%;
        height: 1px;
        background-color: rgb(142, 170, 194);
    }
    .logo_div{
        width: 50px;
        height: 50px;
        border-radius: 10px;
        background-color: antiquewhite;
    }
    .img_logo{
        width: 100%;
        height: 100%;
    }
    .menu_div{
        width: 100%;
        height: 80%;
        display: flex;
        margin:  0 0 100px 0;
        flex-direction: column;
        justify-content: space-around;
        align-items: center;
    }
    .menu_selection{
        cursor: pointer;
        text-align: left;
        font-size: 16px;
        font-weight: lighter;
        width: 90%;
        padding: 20px;
        margin: 20px 0;
        border-radius: 10px;
        background-color: #f6f9fc;
        text-decoration: none;
    }
    .router-link-exact-active{
        background-color: #faebd7;
    }

    .need_help_container{
        width: 100%;
        margin: 100px 0 10px;
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        padding: 10px;
    }
    .need_help_img{
        height: 80%;
        width: 60%;
        
    }
    .contact_help_span{
        font-size: 12px;
    }





    .icon_menu_selection{
        margin: 10px;
    }
    .color_blue{
        color:#5e72e4;
    }
    .color_red{
        color:#f54d47;
    }
    .color_green{
        color:#2dce9c;
    }
    .color_orange{
        color:#fb7d40;
    }
    .bg_blue{
        background-color:#5e72e4;
    }
    .bg_red{
        background-color:rgb(226 10 82);
    }
    .bg_green{
        background-color:#2dce9c;
    }
    .bg_orange{
        background-color:#fb7d40;
    }
    .bg_yellow{
        background-color:#a19456;
    }
    .bg_pink{
        background-color:#b185d6;
    }
    .bg_white_bleu{
        background-color:#1ebec4;
    }
    .bg_brown{
        background-color:#756332;
    }
    .bg_black{
        background-color:#33322c;
    }
    .bg_rose{
        background-color:#86125a;
    }
</style>