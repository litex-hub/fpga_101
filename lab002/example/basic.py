from migen import *


class MyModule(Module):
	def __init__(self):
		self.o = Signal()

		# # #

		d = Signal()
		q = Signal()

		# combinatorial logic
		self.comb += [
			self.o.eq(q),
			d.eq(~q)
		]

		# synchronous logic
		self.sync += d.eq(q)
