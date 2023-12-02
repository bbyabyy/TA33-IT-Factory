from Cursuri.course_14_15.unit_testing.app.mini_calculator import Mini_Calculator


class Test_Mini_Calc_Substraction():

    def setup_method(self):
        # instructiuni de inceput
        self.calc = Mini_Calculator() # cream un obiect al clasei Mini_Calculator

    def teardown_method(self):
        pass
        # aici se scriu instructiuni executate la final

    def test_substraction(self):
        assert self.calc.substraction(20, 7) == 13