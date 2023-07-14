import zutil.farm as f
f.create_trbx_zcfd_input(case_name='basecase',
                         wind_direction=270.0,
                         reference_wind_speed=10.0,
                         terrain_file='turbine.stl',
                         report_frequency=100,
                         update_frequency=50,
                         reference_point_offset=0.0,# for this case, the TRBX file has been calibrated to velocity at the turbine hub
                         turbine_zone_length_factor=1.0,
                         model='simple',
                         turbine_files=[['xy_turbine.txt', 'Siemens_SWT_2.3-93_106.5d_2.3MW_R93m_H63.3m_Air1.225.trbx']],
                         calibration_offset=0.0)
