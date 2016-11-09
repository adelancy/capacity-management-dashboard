/**
 * Created by adrian on 11/7/16.
 */
define(['jquery', 'underscore', 'backbone'], function ($, _, Backbone) {
    return Backbone.Model.extend({

        sync: function (method, model, options) {
            var _root = this;
            if (method === 'read') {
                $.get('data/teams/' + _root.cid, function (data) {
                    _root.set(data.data);
                });
            }
        }
    });
});