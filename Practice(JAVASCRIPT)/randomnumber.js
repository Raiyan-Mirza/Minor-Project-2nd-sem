let min = 1;
let max = 100;
let answer = Math.floor(Math.random() * ((max - min) + 1) + min);

let attempt = 0;
let guess;
let running = true;

while (running) {

    guess = window.prompt((`Guess a Number between 1-100`))
    guess = Number(guess)
    console.log(typeof guess, guess)

    if (isNaN(guess)) {
        window.alert(`Invalid Input! Try again.`)
    }

    else if (guess > max || guess < min) {
        window.alert(`Out of limits, stay within ${min} to ${max}.`)
    }

    else {
        attempt++

        if (guess < answer)
            window.alert(`TOO LOW! TRY AGAIN.`)

        else if (guess > answer)
            window.alert(`TOO HIGH! TRY AGAIN.`)

        else if (guess == answer)
            window.alert(`YOU HAVE GUESS THE ${answer} AND YOU TOOK ${attempt}ATTEMPTS.`)

        else {
            window.alert(`ERROR!`)
            running = false;
        }
       
    }

}






