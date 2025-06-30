// Copyright (c) 2025, Maddati Tech and contributors
// For license information, please see license.txt

frappe.ui.form.on('Student Invoice', {
	refresh(frm) {
		// Add a custom button to create a Payment for this invoice
		if (!frm.is_new() && frm.doc.status !== 'Paid') {
			frm.add_custom_button(__('Create Payment'), function() {
				frappe.new_doc('Payment', {
					invoice: frm.doc.name,
					student: frm.doc.student,
					amount: frm.doc.outstanding_amount,
					payment_date: frappe.datetime.get_today(),
					status: 'Completed'
				});
			}, __('Actions'));
		}

		// Add a custom button to send invoice by email
		if (!frm.is_new()) {
			frm.add_custom_button(__('Send by Email'), function() {
				frappe.call({
					method: "shinwa_hms.scheduled_tasks.send_invoice_email",
					args: { invoice_name: frm.doc.name },
					callback: function(r) {
						frappe.msgprint(r.message);
					}
				});
			}, __('Actions'));
		}
	}
});
