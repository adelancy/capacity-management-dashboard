/**
 * Created by adrian on 11/6/16.
 */
require.config({
    //Should rename this file to app.js

    baseUrl: 'static/js',

    paths: {
        'jquery': 'https://ajax.googleapis.com/ajax/libs/jquery/1.7.2/jquery.min',
        'bootstrap': 'https://netdna.bootstrapcdn.com/bootstrap/3.0.0/js/bootstrap.min',
        'underscore': 'https://cdnjs.cloudflare.com/ajax/libs/underscore.js/1.5.2/underscore-min',
        'backbone': 'https://cdnjs.cloudflare.com/ajax/libs/backbone.js/1.1.0/backbone-min',
        'team-req': 'custom/team-req',
        'async': 'libs/requirejs-plugins/async',
    },

    // The shim config allows us to configure dependencies for
    // scripts that do not call define() to register a module
    shim: {
        'underscore': {
            exports: '_'
        },
        'backbone': {
            //These script dependencies should be loaded before loading
            //backbone.js
            deps: ['jquery', 'underscore'],
            //Once loaded, use the global 'Backbone' as the
            //module value.
            exports: 'Backbone'
        },
        'bootstrap': {
            deps: ['jquery'],
            exports: 'Bootstrap'
        }
    }

});
