class CheckSafeReplication(object):

    def __init__(self, params):
        self.params = params

    def get_slave_status(self):
        res = {}
        slave_status_dict = Env.database.get_slave_status_dict()
        res['slave_io_running'] = slave_status_dict['Slave_IO_Running']
        res['slave_sql_running'] = slave_status_dict['Slave_SQL_Running']
        res['last_io_error'] = slave_status_dict['Last_IO_Error']
        res['last_sql_error'] = slave_status_dict['Last_SQL_Error']

        return res

    def __call__(self):
        res = dict(is_slave=Env.database.is_slave)

        if Env.database.is_slave:
            res.update(Env.database.get_multi_variables_value('relay_log_recovery',
                                                              'relay_log_info_repository'))

            res.update(self.get_slave_status())

        return res
