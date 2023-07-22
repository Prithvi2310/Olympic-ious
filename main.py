from flask import Flask, render_template, request

app = Flask(__name__)

class Question:
    q_id = -1
    question = ""
    option1 = ""
    option2 = ""
    option3 = ""
    correctOption = -1

    def __init__(self, q_id, question, option1, option2, option3, correctOption):
        self.q_id = q_id
        self.question = question
        self.option1 = option1
        self.option2 = option2
        self.option3 = option3
        self.correctOption = correctOption

    def get_correct_option(self):
        if self.correctOption == 1:
             return self.option1
        elif self.correctOption == 2:
            return self.option2
        elif self.correctOption == 3:
            return self.option3

q1 = Question(1, "What is the Olympic motto in Latin and what does it mean in English?", "Citius, Altius, Fortius (Faster, Higher, Stronger)", "xyz", "abc", 1)
q2 = Question(2, "Which athlete has won the most gold medals in Olympic history?", "Michael Phelps", "Prithvi Shah", "Usain Bolt", 1)
q3 = Question(3, "Which city has hosted the most Olympic Games?", "London, UK", "Bejin, Japan", "Paris, France", 1)
q4 = Question(4, "In which sport did the 'Miracle on Ice' take place during the 1980 Winter Olympics?", "Ice Skating", "Volleyball", "Ice Hockey", 3)

questions_list = [q1, q2, q3, q4]

@app.route("/quiz")
def quiz():
    return render_template("quiz.html", questions_list = questions_list)

@app.route("/submitquiz", methods=['POST', 'GET'])
def submit():
    value = request.form['option']
    return value

if __name__ == "__main__":
    app.run(debug=True)