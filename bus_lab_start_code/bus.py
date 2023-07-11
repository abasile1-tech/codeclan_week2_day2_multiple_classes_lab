from bus_stop import BusStop

class Bus:
	def __init__(self, route_num, destination):
		self.route_num = route_num
		self.destination = destination
		self.passengers = []

	def drive(self):
		return "Brum brum"

	def get_num_passengers(self):
		return len(self.passengers)

	def pick_up(self, passenger):
		self.passengers.append(passenger)

	def drop_off(self, passenger):
		self.passengers.remove(passenger)
	
	def empty(self):
		self.passengers = []

	def pick_up_from_stop(self, bus_stop):
		for passenger in bus_stop.queue:
			self.pick_up(passenger)
		bus_stop.empty_queue()