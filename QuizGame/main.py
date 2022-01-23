from data import question_data
from question_model import Question
from random import shuffle
#from quiz_brain import QuizBrain

pitanje = []
ponudjeni_odgovori =[]
ponudjen_odgovor = []
tacan_odgovor = []
for element in question_data:
    pitanje.append(element["question"])
    ponudjen_odgovor.append(element["correct_answer"])
    tacan_odgovor.append(element["correct_answer"])
    for el in element["incorrect_answers"]:
        ponudjen_odgovor.append(el)
    shuffle(ponudjen_odgovor)
    ponudjeni_odgovori.append(ponudjen_odgovor)
    ponudjen_odgovor = []
quiz = Question(pitanje, ponudjeni_odgovori, tacan_odgovor)
while quiz.da_li_ima_jos_pitanja():
    quiz.postavi_pitanje()
print("Kviz je zavrsen!")
print("Vas ukupan skor je: {}/{}".format(quiz.rezultat, quiz.pitanje_broj))
