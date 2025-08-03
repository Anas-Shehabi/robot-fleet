

{
    'name' : "Robot Fleet",
    'author' : "Anas Shehabi",
    'category' : 'Delivery',
    'version' : '17.0.0.1.0',

    'depends' : ['base','mail',
                ],
    'data' : [
        'security/ir.model.access.csv',
        'security/security.xml',
        'data/robot.csv',
        'data/station.csv',
        'data/sequence.xml',
        'views/maintenance.xml',
        'views/robot_view.xml',
        'views/station_view.xml',
        'views/task_view.xml',
        'views/owner.xml',
        'views/task_tag_view.xml',
        'views/robot_tag_view.xml',
        'views/base_menu.xml',
        'Report/maintenance.xml',
        'Report/task_report.xml'
    ],
    'assets' :{
      'web.assets_backend' :  ['robot_fleet/static/src/css/task_kanban.css',
                               'robot_fleet/static/src/js/kanban_disable_drag.js',]
    },

    'application': True,
    'post_init_hook': 'add_no_task_record',  # Matches function name in hooks.py
}