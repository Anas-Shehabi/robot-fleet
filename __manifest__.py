

{
    'name' : "Robot Fleet",
    'author' : "Anas Shehabi",
    'category' : 'Delivery',
    'version' : '17.0.0.1.0',

    'depends' : ['base','mail',
                ],
    'data' : [
        'security/ir.model.access.csv',
        'data/robot.csv',
        'data/station.csv',
        'data/sequence.xml',
        'views/robot_view.xml',
        'views/station_view.xml',
        'views/task_view.xml',
        'views/base_menu.xml',
        'views/owner.xml',
        'views/task_tag_view.xml',
        'views/robot_tag_view.xml',
    ],
    'assets' :{
      'web.assets_backend' :  ['robot_fleet/static/src/css/task_kanban.css']
    },

    'application': True,
    'post_init_hook': 'add_no_task_record',  # Matches function name in hooks.py
}