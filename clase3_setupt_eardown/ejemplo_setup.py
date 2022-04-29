class TestSuite:
    @classmethod
    def setup_class(cls):
        print("SE EJECUTA UNA SOLA VEZ AL INICIO")

    def setup_method(self):
        print("SE EJECUTA ANTES DE CADA TEST CASE")

    def test_first(self):
        print("TEST FIRST")

    def test_second(self):
        print("TEST SECOND")

    def test_third(self):
        print("TEST THIRD")

    def do_something(self):
        pass

    def teardown_method(selfs):
        print("SE EJECUTA AL FINAL DE CADA TEST CASE")

    @classmethod
    def teardown_class(cls):
        print("SE EJECUTA UNA SOLA VEZ AL FINAL")