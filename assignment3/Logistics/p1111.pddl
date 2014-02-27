


(define (problem logistics-c1-s1-p1-a1)
(:domain logistics-strips)
(:objects a0 
          c0 
          t0 
          l00 
          p0 
)
(:init
(AIRPLANE a0)
(CITY c0)
(TRUCK t0)
(LOCATION l00)
(in-city  l00 c0)
(AIRPORT l00)
(OBJ p0)
(at t0 l00)
(at p0 l00)
(at a0 l00)
)
(:goal
(and
(at p0 l00)
)
)
)


