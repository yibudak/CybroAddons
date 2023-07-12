odoo.define('pos_receipt_extend.PaymentScreen', function (require) {
    'use strict';
    var rpc = require('web.rpc')
    const PaymentScreen = require('point_of_sale.PaymentScreen');
    const Registries = require('point_of_sale.Registries');
    const { onMounted } = owl;

    const PosPaymentReceiptExtend = PaymentScreen => class extends PaymentScreen {
        setup() {
        super.setup();
        }
         async validateOrder(isForceValidate) {
            var receipt_number = this.env.pos.selectedOrder.name
            var orders = this.env.pos.selectedOrder
            var datas = this.env.pos.session_orders
            const receipt_order = await super.validateOrder(...arguments);
            const codeWriter = new window.ZXing.BrowserQRCodeSvgWriter();
            const data = this.env.pos.session_orders;
            var length = data.length-1
            var order = data[length]
            var mobile = order.customer_mobile;
            var phone = order.customer_phone;
            var email = order.customer_email;
            var vat = order.customer_vat;
            var address = order.customer_address;
            var name = order.customer_name;
            var number = order.invoice_number;
            var qr_code = order.qr_code;
            if (!address) {
                              this.env.pos.selectedOrder.partner.street = null;
            }
            if (!name) {
                              this.env.pos.selectedOrder.partner.name = null;
            }
            if (!mobile) {
                              this.env.pos.selectedOrder.partner.mobile = null;
            }
            if (!phone) {
                              this.env.pos.selectedOrder.partner.phone = null;
            }
            if (!email) {
                              this.env.pos.selectedOrder.partner.email = null;
            }
            if (!vat) {
                              this.env.pos.selectedOrder.partner.vat = null;
            }
            if (!number) {
                              this.env.pos.selectedOrder.name = null;
            }
            var self= this;
         rpc.query({
                model: 'pos.order',
                method: 'get_invoice',
                args: [receipt_number]
                }).then(function(result){
                const address = `${result.base_url}/my/invoices/${result.invoice_id}?`
                let qr_code_svg = new XMLSerializer().serializeToString(codeWriter.write(address, 150, 150));
                if (qr_code) {
                   self.env.pos.qr_image = "data:image/svg+xml;base64,"+ window.btoa(qr_code_svg);
                }
                if (number) {
                   self.env.pos.invoice  = result.invoice_name
                }
                });
                return receipt_order
         }
         }



       Registries.Component.extend(PaymentScreen, PosPaymentReceiptExtend);

    return PaymentScreen;
       });

