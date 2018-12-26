from qpsolvers import solve_qp
import numpy as np


def compute_multipliers(P, q, G, h, A, b):
	'''		
	Solves
	min 1/2 x^T P x + q^T x
	s.t.
	 Gx <= h
	 Ax = b
	'''
	solution = solve_qp(P, q, G, h, A, b, solver='quadprog')
	return solution

