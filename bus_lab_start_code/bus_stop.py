# Create a new class called BusStop. This should have a name attribute.
# Add an attribute to the BusStop called 'queue'. 
# This should be an empty list that will get filled with instances of the Person class.
# Add a method that adds a person to the queue.
# Add a method that removes all people from the queue.

class BusStop:
	def __init__(self, name):
		self.name = name
		self.queue = []

	def add_to_queue(self, person):
		self.queue.append(person)

	def empty_queue(self):
		self.queue = []

	def queue_length(self):
		return len(self.queue)

	def clear(self):
		self.empty_queue()