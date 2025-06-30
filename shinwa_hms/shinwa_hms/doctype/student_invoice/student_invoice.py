# Copyright (c) 2025, Maddati Tech and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from frappe.utils import nowdate

class StudentInvoice(Document):
    def validate(self):
        # Calculate total from items, ensuring all amounts are numbers
        self.total = sum([float(item.amount or 0) for item in self.items])

        # Calculate total payments made
        payments = frappe.get_all(
            'Payment',
            filters={'invoice': self.name, 'status': 'Completed'},
            fields=['amount']
        )
        paid_amount = sum([float(p.amount or 0) for p in payments])

        # Set outstanding amount
        self.outstanding_amount = self.total - paid_amount

        # Set status
        if self.outstanding_amount <= 0:
            self.status = 'Paid'
        elif self.due_date and str(self.due_date) < nowdate():
            self.status = 'Overdue'
        else:
            self.status = 'Submitted'

    def on_submit(self):
        # Mark as submitted if not already paid
        if float(self.outstanding_amount) > 0:
            if self.due_date and str(self.due_date) < nowdate():
                self.status = 'Overdue'
            else:
                self.status = 'Submitted'
        else:
            self.status = 'Paid'

    def on_cancel(self):
        # Mark as draft on cancel
        self.status = 'Draft'

    def get_linked_payments(self):
        # Returns a list of payments linked to this invoice
        return frappe.get_all('Payment', filters={'invoice': self.name}, fields=['name', 'amount', 'payment_date', 'status'])

    def onload(self):
        # Clear and repopulate linked_payments child table
        self.set('linked_payments', [])
        payments = frappe.get_all(
            'Payment',
            filters={'invoice': self.name},
            fields=['name', 'amount', 'payment_date', 'docstatus', 'status']
        )
        for p in payments:
            payment_status = p.status
            if p.docstatus == 2:
                payment_status = 'Cancelled'
            self.append('linked_payments', {
                'payment': p.name,
                'amount': p.amount,
                'payment_date': p.payment_date,
                'status': payment_status
            })

