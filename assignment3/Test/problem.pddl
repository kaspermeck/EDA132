(define (problem test)

	(:domain logistics)

	(:objects
		t1 t2 - truck
		l1 l2 - location
		c1 - city
		x1 x2 x3 x4 - obj
	)

	(:init
		(at x1 l1)
		(at x2 l1)
		(at x3 l1)
		(at x4 l1)

		(in x1 t1)
		(in x2 t1)
		(in x3 t1)
		(in x4 t2)

		(in-city l1 c1)
		(in-city l2 c1)

		(at t1 l1)
		(at t2 l1)
	)
	(:goal (and
		(at x1 l2)
		(at x2 l2)
		(at x3 l2)
		(at x4 l2)
	))
)