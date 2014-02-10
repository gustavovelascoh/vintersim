
define building_8 model
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
	size [ 4 4 3 ]
	color_rgba [0.2 1 0.2 0.5]	
)

define building_block model
(
	block(
		points 24
		point[0] [0.125 0.125]
		point[1] [0.125 0]		
		point[2] [0.375 0]
		point[3] [0.375 0.25]		
		point[4] [0.625 0.25]
		point[5] [0.625 0]
		point[6] [0.875 0]
		point[7] [0.875 0.5]
		point[8] [1 0.5]		
		point[9] [1 0.875]		
		point[10] [0.875 0.875]
		point[11] [0.875 1]		
		point[12] [0.75 1]
		point[13] [0.75 0.875]
		point[14] [0.5 0.875]
		point[15] [0.5 1]		
		point[16] [0.25 1]
		point[17] [0.25 0.875]
		point[18] [0 0.875]
		point[19] [0 0.625]
		point[20] [0.125 0.625]
		point[21] [0.125 0.375]
		point[22] [0 0.375]		
		point[23] [0 0.125]
		z [0 1]
	)
	size [ 1 1 1 ]
	color_rgba [0.2 1 0.2 0.1]
	laser_return 1	
)
