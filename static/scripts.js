
document.getElementById("copyButton").addEventListener("click", function () {

    const studentCards = document.querySelectorAll(".student-card");

    const names = [];

    studentCards.forEach(function(card) {
        const studentName = card.querySelector("h3").textContent.trim();
        names.push(studentName);
    });

    if (names.length === 0) {
        document.getElementById("message").innerText = "No names found!";
        return;
    }

    navigator.clipboard.writeText(names.join("\n"))
        .then(function() {
            document.getElementById("message").innerText =
                "Only student names copied successfully!";
        })
        .catch(function() {
            document.getElementById("message").innerText =
                "Copy failed!";
        });

});
