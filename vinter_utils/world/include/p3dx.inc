

define p3dx_cover model
(
	block(
		points 8
		point[0] [0 0.7]
		point[1] [0.3 1]
		point[2] [0.7 1]
		point[3] [1 0.7]
		point[4] [1 0.3]
		point[5] [0.7 0]
		point[6] [0.3 0]
		point[7] [0 0.3]
		z [0 1]
	)
	size [ 0.5 0.5 0.02 ]
	color "black"	
)

define p3dx_body model
(
	block(
		points 8
		point[0] [0 0.7]
		point[1] [0.3 1]
		point[2] [0.7 1]
		point[3] [1 0.7]
		point[4] [1 0.3]
		point[5] [0.7 0]
		point[6] [0.3 0]
		point[7] [0 0.3]
		z [0 1]
	)
	size [ 0.48 0.48 0.48 ]
	color "red"
	p3dx_cover
	(
		pose [0 0 0 0]
	)
)

define p3dx position
(
	block
	(
		points 4
		point[0] [0 0]
		point[1] [0 1]
		point[2] [1 1]
		point[3] [1 0]
		z [0 1]
	)
	size [0.2 0.5 0.2]
	color "black"
	p3dx_body
	(
		pose [0 0 -0.2 0]
	)
	
	lms200
	(
		pose [0 0 0.3 0]
	)
)
