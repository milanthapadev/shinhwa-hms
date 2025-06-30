// Copyright (c) 2025, Maddati Tech and contributors
// For license information, please see license.txt

frappe.ui.form.on("Complaint-Request", {
	refresh(frm) {

	},
	branch: function(frm) {
		frm.set_query("room", function() {
			if (frm.doc.branch) {
				return {
					filters: {
						branch: frm.doc.branch
					}
				};
			}
		});
	},
	onload: function(frm) {
		frm.trigger("branch");
	}
});
