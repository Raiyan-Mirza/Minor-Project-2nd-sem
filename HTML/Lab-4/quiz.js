const quizQuestions = [
    {
        question: "What is 12 * 4?",
        answer: "48"
    }

];

function runQuiz() {
    let score = 0; 
    const totalQuestions = quizQuestions.length;

    for (let i = 0; i < totalQuestions; i++) {
        const currentQuizItem = quizQuestions[i];

        const userAnswer = prompt(currentQuizItem.question);

        if (userAnswer === null) {
            alert("Quiz interrupted. Exiting game.");
            return;
        }

        const normalizedUserAnswer = userAnswer.toLowerCase().trim();
        
        const acceptedAnswers = currentQuizItem.answer; 

        if (normalizedUserAnswer === acceptedAnswers) {
            alert("Correct!");
            score++;
        } else {
        
            alert(`Wrong! A correct answer was: ${acceptedAnswers}`);
        }
    }

    alert(`Quiz Over! Your final score is ${score} out of ${totalQuestions}.`);
}

function startGame() {
    let playAgain = true;

    while (playAgain) {
        runQuiz();

        playAgain = confirm("Do you want to play the Prompt Quizzer again?");
    }

    alert("Thanks for playing! Goodbye.");
}

startGame();