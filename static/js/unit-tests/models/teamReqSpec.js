/**
 * Created by adrian.p.delancy on 11/22/2016.
 */

define(function (require) {
    "use strict";

    describe('Create a VM Requirement Model and Save it to the Database', function () {
        var Model = require('../../custom/models/vm-req-model');

        it('Should load the correct class properly', function () {
            expect(Model).toBeDefined();
        });

        it('Should allow the creation of a new model object instance', function(){
            var model = new Model();
            expect(model).toBeDefined();
        });

        it('Should persist the data model to the database successfully', function(){
            var magicNumber = Math.round(Math.random() *10);
            var data = [
                {name: "crsf_token", value: "1480296505##f9cba005afe7b2e4ecc1d6ff8b4ec1d1e95ab274"},
                {name: "name", value: "Test VM Req " + magicNumber},
                {name: "team-id", value: "Test Team " + magicNumber},
                {name: "vm_type", value: "Production"},
                {name: "os_type", value: "Microsoft Windows Server 2013"},
                {name: "vcpus", value: "2"},
                {name: "ram", value: "4"}
            ]

            var vmReq = new Model();
            vmReq.setAttributesAsArray(data);

            expect(vmReq.get('crsf_token')).toBe('1480296505##f9cba005afe7b2e4ecc1d6ff8b4ec1d1e95ab274');
            expect(vmReq.type).toBe('vm-req');
            expect(vmReq.get('ram')).toBe("4");

            //spyOn($, 'ajax').and.callThrough();
            vmReq.save();
            //expect($.ajax).toHaveBeenCalled();
        })

    });

     describe('Create a BM Requirement Model and Save it to the Database', function () {
        var Model = require('../../custom/models/bm-req-model');

        it('Should load the correct class properly', function () {
            expect(Model).toBeDefined();
        });

        it('Should allow the creation of a new model object instance', function(){
            var model = new Model();
            expect(model).toBeDefined();
        })

    });

    describe('Create a Team Model and Save it to the Database', function () {
        var Model = require('../../custom/models/team-model');

        it('Should load the correct class properly', function () {
            expect(Model).toBeDefined();
        });

        it('Should allow the creation of a new model object instance', function(){
            var model = new Model();
            expect(model).toBeDefined();
        })

    });



});