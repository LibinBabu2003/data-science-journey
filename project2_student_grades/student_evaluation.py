class School:
    def __init__(self,student,stu_id,marks):
        self.student=student
        self.stu_id=stu_id
        self.marks=marks
    def calc_total(self):
        a=0
        for i in self.marks.values():
            a+=i
        return a
    def calc_avg(self):
        return self.calc_total() / len(self.marks)

    def grade(self):
        if self.calc_avg()>90:
            return "A"
        elif self.calc_avg() >75:
            return "B"
        else:
            return  "c"
    def show_result(self):
        print(f"name:{self.student} \n student id:{self.stu_id} \n marks:{self.marks} \n average:{self.calc_avg()}, \n grade:{self.grade()}")

my=School("Libin",12,{"maths":98,"english":88,"malayalam":76})
my.calc_total()
my.calc_avg()
my.grade()
my.show_result()
