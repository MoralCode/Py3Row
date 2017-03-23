def testfind_noerror(self, pyrow):
        try:
            ergs = pyrow.find()
        except Exception as e:
            self.fail("pyrow.find() raised the following exception unexpectedly: {}".format(e))
        self.assertTrue(len(list(ergs))>0, "No ergs found")

def testpyrow_setUp(self, pyrow):
    erg_list = list(pyrow.find())
    if len(erg_list) == 0:
        self.fail("No ergs found")
    self.erg = pyrow.PyRow(erg_list[0])

def testpyrow_noerror(self, pyrow):
    ergs = list(pyrow.find())
    if len(ergs) == 0:
        self.fail("pyrow.find() returned no ergs")
    try:
        erg = pyrow.PyRow(ergs[0])
    except Exception as e:
        self.fail("pyrow.PyRow() raised the following exception unexpectedly: {}".format(e))

def testpyrow_get_monitor(self, pyrow):
    default_keys = [
        'time', 'distance', 'spm', 'power',
        'pace', 'calhr',
        'calories', 'heartrate',
        'status'
    ]
    forceplot_keys = [
        'forceplot', 'strokestate',
    ]

    monitor = self.erg.get_monitor()
    self.assertIs(type(monitor), dict)
    for item in default_keys:
        self.assertIn(item, monitor)

    monitor = self.erg.get_monitor(forceplot=True)
    self.assertIs(type(monitor), dict)
    for item in default_keys + forceplot_keys:
        self.assertIn(item, monitor)

def testpyrow_get_forceplot(self, pyrow):
    keys = [
        'forceplot', 'strokestate', 'status'
    ]
    monitor = self.erg.get_forceplot()
    self.assertIs(type(monitor), dict)
    for item in keys:
        self.assertIn(item, monitor)

def testpyrow_get_workout(self, pyrow):
    keys = [
        'userid', 'type', 'state', 'inttype', 'intcount', 'status'
    ]
    monitor = self.erg.get_workout()
    self.assertIs(type(monitor), dict)
    for item in keys:
        self.assertIn(item, monitor)
