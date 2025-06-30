# Copyright (c) 2025, Maddati Tech and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document


class Student(Document):
	def validate(self):
		# Only check room capacity if status is Active AND room is being changed or doc is new
		if self.room and self.status == "Active":
			if self.is_new() or self.has_value_changed("room"):
				room = frappe.get_doc('Room', self.room)
				if room.occupied_beds >= (room.capacity or 0) and not self.flags.ignore_full_check:
					frappe.throw(f"Room {room.room_number} is already full. Please select another room.")

	def after_insert(self):
		if self.room:
			room = frappe.get_doc('Room', self.room)
			room.occupied_beds = (room.occupied_beds or 0) + 1
			# Update status
			if room.occupied_beds >= (room.capacity or 0):
				room.status = "Full"
			else:
				room.status = "Available"
			room.save()

	def before_save(self):
		self.update_accommodation_history()

	def update_accommodation_history(self):
		# Only run if branch and room are set
		if not self.branch or not self.room:
			return

		today = frappe.utils.today()

		# Always add a new row if status is Active and this is a new assignment
		if self.status == "Active":
			# Check if the latest row is already for this room+branch and is still active
			latest = None
			for row in self.accommodation_history:
				if row.room == self.room and row.branch == self.branch and row.status == "Active" and not row.to_date:
					latest = row
					break
			if not latest:
				self.append("accommodation_history", {
					"branch": self.branch,
					"room": self.room,
					"from_date": today,
					"status": "Active"
				})
		# If status is Left or Cancelled, close all active rows for this room+branch
		elif self.status in ["Left", "Cancelled"]:
			for row in self.accommodation_history:
				if row.room == self.room and row.branch == self.branch and row.status == "Active" and not row.to_date:
					row.to_date = today
					row.status = self.status
		# Do not remove or filter any rows; all history is preserved

	def on_update(self):
		# If status changed to Left or Cancelled, release the room
		if self.room and self.status in ["Left", "Cancelled"]:
			room = frappe.get_doc('Room', self.room)
			room.occupied_beds = max((room.occupied_beds or 1) - 1, 0)
			if room.occupied_beds < (room.capacity or 0):
				room.status = "Available"
			room.save()
			# self.room = None  # Do not clear room, keep for history

	def on_cancel(self):
		if self.room:
			room = frappe.get_doc('Room', self.room)
			room.occupied_beds = max((room.occupied_beds or 1) - 1, 0)
			# Update status
			if room.occupied_beds < (room.capacity or 0):
				room.status = "Available"
			room.save()

	def on_trash(self):
		# Always decrement occupied_beds on delete
		if self.room:
			room = frappe.get_doc('Room', self.room)
			room.occupied_beds = max((room.occupied_beds or 1) - 1, 0)
			if room.occupied_beds < (room.capacity or 0):
				room.status = "Available"
			room.save()
		# Prevent delete unless status is Left or Cancelled
		if self.status not in ["Left", "Cancelled"]:
			frappe.throw("You can only delete an Admission if its status is Left or Cancelled.")