import os
import openai
from translator import translate

from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)

# the line to run in the terminal window: flask --app hackopenAI run


CORS(app, origins='*')

@app.route('/')
def hello():
    return 'Hello World!'

@app.route('/addFeature/<string:question>', methods =['GET'])
def addVowels(question):
    openai.api_key = "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"


    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": question}
        ]
    )

    print(completion.choices[0].message.content)
    return completion.choices[0].message.content


# @app.route('/translate/<string:question>', methods =['GET'])
@app.route('/translate/<string:question>/<int:level>', methods=['GET'])
def translateText(question, level):

    enComp = translate(question, )
    print("english complicated: " + enComp)  # delete this
    openai.api_key = "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"
    # level = 1  ##fix
    if level == 1:
        instructions = "please rephrase the following text for a 1st grader:\n"
    if level == 2:
        instructions = "please rephrase the following text for a 3rd grader:\n"
    if level == 3:
        instructions = "please rephrase the following text for a 5th grader:\n"
    if level == 4:
        instructions = "please convert digits to words in the following text without changing the rest of the text:\n"
    if level == 5:
        instructions = "please convert words to digits in the following text without changing the rest of the text:\n"
    else:
        instructions = "please rephrase the following text for a child:\n"

    paragraph = instructions + enComp
    try:
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": paragraph}
            ]
        )
        enSimpler = completion.choices[0].message.content

        print("english simplified: ", enSimpler)

    # back to hebrew
    # try:
        heSimpler = translate(enSimpler, 'iw')
        reversed_text = heSimpler[::-1]
        print("hebrew simplified: " + reversed_text)  # delete this
        return heSimpler
    except:
        return 'מצטערים, לא נמצא מידע מתאים'





@app.route('/getText/<string:text>', methods=['GET'])
def process_text(text):
    level=1;
    first_word = text.split()[0]  # Get the first word of the text

    if first_word == "המדע":
        # Check different cases for 'apple'
        if level == 1:
            return "מדע הוא תחום מרתק וגדול שעוזר לנו ללמוד על העולם ולהבין דברים חדשים. מדענים משתמשים בדרכים מיוחדות לגלות תגליות חשובות. הם לומדים על היקום ועל כל היצורים שסביבנו. המדע יכול לעזור לנו ליצור דברים חדשים ולפתור בעיות. הוא מספק לנו ידע שמשנה את העולם ומפתח את היכולות שלנו. מדע הוא כמו אוצר גדול של ידע שעוזר לנו להבין עולם טוב יותר."
        elif level == 2:
            return "מדמדע הוא תחום מרתק וגדול שעוזר לנו ללמוד על העולם ולהבין דברים חדשים. מדענים משתמשים בדרכים מיוחדות לגלות תגליות חשובות. הם לומדים על היקום ועל כל היצורים שסביבנו. המדע יכול לעזור לנו ליצור דברים חדשים ולפתור בעיות. הוא מספק לנו ידע שמשנה את העולם ומפתח את היכולות שלנו. מדע הוא כמו אוצר גדול של ידע שעוזר לנו להבין עולם טוב יותר."
        elif level == 3:
            return "מדע הוא תחום ענק ומרתק שחוקר את הטבע ועוזר לנו להבין את העולם שסביבנו. זה הבסיס להתקדמות שלנו והוא ממלא תפקיד מכריע בחיינו. מדענים משתמשים בשיטות וניסויים מיוחדים כדי ללמוד על היקום ועל החיים עצמם. המדע מעורר את הדמיון שלנו ומוביל לתגליות ושיפורים מדהימים בחיינו. זה גם מצייד אותנו בכלים להתמודד עם בעיות מורכבות, ליצור טכנולוגיות חדשות ולהפוך את העולם שלנו לטוב יותר. כאשר אנו מתעמקים במדע, אנו נדהמים מהידע הרב שאנו צוברים ומהיכולת שלנו להבין ולהשפיע על הסביבה שלנו ועל תהליכי החיים."
        else:
            return "please Enter a different pargraph"

    elif first_word == "האסטרונומיה":
        # Check different cases for 'banana'
        if level == 1:
            return "אסטרונומיה היא מדע מיוחד שעוזר לנו ללמוד על הדברים בשמיים. אסטרונומים משתמשים בכלים כמו טלסקופים כדי לחקור כוכבים וגלקסיות שנמצאים רחוק מאוד. הם גם לומדים כיצד דברים נעים בחלל וכיצד התחיל היקום. ישנם חלקים שונים באסטרונומיה, כמו חקר כוכבים וגלקסיות, ואפילו חיפוש אחר חיים אחרים בחלל. על ידי לימוד אסטרונומיה, אנחנו יכולים ללמוד הרבה על היקום ואפילו לצאת לטיולים מגניבים לירח ולכוכבים."
        elif level == 2:
            return "אסטרונומיה הוא מדע שמציג לנו את השמיים. אנחנו משתמשים בכלים מיוחדים כמו טלסקופים כדי לחקור כוכבים וגלקסיות רחוקות. אסטרונומים חוקרים גם את מהות היקום ואיך הוא התחיל. באסטרונומיה יש חלקים שונים, כמו למדוד כוכבים וגלקסיות או לחפש חיים בחלל. כשאנחנו לומדים אסטרונומיה, אנחנו לומדים הרבה על היקום ויכולים אפילו לטייל לירח ולכוכבים בטיולים מרגשים."
        elif level == 3:
            return "המדע הוא תחום מחקר שובה לב ונרחב שחוקר את הטבע ועוזר לנו להבין את העולם בו אנו חיים. הוא סולל את הדרך להתקדמות ומאפשר לנו לגלות תגליות חדשות. באמצעות שיטות וניסויים מדעיים, מדענים מתעמקים במסתרי היקום ובמורכבות החיים. המדע מצית את הדמיון שלנו, מה שמוביל לפריצות דרך יוצאות דופן. הוא מצייד אותנו בכלים לפתרון בעיות ומשפר את חיי היומיום שלנו. על ידי אימוץ המדע, אנו צוברים ידע מעמיק ומשיגים את היכולת להשפיע לטובה על הסביבה שלנו."
        else:
            return "please Enter a different pargraph"

    elif first_word == "אין":
        # Check different cases for 'sahara island'
        if level == 1:
            return "האי סהרה הוא מקום מיוחד במדבר. זה כמו מעגל גדול ויש לו שמות שונים כמו עין תפאות ורצון דה ריצ'רד. זה היה שם הרבה מאוד זמן, בערך 400 מיליון שנה! כשמסתכלים על זה מלמעלה, זה נראה ממש מגניב. האדמה סביבו מחודדת וזה מרגיש כאילו העין נמשכת לנצח. העין לא השתנתה הרבה בכל השנים האלה. הוא מוקף בסוגים שונים של סלעים שלקח הרבה זמן להיווצר. העין מורכבת מסלעים, שלג וחול, וכולם משתלבים זה בזה בצורה מיוחדת"
        elif level == 2:
            return "אי הסהרה, הנקרא גם עין הסהרה, הוא מקום מרתק באמצע מדבר סהרה המערבית במצרים. זה נראה כמו עיגול גדול ויש לו גם שמות אחרים, כמו עין תפאות ורצון דה ריצ'רד. הוא נוצר לפני הרבה מאוד זמן, בערך 400 מיליון שנה! כשאתה רואה את זה מלמעלה, זה נראה ממש מגניב ונראה שהוא נמשך לנצח. העין לא השתנתה הרבה במהלך כל השנים האלה. הוא מוקף בשכבות שונות של סלעים שלקח זמן רב להיווצר. העין מורכבת מסלעים, שלג וחול, וכולם משתלבים זה בזה בצורה מיוחדת."
        elif level == 3:
            return "מדע הוא תחום ענק ומרתק שחוקר את הטבע ועוזר לנו להבין את העולם שסביבנו. זה הבסיס להתקדמות שלנו והוא ממלא תפקיד מכריע בחיינו. מדענים משתמשים בשיטות וניסויים מיוחדים כדי ללמוד על היקום ועל החיים עצמם. המדע מעורר את הדמיון שלנו ומוביל לתגליות ושיפורים מדהימים בחיינו. זה גם מצייד אותנו בכלים להתמודד עם בעיות מורכבות, ליצור טכנולוגיות חדשות ולהפוך את העולם שלנו לטוב יותר. כאשר אנו מתעמקים במדע, אנו נדהמים מהידע הרב שאנו צוברים ומהיכולת שלנו להבין ולהשפיע על הסביבה שלנו ועל תהליכי החיים."
        else:
            return "Invalid level entered."

    else:
        # return first_word
        return "מצטערים. לא נמצאו תוצאות מתאימות."


    # Example usage
    # input_text = input("Enter a text: ")
    # button_click = int(input("Enter button click (1-3): "))
    #
    # result = process_text(input_text, button_click)
    # print(result)
    # return result;


if __name__ == '__main__':
    app.run(debug=True)

