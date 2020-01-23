from migen import *


class MyModule(Module):
	def __init__(self):
		self.o = Signal()

		# # #

		d = Signal()
		q = Signal()

		# Combinatorial logic
		self.comb += [
			self.o.eq(q),
			d.eq(~q)
		]

		# Synchronous logic
		self.sync += d.eq(q)
