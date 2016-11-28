/**
 * Created by adrian.p.delancy on 11/22/2016.
 */
define(['custom/models/root-model'], function (Model) {
    /*global define */
   return Model.extend({
       urlRoot: '/data/vm-reqs',
       type: 'vm-req'
    });
});