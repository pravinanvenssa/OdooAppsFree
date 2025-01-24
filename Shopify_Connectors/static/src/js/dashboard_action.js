odoo.define('custom_dashboard.dashboard_action', function (require) {
    "use strict";

    const publicWidget = require('web.public.widget');
    const { _t } = require('web.core');

    publicWidget.registry.DashboardCardClick = publicWidget.Widget.extend({
        selector: '.o_dashboard_card', // Targeting the card element
        events: {
            'click': '_onCardClick', // Trigger action when the card is clicked
        },

        /**
         * Handle card click event and trigger corresponding action
         * @param {Event} event - The click event
         */
        _onCardClick: function (event) {
            event.preventDefault();
            const actionId = $(event.currentTarget).data('action-id'); // Get the action ID from the clicked card
            if (actionId) {
                this.do_action(actionId); // Trigger the corresponding action dynamically
            } else {
                console.warn('No action found for the clicked card.');
            }
        },
    });
});
