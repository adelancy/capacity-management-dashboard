/**
 * Created by adrian on 11/7/16.
 * Javascript Backbone Model Class to represent a Team Resource object
 */
define(['custom/models/root-model'], function (Model) {
    /*global define */
   return Model.extend({
       urlRoot: '/data/teams',
       type: 'team'
    });
});