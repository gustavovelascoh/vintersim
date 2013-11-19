define lms200 ranger
(
	sensor
	(
		# real range
		#range [0.0 30.0]
		# scaled range (real /5)
		range [0.0 6.0]
		fov 180
		samples 361
	)
	block(
		points 6
		point[0] [0 1]
		point[1] [0.85 1]
		point[2] [1 0.85]
		point[3] [1 0.15]
		point[4] [0.85 0]
		point[5] [0 0]
		z [0 1]
	)
	color_rgba [ 0 0 1 0.9 ]
	size [ 0.25 0.25 0.25 ]
	pose [0.0 0.0 0.0 0.0]
	laser_return 1
)
