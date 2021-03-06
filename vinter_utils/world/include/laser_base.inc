

define laser_base position
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
	size [ 0.4 0.4 0.4 ]
	color_rgba [0.2 0.2 0.2 0.8]
	lms200
	(
		pose [0 0 0 0]
	)
	laser_return 1
)
