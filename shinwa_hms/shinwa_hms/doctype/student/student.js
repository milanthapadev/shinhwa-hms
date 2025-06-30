frappe.ui.form.on('Student', {
    onload(frm) {
        frm.fields_dict.room.get_query = function (doc) {
            return {
                filters: {
                    branch: frm.doc.branch
                },
                query: "shinwa_hms.custom_room_query_with_status"
            };
        };
    },
    branch(frm) {
        frm.set_value('room', null); // Clear room when branch changes
        frm.fields_dict.room.get_query = function (doc) {
            return {
                filters: {
                    branch: frm.doc.branch
                },
                query: "shinwa_hms.custom_room_query_with_status"
            };
        };
    },
    room(frm) {
        if (frm.doc.room) {
            frappe.db.get_value('Room', frm.doc.room, 'price', (r) => {
                frm.set_value('monthly_fee', r.price || 0);
            });
        } else {
            frm.set_value('monthly_fee', 0);
        }
    },
    extra_services_add(frm) {
        // Wait for the row to be fully added before calculating
        setTimeout(() => calculate_extra_services_fees(frm), 100);
    },
    extra_services_remove(frm) {
        calculate_extra_services_fees(frm);
    },
    extra_services_amount(frm, cdt, cdn) {
        calculate_extra_services_fees(frm);
    },
    extra_services_edit(frm) {
        calculate_extra_services_fees(frm);
    }
});

frappe.ui.form.on('Student Extra Service', {
    amount: function(frm, cdt, cdn) {
        calculate_extra_services_fees(frm);
    },
    service: function(frm, cdt, cdn) {
        calculate_extra_services_fees(frm);
    },
    extra_services_remove: function(frm) {
        calculate_extra_services_fees(frm);
    }
});

function calculate_extra_services_fees(frm) {
    let total = 0;
    (frm.doc.extra_services || []).forEach(row => {
        total += flt(row.amount);
    });
    frm.set_value('extra_services_fees', total);
}