def add_no_task_record(env):
    Task = env['robot_fleet.task']
    print("🚀 pre_init_hook called")
    if not Task.search([('name', '=', 'No Task')]):
        Task.create({
            'name': 'No Task',
            'status': 'new',
            'description': 'Default task when no task is assigned',
        })

