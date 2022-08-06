odoo.define("sh_portal_dashboard.sale_charts", function (require) {
    "use strict";

    var core = require("web.core");
    var _t = core._t;
    var ajax = require("web.ajax");

    /**
     * Fetch the sale chart data by ajax call.
     *
     * @returns {rendered chart}
     */
    function set_charts() {
        ajax.jsonRpc("/sh_portal_dashboard/get_sale_chart", "call", {
            sh_filter_chart_type: $.cookie("sh_filter_chart_type"),
        }).then(function (data) {
            //chart data start here

            var chart_data = {
                // A labels array that can contain any sort of values
                labels: data.x_axis_labels_list,
                // Our series array that contains series objects or in this case series data arrays
                series: [data.y_axis_series_list],
            };

            var options = {
                plugins: [Chartist.plugins.tooltip()],
                seriesBarDistance: 10,
            };

            var responsiveOptions = [
                [
                    "screen and (max-width: 640px)",
                    {
                        seriesBarDistance: 5,
                        axisX: {
                            //    		      labelInterpolationFnc: function (value) {
                            //    		        return value[0];
                            //    		      }
                        },
                    },
                ],
            ];

            // Create a new line chart object where as first parameter we pass in a selector
            // that is resolving to our chart container element. The Second parameter
            // is the actual data object.

            var heading_chart = '<div id="js_id_sale_bar_chart_div_heading" class="text-center">' + data.heading + "</div>";
            if (data.is_show_sale_chart && $("#js_id_sale_bar_chart_div").length) {
                $("#js_id_sale_bar_chart_div_heading").replaceWith(heading_chart);
                new Chartist.Bar("#js_id_sale_bar_chart_div", chart_data, options, responsiveOptions);
            }

            //chart data ends here
        });
    }

    /**
     * Fetch the invoice chart data by ajax call.
     *
     * @returns {rendered chart}
     */

    function set_invoice_charts() {
        ajax.jsonRpc("/sh_portal_dashboard/get_invoice_chart", "call", {
            sh_filter_chart_type: $.cookie("sh_filter_chart_type"),
        }).then(function (data) {
            //chart data start here

            var chart_data = {
                // A labels array that can contain any sort of values
                labels: data.x_axis_labels_list,
                // Our series array that contains series objects or in this case series data arrays
                series: [data.y_axis_series_list],
            };

            var options = {
                plugins: [Chartist.plugins.tooltip()],
                seriesBarDistance: 10,
            };

            var responsiveOptions = [
                [
                    "screen and (max-width: 640px)",
                    {
                        seriesBarDistance: 5,
                        axisX: {
                            //    		      labelInterpolationFnc: function (value) {
                            //    		        return value[0];
                            //    		      }
                        },
                    },
                ],
            ];

            // Create a new line chart object where as first parameter we pass in a selector
            // that is resolving to our chart container element. The Second parameter
            // is the actual data object.
            var heading_chart = '<div id="js_id_invoice_bar_chart_div_heading" class="text-center">' + data.heading + "</div>";
            if (data.is_show_invoice_chart && $("#js_id_invoice_bar_chart_div").length) {
                $("#js_id_invoice_bar_chart_div_heading").replaceWith(heading_chart);
                new Chartist.Bar("#js_id_invoice_bar_chart_div", chart_data, options, responsiveOptions);
            }

            //chart data ends here
        });
    }

    /**
     * Fetch the purchase chart data by ajax call.
     *
     * @returns {rendered chart}
     */

    function set_purchase_charts() {
        ajax.jsonRpc("/sh_portal_dashboard/get_purchase_chart", "call", {
            sh_filter_chart_type: $.cookie("sh_filter_chart_type"),
        }).then(function (data) {
            //chart data start here

            var chart_data = {
                // A labels array that can contain any sort of values
                labels: data.x_axis_labels_list,
                // Our series array that contains series objects or in this case series data arrays
                series: [data.y_axis_series_list],
            };

            var options = {
                plugins: [Chartist.plugins.tooltip()],
                seriesBarDistance: 10,
            };

            var responsiveOptions = [
                [
                    "screen and (max-width: 640px)",
                    {
                        seriesBarDistance: 5,
                        axisX: {
                            //    		      labelInterpolationFnc: function (value) {
                            //    		        return value[0];
                            //    		      }
                        },
                    },
                ],
            ];

            // Create a new line chart object where as first parameter we pass in a selector
            // that is resolving to our chart container element. The Second parameter
            // is the actual data object.

            var heading_chart = '<div id="js_id_purchase_bar_chart_div_heading" class="text-center">' + data.heading + "</div>";
            if (data.is_show_purchase_chart && $("#js_id_purchase_bar_chart_div").length) {
                $("#js_id_purchase_bar_chart_div_heading").replaceWith(heading_chart);
                new Chartist.Bar("#js_id_purchase_bar_chart_div", chart_data, options, responsiveOptions);
            }

            //chart data ends here
        });
    }

    /**
     * Fetch the bills chart data by ajax call.
     *
     * @returns {rendered chart}
     */

    function set_bill_charts() {
        ajax.jsonRpc("/sh_portal_dashboard/set_bill_charts", "call", {
            sh_filter_chart_type: $.cookie("sh_filter_chart_type"),
        }).then(function (data) {
            //chart data start here

            var chart_data = {
                // A labels array that can contain any sort of values
                labels: data.x_axis_labels_list,
                // Our series array that contains series objects or in this case series data arrays
                series: [data.y_axis_series_list],
            };

            var options = {
                plugins: [Chartist.plugins.tooltip()],
                seriesBarDistance: 10,
            };

            var responsiveOptions = [
                [
                    "screen and (max-width: 640px)",
                    {
                        seriesBarDistance: 5,
                        axisX: {
                            //    		      labelInterpolationFnc: function (value) {
                            //    		        return value[0];
                            //    		      }
                        },
                    },
                ],
            ];

            // Create a new line chart object where as first parameter we pass in a selector
            // that is resolving to our chart container element. The Second parameter
            // is the actual data object.
            var heading_chart = '<div id="js_id_bill_bar_chart_div_heading" class="text-center">' + data.heading + "</div>";
            if (data.is_show_bill_chart && $("#js_id_bill_bar_chart_div").length) {
                $("#js_id_bill_bar_chart_div_heading").replaceWith(heading_chart);
                new Chartist.Bar("#js_id_bill_bar_chart_div", chart_data, options, responsiveOptions);
            }

            //chart data ends here
        });
    }

    /**
     * Fetch the product wise sale data by ajax call.
     *
     * @returns {rendered chart}
     */

    function get_product_wise_sale_data() {
        ajax.jsonRpc("/sh_portal_dashboard/get_product_wise_sale_data", "call", {
            sh_filter_chart_type: $.cookie("sh_filter_chart_type"),
        }).then(function (data) {
            var table = '<table id="js_id_tbl_product_wise_sale" class="table rounded bg-white"> <thead> <tr> <th>Image</th> <th>Products</th> <th>Amount</th> <th>Qty Sold</th> </tr> </thead><tbody>';

            _.each(data.products, function (rec) {
                table = table + "<tr> <td>" + rec.product_img + "</td> <td>" + rec.product + "</td> <td>" + rec.amount + "</td> <td> " + rec.qty + " </td> </tr>";
            });

            table = table + "</tbody></table>";

            if (!data.products.length) {
                table = table + '<div class="js_cls_sh_portal_dashbaord_table_no_data_msg alert alert-info" role="alert">No records found!</div>';
            }

            var heading_chart = '<div id="js_id_product_wise_sale_chart_div_heading" class="text-center">' + data.heading + "</div>";
            var heading_table = '<div id="js_id_tbl_product_wise_sale_heading" class="text-center">' + data.heading + "</div>";

            if (data.is_show_product_wise_sale_data) {
                $("#js_id_tbl_product_wise_sale").replaceWith(table);
                $("#js_id_product_wise_sale_chart_div_heading").replaceWith(heading_chart);
                $("#js_id_tbl_product_wise_sale_heading").replaceWith(heading_table);
            } else {
                $("#js_id_tbl_product_wise_sale").hide();
            }

            //chart data start here
            var chart_data = {
                // A labels array that can contain any sort of values
                labels: data.x_axis_labels_list,
                // Our series array that contains series objects or in this case series data arrays
                series: [data.y_axis_series_list_amount],
            };

            var options = {
                plugins: [Chartist.plugins.tooltip()],
                seriesBarDistance: 50,
                reverseData: true,
                horizontalBars: true,
                axisY: {
                    offset: 120,
                },
            };

            var responsiveOptions = [
                [
                    "screen and (max-width: 640px)",
                    {
                        seriesBarDistance: 5,
                        axisX: {
                            //    		      labelInterpolationFnc: function (value) {
                            //    		        return value[0];
                            //    		      }
                        },
                    },
                ],
            ];

            // Create a new line chart object where as first parameter we pass in a selector
            // that is resolving to our chart container element. The Second parameter
            // is the actual data object.
            if (data.is_show_product_wise_sale_data && $("#js_id_product_wise_sale_chart_div").length) {
                new Chartist.Bar("#js_id_product_wise_sale_chart_div", chart_data, options, responsiveOptions);
            }

            //chart data ends here
        });
    }

    /**
     * Fetch the product wise purchase data by ajax call.
     *
     * @returns {rendered chart}
     */

    function get_product_wise_purchase_data() {
        ajax.jsonRpc("/sh_portal_dashboard/get_product_wise_purchase_data", "call", {
            sh_filter_chart_type: $.cookie("sh_filter_chart_type"),
        }).then(function (data) {
            var table = '<table id="js_id_tbl_product_wise_purchase" class="table rounded bg-white"> <thead> <tr> <th>Image</th> <th>Products</th> <th>Amount</th> <th>Qty Bought</th> </tr> </thead><tbody>';

            _.each(data.products, function (rec) {
                table = table + "<tr> <td>" + rec.product_img + "</td> <td>" + rec.product + "</td> <td>" + rec.amount + "</td> <td> " + rec.qty + " </td> </tr>";
            });

            table = table + "</tbody></table>";

            if (!data.products.length) {
                table = table + '<div class="js_cls_sh_portal_dashbaord_table_no_data_msg alert alert-info" role="alert">No records found!</div>';
            }

            var heading_chart = '<div id="js_id_product_wise_purchase_chart_div_heading" class="text-center">' + data.heading + "</div>";
            var heading_table = '<div id="js_id_tbl_product_wise_purchase_heading" class="text-center">' + data.heading + "</div>";
            if (data.is_show_product_wise_purchase_data) {
                $("#js_id_tbl_product_wise_purchase").replaceWith(table);
                $("#js_id_product_wise_purchase_chart_div_heading").replaceWith(heading_chart);
                $("#js_id_tbl_product_wise_purchase_heading").replaceWith(heading_table);
            } else {
                $("#js_id_tbl_product_wise_purchase").hide();
            }

            //chart data start here
            var chart_data = {
                // A labels array that can contain any sort of values
                labels: data.x_axis_labels_list,
                // Our series array that contains series objects or in this case series data arrays
                series: [data.y_axis_series_list_amount],
            };

            var options = {
                plugins: [Chartist.plugins.tooltip()],
                seriesBarDistance: 10,
                reverseData: true,
                horizontalBars: true,
                axisY: {
                    offset: 120,
                },
            };

            var responsiveOptions = [
                [
                    "screen and (max-width: 640px)",
                    {
                        seriesBarDistance: 5,
                        axisX: {
                            //    		      labelInterpolationFnc: function (value) {
                            //    		        return value[0];
                            //    		      }
                        },
                    },
                ],
            ];

            // Create a new line chart object where as first parameter we pass in a selector
            // that is resolving to our chart container element. The Second parameter
            // is the actual data object.
            if (data.is_show_product_wise_purchase_data && $("#js_id_product_wise_purchase_chart_div").length) {
                new Chartist.Bar("#js_id_product_wise_purchase_chart_div", chart_data, options, responsiveOptions);
            }

            //chart data ends here
        });
    }

    /**
     * Fetch the Category wise product sale data by ajax call.
     *
     * @returns {rendered chart}
     */

    /**
     * Fetch the Category wise product purchase data by ajax call.
     *
     * @returns {rendered chart}
     */

    /**
     * Fetch the project task data by ajax call.
     *
     * @returns {rendered chart}
     */

    function get_project_task_data() {
        ajax.jsonRpc("/sh_portal_dashboard/get_project_task_data", "call", {
            sh_filter_chart_type: $.cookie("sh_filter_chart_type"),
        }).then(function (data) {
            var table = '<table id="js_id_tbl_project_task" class="table rounded bg-white"> <thead> <tr> <th>Project</th> <th>Task</th> <th>Deadline</th> </tr> </thead><tbody>';

            _.each(data.tasks, function (rec) {
                table = table + "<tr> <td>" + rec.project + "</td> <td>" + rec.task + "</td> <td> " + rec.deadline + " </td> </tr>";
            });

            table = table + "</tbody></table>";

            if (!data.tasks.length) {
                table = table + '<div class="js_cls_sh_portal_dashbaord_table_no_data_msg alert alert-info" role="alert">No records found!</div>';
            }

            if (data.is_show_project_chart_data) {
                $("#js_id_tbl_project_task").replaceWith(table);
            } else {
                $("#js_id_tbl_project_task").hide();
            }
        });
    }

    /**
     * Fetch the quotations data by ajax call.
     *
     * @returns {rendered chart}
     */

    function get_last_quote() {
        ajax.jsonRpc("/sh_portal_dashboard/get_last_quote", "call", {
            sh_filter_chart_type: $.cookie("sh_filter_chart_type"),
        }).then(function (data) {
            var table = '<table id="js_id_tbl_last_quote" class="table table-sm"> <thead> <tr> <th>Order Number</th> <th>Order Date</th> </tr> </thead><tbody>';

            _.each(data.quotes, function (rec) {
                table = table + "<tr> <td>" + rec.name + "</td> <td>" + rec.date_order + "</td> </tr>";
            });

            table = table + "</tbody></table>";

            if (!data.quotes.length) {
                table = table + '<div class="js_cls_sh_portal_dashbaord_table_no_data_msg alert alert-info" role="alert">No records found!</div>';
            }

            if (data.is_show_last_quote_table) {
                $("#js_id_tbl_last_quote").replaceWith(table);
            } else {
                $("#js_id_tbl_last_quote").hide();
            }
        });
    }

    /**
     * Fetch the sale orders data by ajax call.
     *
     * @returns {rendered chart}
     */

    function get_last_sale_order() {
        ajax.jsonRpc("/sh_portal_dashboard/get_last_sale_order", "call", {
            sh_filter_chart_type: $.cookie("sh_filter_chart_type"),
        }).then(function (data) {
            var table = '<table id="js_id_tbl_last_sale_order" class="table table-sm"> <thead> <tr> <th>Order Number</th> <th>Order Date</th> <th>Status</th> </tr> </thead><tbody>';

            _.each(data.orders, function (rec) {
                table = table + "<tr> <td>" + rec.name + "</td> <td>" + rec.date_order + "</td> <td>" + rec.status + "</td> </tr>";
            });

            table = table + "</tbody></table>";

            if (!data.orders.length) {
                table = table + '<div class="js_cls_sh_portal_dashbaord_table_no_data_msg alert alert-info" role="alert">No records found!</div>';
            }

            if (data.is_show_last_sale_order_table) {
                $("#js_id_tbl_last_sale_order").replaceWith(table);
            } else {
                $("#js_id_tbl_last_sale_order").hide();
            }
        });
    }

    /**
     * Fetch the recent RFQ data by ajax call.
     *
     * @returns {rendered chart}
     */

    function get_last_rfq() {
        ajax.jsonRpc("/sh_portal_dashboard/get_last_rfq", "call", {
            sh_filter_chart_type: $.cookie("sh_filter_chart_type"),
        }).then(function (data) {
            var table = '<table id="js_id_tbl_last_rfq" class="table table-sm"> <thead> <tr> <th>Reference</th> <th>Order Date</th> </tr> </thead><tbody>';

            _.each(data.rfqs, function (rec) {
                table = table + "<tr> <td>" + rec.name + "</td> <td>" + rec.date_order + "</td> </tr>";
            });

            table = table + "</tbody></table>";

            if (!data.rfqs.length) {
                table = table + '<div class="js_cls_sh_portal_dashbaord_table_no_data_msg alert alert-info" role="alert">No records found!</div>';
            }

            if (data.is_show_last_rfq_table) {
                $("#js_id_tbl_last_rfq").replaceWith(table);
            } else {
                $("#js_id_tbl_last_rfq").hide();
            }
        });
    }

    /**
     * Fetch the recent Purchase Order data by ajax call.
     *
     * @returns {rendered chart}
     */

    function get_last_purchase() {
        ajax.jsonRpc("/sh_portal_dashboard/get_last_purchase_order", "call", {
            sh_filter_chart_type: $.cookie("sh_filter_chart_type"),
        }).then(function (data) {
            var table = '<table id="js_id_tbl_last_purchase_order" class="table table-sm"> <thead> <tr> <th>Reference</th> <th>Order Date</th> <th>Status</th>  </tr> </thead><tbody>';

            _.each(data.orders, function (rec) {
                table = table + "<tr> <td>" + rec.name + "</td> <td>" + rec.date_order + "</td> <td>" + rec.status + "</td> </tr>";
            });

            table = table + "</tbody></table>";

            if (!data.orders.length) {
                table = table + '<div class="js_cls_sh_portal_dashbaord_table_no_data_msg alert alert-info" role="alert">No records found!</div>';
            }

            if (data.is_show_last_purchase_order_table) {
                $("#js_id_tbl_last_purchase_order").replaceWith(table);
            } else {
                $("#js_id_tbl_last_purchase_order").hide();
            }
        });
    }

    /**
     * Fetch the recent invoice table data by ajax call.
     *
     * @returns {rendered chart}
     */

    function get_last_invoice() {
        ajax.jsonRpc("/sh_portal_dashboard/get_last_invoice", "call", {
            sh_filter_chart_type: $.cookie("sh_filter_chart_type"),
        }).then(function (data) {
            var table = '<table id="js_id_tbl_last_invoice" class="table table-sm"> <thead> <tr> <th>Invoice #</th> <th>Invoice Date</th> <th>Due Date</th> <th>Status</th> <th class="text-right">Amount Due</th>  </tr> </thead><tbody>';

            _.each(data.invoices, function (rec) {
                table = table + "<tr> <td>" + rec.name + "</td> <td>" + rec.invoice_date + "</td> <td>" + rec.invoice_date_due + "</td><td>" + rec.status + '</td> <td class="text-right">' + rec.amount_residual + "</td> </tr>";
            });

            table = table + "</tbody></table>";

            if (!data.invoices.length) {
                table = table + '<div class="js_cls_sh_portal_dashbaord_table_no_data_msg alert alert-info" role="alert">No records found!</div>';
            }

            if (data.is_show_last_invoice_table) {
                $("#js_id_tbl_last_invoice").replaceWith(table);
            } else {
                $("#js_id_tbl_last_invoice").hide();
            }
        });
    }

    /**
     * Fetch the recent bill table data by ajax call.
     *
     * @returns {rendered chart}
     */

    function get_last_bill() {
        ajax.jsonRpc("/sh_portal_dashboard/get_last_bill", "call", {
            sh_filter_chart_type: $.cookie("sh_filter_chart_type"),
        }).then(function (data) {
            var table = '<table id="js_id_tbl_last_bill" class="table table-sm"> <thead> <tr> <th>Invoice #</th> <th>Invoice Date</th> <th>Due Date</th> <th>Status</th> <th class="text-right">Amount Due</th>  </tr> </thead><tbody>';

            _.each(data.invoices, function (rec) {
                table = table + "<tr> <td>" + rec.name + "</td> <td>" + rec.invoice_date + "</td> <td>" + rec.invoice_date_due + "</td><td>" + rec.status + '</td> <td class="text-right">' + rec.amount_residual + "</td> </tr>";
            });

            table = table + "</tbody></table>";

            if (!data.invoices.length) {
                table = table + '<div class="js_cls_sh_portal_dashbaord_table_no_data_msg alert alert-info" role="alert">No records found!</div>';
            }

            if (data.is_show_last_bill_table) {
                $("#js_id_tbl_last_bill").replaceWith(table);
            } else {
                $("#js_id_tbl_last_bill").hide();
            }
        });
    }

    /**
     * call all chart render functions when document is ready.
     * load default user setting from browser cookie.
     *
     * @returns {rendered chart}
     */

    $(document).ready(function () {
        $(".js_cls_sh_portal_dashbaord_table_no_data_msg").remove();
        //load all charts
        set_charts();
        set_invoice_charts();
        set_purchase_charts();
        set_bill_charts();

        //get product data
        get_product_wise_sale_data();
        get_product_wise_purchase_data();

        //category wise product
        get_project_task_data();

        //last quote
        get_last_quote();
        get_last_sale_order();

        //last RFQS
        get_last_rfq();
        get_last_purchase();

        //invoice Table
        get_last_invoice();
        get_last_bill();

        //if cookie has sh_filter_chart_type value than set the selection value
        if ($.cookie("sh_filter_chart_type")) {
            $("#js_id_select_filter_chart").val($.cookie("sh_filter_chart_type"));
        }

        //when selection filter chart type changed than update cookie value and load all charts again async
        $("#js_id_select_filter_chart").change(function () {
            //set new filter chart type value in cookiechart_data
            $.cookie("sh_filter_chart_type", $("#js_id_select_filter_chart").val());

            $(".js_cls_sh_portal_dashbaord_table_no_data_msg").remove();
            //load all charts again to render new chart type.
            set_charts();
            set_invoice_charts();
            set_purchase_charts();
            set_bill_charts();

            //get product data
            get_product_wise_sale_data();
            get_product_wise_purchase_data();
            get_project_task_data();

            //last quote
            get_last_quote();
            get_last_sale_order();

            //last RFQS
            get_last_rfq();
            get_last_purchase();

            //invoice Table
            get_last_invoice();
            get_last_bill();
        });
    });
});
