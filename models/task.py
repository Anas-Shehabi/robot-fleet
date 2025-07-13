# --------------------------------------------
# task.py - Task model
# --------------------------------------------


from odoo import models, fields,api
from odoo.exceptions import ValidationError


class Task(models.Model):
    _name = 'robot_fleet.task'
    _description = 'Robot Task'
    _inherit = ['mail.thread','mail.activity.mixin']
    active = fields.Boolean(default=True)

    tags_ids = fields.Many2many('task_tag')

    # add ref to present a sequences
    ref=fields.Char(default='New',readonly=1)

    name=fields.Char(string='Task Name')
    description = fields.Text(string='Task Description', tracking=1 )
    task_begins = fields.Datetime(tracking=1)
    task_ends = fields.Datetime()

    status = fields.Selection([
        ('new', 'New'),
        ('in_progress', 'In Progress'),
        ('done', 'Done')
    ], string='Status', default='new',tracking=1)

    robot_id = fields.Many2one('robot', string='Assigned Robot',tracking=1)
    task_owner_id = fields.Many2one('task.owner',tracking=1)

    robot_ids = fields.One2many('robot','task_id',tracking=1)

    source_station_id = fields.Many2one('station', string='Source Station',tracking=1)
    destination_station_id = fields.Many2one('station', string='Destination Station',tracking=1)


    def action_new(self):
        for rec in self:
            rec.status='new'

    def action_in_progres(self):
        for rec in self:
            rec.status = 'in_progress'
            for robot in rec.robot_ids:
                robot.status_robot = 'active'
                robot.current_task_id = rec.id

    def action_done(self):
        for rec in self:
            rec.status = 'done'
            rec.task_ends = fields.Datetime.now()
            for robot in rec.robot_ids:
                robot.status_robot = 'idle'
                robot.current_task_id = 1
                robot.completed_task_ids |= rec



    @api.model
    def create (self,vals):
        res = super(Task,self).create(vals)
        if res.ref == 'New':
            res.ref = self.env['ir.sequence'].next_by_code('task_seq')
        print(res.ref)
        return res

    """
    For each robot assigned to the task:
    It checks if status_robot == 'active'
    Then checks if robot.current_task_id.ref != task.ref (i.e., robot is active and working on a different task)
    If such robots exist, it blocks the assignment and gives their names
    """
    @api.constrains('robot_ids')
    def _check_robot_not_active(self):
        for task in self:
            active_robots = []
            for robot in task.robot_ids:
                if robot.status_robot == 'active':
                    if not robot.current_task_id or robot.current_task_id.ref != task.ref:
                        if robot.name not in active_robots:
                            active_robots.append(robot.name)
            if active_robots:
                robot_names = ', '.join(active_robots)
                raise ValidationError(f"Cannot assign active robot(s) to a task: {robot_names}")