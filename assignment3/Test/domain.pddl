(define (domain logistics)
	(:requirements :adl)
	(:types
		obj vehicle - physobj
		truck airplane - vehicle
		location city - object
		airport - location)

	(:predicates
		(at ?x - physobj ?l - location)
		(in ?x - obj ?t - vehicle)
		(in-city ?l - location ?c - city))

	(:action drive-truck
		:parameters (
			?truck - truck
			?loc-from - location
			?loc-to - location
			?city - city)

		:precondition (and 
			(at ?truck ?loc-from)
			(in-city ?loc-from ?city)
			(in-city ?loc-to ?city))

		:effect (and 
			(at ?truck ?loc-to)
			(not (at ?truck ?loc-from))
			(forall (?x - obj)
				(when (and (in ?x ?truck))
					(and (not (at ?x ?loc-from))
						(at ?x ?loc-to)))))
	)
)