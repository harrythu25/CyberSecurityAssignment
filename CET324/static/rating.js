
var resultMessage = document.getElementById("result-message");
var input = document.getElementById("pasword-to-test");


let lowercaseRegex = new RegExp('(?=.*[a-z])');
let uppercaseRegex = new RegExp('(?=.*[A-Z])');
let numericRegex = new RegExp('(?=.*[0-9])');
let specialcharRegex = new RegExp('(?=.*[*.!@$%^&(){}[]:;<>,.?/~_+-=|\])');


var a = document.getElementById("no-lowercase");
var ayes = document.getElementById("yes-lowercase");

var b = document.getElementById("no-uppercase");
var byes = document.getElementById("yes-uppercase");

var c = document.getElementById("no-numeric");
var cyes = document.getElementById("yes-numeric");

var d = document.getElementById("no-special");
var dyes = document.getElementById("yes-special");


function clearFunction() {
    resultMessage.style.color = "black";
}
function possiblepasswords(word) {
    total = 1;
    for (var i = 0; i < word.length; i++) {
        if (word[i] >= "A" && word[i] <= "Z") {
            total = total * 26;
        }
        else if (word[i] >= "a" && word[i] <= "z") {
            total = total * 26;
        }
        else if (word[i] >= "0" && word[i] <= "9") {
            total = total * 10;
        }
        else {
            total = total * 33;
        }
    }
    return (Math.log10(total));
}
input.addEventListener('keyup', function () {
    result = zxcvbn(input.value)

    document.getElementById("result-attempts").textContent = result.guesses_log10;
    document.getElementById("result-score").textContent = result.score;
    document.getElementById("result-warning").textContent = result.feedback.warning;
    document.getElementById("total-possible").textContent = possiblepasswords(input.value);


    if (lowercaseRegex.test(input.value)) {
        a.style.display = "none";
        ayes.style.display = "block";
    }
    else {
        a.style.display = "block";
        ayes.style.display = "none";
    }


    if (uppercaseRegex.test(input.value)) {
        b.style.display = "none";
        byes.style.display = "block";
    }
    else {
        b.style.display = "block";
        byes.style.display = "none";
    }

    if (numericRegex.test(input.value)) {
        c.style.display = "none";
        cyes.style.display = "block";
    }
    else {
        c.style.display = "block";
        cyes.style.display = "none";
    }

    if (specialcharRegex.test(input.value)) {
        d.style.display = "none";
        dyes.style.display = "block";
    }
    else {
        d.style.display = "block";
        dyes.style.display = "none";
    }

})


