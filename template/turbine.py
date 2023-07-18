name='turbine'
import zutil
import math    

parameters = { 

'units' : 'SI',
'reference' : 'IC_1',
'restart' : False,
'partitioner' : 'metis',
'time marching' : { 
                   'unsteady' : {
                                 'total time' : 1.0,
                                 'time step' : 1.0,
                                 'order' : 'second',
                                 'start' : 0,
                                },
                   'scheme' : {
                               'name' : 'runge kutta',
                               'stage': 5,
                               },
                   'multigrid' : 4,            
                   'cfl' : 1.0,
                   'cfl transport' : 1.0,
                   'cycles' : 2000,
                  },

'equations' : 'RANS',

'RANS' : {
               'order' : 'second',
               'limiter' : 'vanalbada',
               'precondition' : True,                                          
               'turbulence' : {
                                'model' : 'sst',
                                'betastar' : 0.03,
                              },
               },
'material' : 'air',
'air' : {
        'gamma' : 1.4,
        'gas constant' : 287.0,
        'Sutherlands const': 110.4,
        'Prandtl No' : 0.72,
        'Turbulent Prandtl No' : 0.9,
        },
'IC_1' : {
          'temperature' : 288.15,
          'pressure' : 101325.0,
          'V': {
                'vector' : [11.03,0.0,0.0],
                },
          # 'Reynolds No' : (9.0e-05),
          'viscosity' : 1.79e-05,
          'Reference Length' : 63.3,#9.0e-05, 0.416
          'turbulence intensity': 0.104413,
          'eddy viscosity ratio': 1.10223e+06,
          'ambient turbulence intensity': 1e-20,
          'ambient eddy viscosity ratio': 1e-20,
          'profile' : {
                       'field': 'profile_270p00_10p00.vtp',
                       'use wall distance' : True,
                      },
         },
'BC_1' : {
          'zone' : [4],
          'type' : 'wall',
          'kind' : 'wallfunction',
          'roughness': {
                        'type' : 'length',
                        'scalar': 0.03,
                        },
         },
'BC_2' : {
          'zone' : [5],
          'type' : 'symmetry',
         # 'condition' : 'IC_1',
         # 'kind' : 'riemann',
         },
'BC_3' : {
          'zone' : [0,1,2,3] ,
          'type' : 'farfield',
          'kind' : 'riemann',
          'condition' : 'IC_1',
         },
'write output' : {
                  'format' : 'vtk',
                  'surface variables': ['V','p','T','rho','cp','yplus','ut','cf','frictionforce'],
                  'volume variables': ['V','p','T','rho','eddy','ti','var_6','walldist','Qcriterion','MomentumSource'],
                  'frequency' : 100,
                  'scripts': ["catalyst.py"],
                 },         
'report' : {
            'frequency' : 10,
            'monitor' : {
                        },
           },                   
}
