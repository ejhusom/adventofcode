/* Open index.html, and import file 'expense-report.txt'. The solution to the
 * puzzles will be written to the console.
 */

const fileSelector = document.getElementById("file-selector");
fileSelector.addEventListener("change", (event) => {
    const file = event.target.files;
});

document.getElementById('import').onclick = function () {
    var file = document.getElementById('file-selector').files[0];

    var reader = new FileReader();

    reader.onload = function (e) {
        var string = e.target.result;

        var num = "";
        var numbers = [];


        // Read numbers from file
        for (i = 0; i < string.length; i++) {

            if (string[i] !== "\n") {
                num = num + string[i];
            } else {
                numbers.push(Number(num));
                num = "";
            }

        }

        // Puzzle 1
        for (i = 0; i < numbers.length; i++) {
            var number1 = numbers[i];
            for (j = i+1; j < numbers.length; j++) {
                var number2 = numbers[j];

                if (number1 + number2 === 2020) {
                    console.log(number1*number2);
                }
            }
        }

        // Puzzle 2
        for (i = 0; i < numbers.length; i++) {
            var number1 = numbers[i];
            for (j = i+1; j < numbers.length; j++) {
                var number2 = numbers[j];
                for (k = j+1; k < numbers.length; k++) {
                    var number3 = numbers[k];

                    if (number1 + number2 + number3 === 2020) {
                        console.log(number1*number2*number3);
                    }
                }
            }
        }
    }
    reader.readAsText(file);
}
