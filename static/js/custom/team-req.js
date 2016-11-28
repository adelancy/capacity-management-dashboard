/**
 * Created by adrian.p.delancy on 10/27/2016.
 */

define(function (require) {
     /*global define */
    var $ = require('jquery');
    var TeamModel = require('custom/models/team-model');
    var VMRequirement = require('custom/models/vm-req-model');
    var BMRequirement = require('custom/models/bm-req-model');


    //Do setup work here

    var module = {

        init: function () {
            /**
             * Perform the initial tasks to prepare the webpage more comments
             */
            //Todo: Send a network request to get the list of teams created

            //Check if New Team is selected and display the Create Team form.
            if ($('#select-team-dropdown option:selected').attr('value') === 'New Team') {
                this.showCreateTeamForm();
            }

            this.addButtonListeners();

        },

        addButtonListeners: function () {
            $('#select-team-dropdown').change(this.selectButtonListener(this));
            $('#create-team-form').submit(this.submitTeamForm);
            $('#create-vm-req').submit(this.submitVMRequirementForm);
            $('#bm-req-form').submit(this.submitBMRequirementForm);

        },

        showCreateTeamForm: function () {
            var createTeamForm$ = $('#create-team-form');
            createTeamForm$.show();
        },

        hideCreateTeamForm: function () {
            var createTeamForm$ = $('#create-team-form');
            createTeamForm$.hide();
        },

        selectButtonListener: function (ctx) {
            return (function (event) {
                event.preventDefault();
                var teamSelction = $('#select-team-dropdown option:selected').attr('value');
                if (teamSelction === 'New Team') {
                    ctx.showCreateTeamForm();
                } else {
                    ctx.hideCreateTeamForm();
                }
            });
        },

        submitTeamForm: function (event) {
            "use strict";
            //event.preventDefault();

            var data = $('#create-team-form').find('form').serializeArray(); //Get the form data
            window.console.log(data);
            //Create new Team Model to sync with DB
            //var teamModel = new TeamModel(data);
            //console.log(teamModel);
            //teamModel.save()
            //this.submit(data);
        },

        submitVMRequirementForm: function(event) {
            "use strict";
            event.preventDefault();
            //Todo: Get currently selected Team
            var teamID = $('#select-team-dropdown').attr('value'); //Todo: update so this returns the team ID.
            var data = $('#create-vm-req').find('form').serializeArray(); //Get the form data
            data.push({name: 'team-id', value: teamID});
            console.log(data);
            var vmReq = new VMRequirement();
            vmReq.setAttributesAsArray(data);
            console.log(vmReq);
            vmReq.save();
        },

        submitBMRequirementForm: function(event) {
            "use strict";
            event.preventDefault();
            //Todo: Get currently selected Team
            var teamID = $('#select-team-dropdown').attr('value'); //Todo: update so this returns the team ID.
            var data = $('#team-form form').serializeArray(); //Get the form data
            data.push({name: 'team-id', value: teamID});
            console.log(data);
            var bmReq = new BMRequirement();
            bmReq.setAttributesAsArray(data);
            console.log(bmReq);
            bmReq.save();
        }
    };

    return function() {
        module.init();

    }(); //Execute the module once loaded
});