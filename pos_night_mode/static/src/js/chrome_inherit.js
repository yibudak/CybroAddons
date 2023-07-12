    odoo.define('pos_night_mode.chrome', function(require){
        'use strict';

        const Chrome = require('point_of_sale.Chrome');
        const Registries = require('point_of_sale.Registries');
        var rpc = require('web.rpc')

        const PosNightMod = (Chrome) =>
            class extends Chrome {
                async start() {
                    var self = this;
                    await super.start();
                    rpc.query({
                        model: 'res.users',
                        method: 'get_active'
                    }).then(function(res){
                        if(res){
                            $("#fa-icon").removeClass("fa fa-moon-o").removeClass("moon-color").addClass("fa fa-sun-o").addClass("sun-color");
                            self._OnNightTrue()
                        }
                        else{
                            $("#fa-icon").removeClass("sun-color").removeClass("fa fa-sun-o").addClass("fa fa-moon-o").addClass("moon-color");
                        }
                    })
                }
                OnClickMoon(){
                    var self = this;
                    if($('#button_toggle')[0].attributes[4].nodeValue == "true"){
                         $("#fa-icon").removeClass("fa fa-moon-o").removeClass("moon-color").addClass("fa fa-sun-o").addClass("sun-color");
                        rpc.query({
                            model:'res.users',
                            method: 'set_active'
                        }).then(function(){
                            self._OnNightTrue()
                        })
                    }
                    else{
                        $("#fa-icon").removeClass("sun-color").removeClass("fa fa-sun-o").addClass("fa fa-moon-o").addClass("moon-color");
                        rpc.query({
                            model: 'res.users',
                            method: 'set_deactivate'
                        }).then(function(){
                            $('style').remove()
                        })
                    }
                }
                _OnNightTrue(){
                    var pos_element = document.querySelector('.pos')
                    var pos_product_list_modifier = document.createElement('style')
                    pos_product_list_modifier.innerHTML = '.pos{color:white;}'+'.pos .product { background-color:#3c3f41 !important;border:'+
                    'thin solid white;border-radius: 5px;}.pos .product .product-img img {background-image:'+
                    'linear-gradient(to bottom,white,#3c3f41) !important;}'+
                    '.pos .product-list-container{background-color:#3c3f41 !important;}'+
                    '.pos .product .price-tag {color:#F45976 !important;}'+
                    '.pos .order{background-color:#3c3f41}'+
                    '.pos .rightpane{background-color:#3c3f41}'+
                    '.pos .rightpane-header{background-color:#3c3f41;}'+
                    '.pos .breadcrumb-button{color:white}'+
                    '.pos .category-simple-button{background-color:#3c3f41 !important;}'+
                    '.pos .sb-product .pos-search-bar{background-color:#3c3f41 !important;}'+
                    '.pos .rightpane-header .pos-search-bar input, .pos .partnerlist-screen'+
                    ' .pos-search-bar input{color:#adb7c1}'+
                    '.pos .order .orderline.selected{background:rgb(112, 115, 117) !important}'+
                    '.pos .order .orderline .info-list{color:#B3B7BF !important}'+
                    '.pos .order .orderline .info-list em{color:#B3B7BF !important}'+
                    '.pos .control-button{background-color:#3c3f41 !important;}'+
                    '.pos .mode-button.selected-mode{background-color:#707375 !important;}'+
                    '.pos .numpad button{background-color:#3c3f41;color:white;}'+
                    '.pos .numpad button:hover{background-color:#f45976 !important;}'+
                    '.pos .button.validation:hover{background-color:#f45976 !important;}'+
                    '.pos .actionpad .button{background-color:#3c3f41;color:white;}'+
                    '.pos .actionpad .button:hover{background-color:#f45976 !important;}'+
                    '.pos .control-button:hover{background-color:#f45976 !important;}'+
                    '.pos .modal-dialog .popup{background-color:#1e1f20 !important;}'+
                    '.pos .popup .button{background:#8F3536;color: white !important};'+
                    '.ticket-screen .controls button {background-color:white;color:black;}'+
                    '.ticket-screen .pos-search-bar .filter{color:black}'+
                    '.ticket-screen .pos-search-bar .filter .options{border-radius:5px}'+
                    '.pos .order-container{background-color:#3c3f41}'+
                    '.pos .partner-window{color:black;}'+
                    '.pos .partnerlist-screen .partner-list thead > tr{background-color:#3c3f41;color:white}'+
                    '.pos .partnerlist-screen tr.partner-line:hover{background-color:#f45976}'+
                    '.pos .partner-list tr.partner-line.highlight{background-color:#017e84}'+
                    '.screen .screen-content{background-color:#e0e2e6}'+
                    '.pos .partnerlist-screen .pos-search-bar i{color:black;}'+
                    '.pos .partnerlist-screen .pos-search-bar input{color:#2a2b2d;}'+
                    '.screen .top-content .button.highlight{background-color:#017e84 !important;border-color:#3c3f41 !important;}'+
                    '.screen .top-content{background-color:#3c3f41}'+
                    '.pos .close-pos-popup header{background-color:rgb(56, 57, 58)}'+
                    '.pos .popup .title{background-color:rgb(56, 57, 58)}'+
                    '.pos .close-pos-popup .closing-notes{background-color:#c1c3c6}'+
                    '.pos .opening-cash-control .opening-cash-notes{background-color:#c1c3c6}'+
                    '.payment-screen .main-content{background:#3c3f41}'+
                    '.paymentmethods .button{background:#3c3f41}'+
                    '.pos .paymentline{background:#3c3f41}'+
                    '.pos .paymentline.selected{background:#707375}'+
                    '.pos .screen .button.next:not(.highlight){background:#e6e3e2;color:#017e84;}'+
                    '.receipt-screen .default-view{background:#3c3f41}'+
                    '.receipt-screen .default-view .actions .send-email input{background:#666668;color:white;}'+
                    '.receipt-screen .default-view .actions .buttons .button{background:#666668}'+
                    '.receipt-screen .default-view .actions .send-email button.send{background:#017e84;color:black}'+
                    '.pos .pos-receipt-container > div{color:black}'+
                    '.pos .popup.popup-error .button{background:#8F3536}'+
                    '.pos .orders .order-row:nth-child(n){background:#3c3f41}'+
                    '.pos .orders .order-row.highlight{background:#017e84}'+
                    '.pos .orders .order-row:hover{background:#f45976;}'+
                    '.payment-screen .payment-buttons .button{background:#3c3f41}'+
                    '.payment-screen .payment-buttons .button:hover{background:#f45976;}'
                    ;
                    pos_element.parentNode.insertBefore(pos_product_list_modifier, pos_element);
                }
            }
        Registries.Component.extend(Chrome, PosNightMod);

        return Chrome;
    });