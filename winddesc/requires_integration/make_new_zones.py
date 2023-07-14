import zutil.farm as f
f.generate_inputs(base_case='basecase', wind_direction=270.0, wind_speed=10.0, wind_height=63.3, roughness_length=0.03,turbine_info=[['xy_turbine.txt', 'Siemens_SWT_2.3-93_106.5d_2.3MW_R93m_H63.3m_Air1.225.trbx']], terrain_file='turbine.stl')

