/**
 * Created by adrian on 11/7/16.
 */
define(['jquery', 'underscore', 'backbone'], function ($, _, Backbone) {
    return Backbone.Model.extend({

        setAttributesAsArray: function(attributes) {
            /**
             * Methods accepts attributes to be set on the model as an array and sets them on the on model's attr hash.
             */
            "use strict";
            var _root = this;
             _.each(attributes, function(element){
                _root.set(element.name, element.value);
            });
        },

        middleware: { //This formulation allows us to override middleware methods in model implementations.
            handleGETRequest: function (options) {
                "use strict";
                $.get(model.url + '/' + _root.cid, function (data) {
                    console.log('GET Data received');
                    console.log(data);
                    _root.set(data.data);
                });
            },
            handlePOSTRequest: function(url, reqData) {
                "use strict";
                //Todo: Convert request data to json api format
                console.log(url);
                $.ajax({
                        url: url,
                        type: 'POST',
                        data: reqData,
                        success: function (result) {
                            // Do something with the result
                            console.log('Logging the result');
                            console.log(result);
                        },
                        error: function(err, status, message) {
                            console.log('is this being executed?')
                            console.error(err.responseText);
                        }
                    });
            },
            handlePATCHRequest: function(options) {
                "use strict";
                $.ajax({
                        url: model.url,
                        type: 'PATCH',
                        success: function (result) {
                            // Do something with the result
                        }
                    });
            },
            handlePUTRequest: function (options) {
                $.ajax({
                        url: model.url,
                        type: 'PUT',
                        success: function (result) {
                            // Do something with the result
                        }
                    });

            },

            handleDELETERequest: function(options) {
                "use strict";
                $.ajax({
                        url: model.url,
                        type: 'DELETE',
                        success: function (result) {
                            // Do something with the result
                        }
                    });
            }
        },

        sync: function (method, model, options) {
            var reqData = JSON.stringify(options.attrs || model.toJSON(options));
            var url = 'http://' + window.location.host + model.url();
            //var url = 'http://localhost:5000' + model.url();
            switch (method) {
                case 'read':
                    model.middleware.handleGETRequest(url, reqData);
                    break;
                case 'create':
                    console.log('Create method executed in sync');
                    model.middleware.handlePOSTRequest(url, reqData);
                    break;
                case 'update':
                    console.log('Update method executed in sync');
                    model.middleware.handlePATCHRequest(url, reqData);
                    break;
                case 'patch':
                    model.middleware.handlePATCHRequest(url, reqData);
                    break;
                case 'delete':
                    model.middleware.handleDELETERequest(url, reqData);
                default:
                    console.log('Incorrect method passed');
            }
        }
    })
});