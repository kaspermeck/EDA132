; Vi kan inte gå in i en ruta där vi inte vet vad det är.
; (ty då skulle vi kunna dö - och plannern hade kunnat springa 
; igenom planen genom att testa var den dör och då inte ta den
; vägen (dvs vi tar bort hela poängen med spelet))
;
; Därför måste vi ha någon slags 'known/safe' variabel
;
;

(define (domain wumpusworld)
	(:requirements :strips)
	(:types
		worldobj   ;assumed we got agent
		direction  ;assumed we got north, west, wouth, east
		square
		wumpus pit gold stench breeze - worldobj
	)

	(:predicates
		(sqr-north-of ?sqr ?nsqr)
		(sqr-west-of  ?sqr ?wsqr)
		(sqr-south-of ?sqr ?ssqr)
		(sqr-east-of  ?sqr ?esqr)
		(safe ?sqr)
		(maybe-in ?obj ?sqr)
		(facing ?dir)
		(in ?obj ?sqr)
	)

	(:action forward
		:parameters (
			?insqr - square
			?tosqr - square
		)
		:precondition (and
			(in agent ?insqr)
			(or
				(and (facing north) (sqr-north-of ?tosqr ?insqr))
				(and (facing west)  (sqr-west-of  ?tosqr ?insqr))
				(and (facing south) (sqr-south-of ?tosqr ?insqr))
				(and (facing east)  (sqr-east-of  ?tosqr ?insqr))
			)
		)
		:effect (and
			;move
			(in agent ?tosqr)
			(not (in agent ?insqr))

			;add to maybe in's
		)
	)

	(:action turnleft
		:effect (and
			(when (facing north) (and (facing west)  (not (facing north))))
			(when (facing west)  (and (facing south) (not (facing west) )))
			(when (facing south) (and (facing east)  (not (facing south))))
			(when (facing east)  (and (facing north) (not (facing east) )))
		)
	)

	(:action turnright
		:effect (and
			(when (facing north) (and (facing east)  (not (facing north))))
			(when (facing west)  (and (facing north) (not (facing west) )))
			(when (facing south) (and (facing west)  (not (facing south))))
			(when (facing east)  (and (facing south) (not (facing east) )))
		)
	)

)

