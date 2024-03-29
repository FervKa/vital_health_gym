import datetime


class General_report:
    def __init__(self, type_report: str):
        self.id = 0
        self.type_report = type_report
        self.new_users: 0
        self.last_report_generated = datetime.datetime.now()

    @property
    def get_last_report_generated(self):
        return self.last_report_generated

    @get_last_report_generated.setter
    def set_last_report_generated(self, date):
        self.last_report_generated = datetime.date.fromisoformat(
            date.strftime("%Y-%m-%d")
        )


""" date = datetime.date.fromisoformat(currentDay.strftime("%Y-%m-%d")) """


report_one = General_report("Day")
report_one.set_last_report_generated = datetime.datetime.now()
print(report_one.get_last_report_generated)
