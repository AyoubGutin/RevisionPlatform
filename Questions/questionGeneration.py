import math
import os
import sqlite3
import random


def generateMathQuestion(difficulty):
    """
    Function for generating math questions for inserting into the database.
    """
    operators = ["+", "-", "*", "/"]

    if difficulty == 1:
        # Simple math questions that have operations
        num1 = random.randint(1,100)
        num2 = random.randint(1, 100)
        operator = random.choice(operators)
        question = f"What Is {num1} {operator} {num2}?"
        answer = eval(f"{num1}{operator}{num2}")
        isCorrect = False
        points = 5

    if difficulty == 2:
        # Algebra math questions
        a = random.randint(1,10)
        b = random.randint(1,30)
        c = random.randint(1,100)
        question = f"What Is x When: {a}x + {b} = {c}"
        answer = (c - b) / a
        isCorrect = False
        points = 10

    if difficulty == 3:
        # Geometry Math Questions
        length = random.randint(1,50)
        width = random.randint(1,50)
        radius = random.randint(1,30)
        choice = random.randint(1,4)
        isCorrect = False
        points = 15

        if choice == 1:
            question = f"Calculate the area of a rectangle:\nWidth = {width} Length = {length}"
            answer = width * length

        if choice == 2:
            question = f"Calculate the perimeter of a rectangle:\nWidth = {width} Length = {length}"
            answer = 2 * (width + length)

        if choice == 3:
            question = f"Calculate the area of a circle to 3 decimal places:\nRadius = {radius}"
            answer = round(math.pi * radius**2, 3)

        if choice == 4:
            question = f"Calculate the circumference of a circle to 3 decimal places:\nRadius = {radius}"
            answer = round(2*math.pi*radius, 3)

    answer = round(answer)
    return question, answer, isCorrect, points


def insertQuestion(questionText, answer, isCorrect, points):

    # Database connection
    projectRoot = "C:\\Users\\washb\\PycharmProjects\\RevisionPlatform"
    dbPath = os.path.join(projectRoot, "user_database.db")

    try:
        conn = sqlite3.connect(dbPath)
    except sqlite3.Error as e:
        print("SQLITE ERROR", e)

    difficultyLevel = 3
    cursor = conn.cursor()
    cursor.execute("""
                    INSERT INTO questions(questionText, answer, isCorrect, difficultyLevel, points)
                    VALUES (?, ?, ?, ?, ?)
                """, (questionText, answer, isCorrect, difficultyLevel, points))

    conn.commit()

for n in range(0,50):
    question, answer, isCorrect, points = generateMathQuestion(3)
    insertQuestion (question, answer, isCorrect, points)