/**
 * Created by adrian.p.delancy on 10/27/2016.
 */

define(['custom/models/team-model'], function (TeamModel) {
    //Do setup work here

    var module = {

        init: function () {
            /**
             * Perform the initial tasks to prepare the webpage
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
            $('#create-team-form').find('form input:submit').on('submit', this.submitTeamForm);
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
            event.preventDefault();
            var data = $('#team-form form').serializeArray(); //Get the form data
            window.console.log(data);
        }
    };

    return function() {
        module.init();

    }(); //Execute the module once loaded
});