/**
 * Created by adrian.p.delancy on 11/22/2016.
 */
define(['./root-model'], function (Model) {
   return Model.extend({
       urlRoot: '/data/bm-req',
       type: 'bm-req'
    });
});