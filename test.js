// let tg = {
//     token: "5795536583:AAGinMCu-OZKscjiFlBmJGl4yuIx0sN-pcE", // Your bot's token that got from @BotFather 5400134944:AAF5R6tUdz89oNyQGKNlrYCe-yqr58I2i-M
//     chat_id: "822011385" // The user's(that you want to send a message) telegram chat id
// }
//
// function sendMessage(that)
// {
//     const url = `https://api.telegram.org/bot${tg.token}/sendMessage?chat_id=${tg.chat_id}&text=${that.name.value.concat(" ", that.number.value)}`; // The url to request
//     const xht = new XMLHttpRequest();
//     xht.open("GET", url);
//     xht.send();
// }

// Get the modal
var modal = document.getElementById("myModal");
// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

var container = document.getElementsByClassName("main");

function search(){
    modal.style.display = "block";
}
//
// async function test() {
//     let vin = document.getElementById("vin").value;
//     let url = 'https://baza-gai.com.ua/vin/' + vin;
//     let request = fetch(url, {
//         headers: {
//             "Accept": "application/json",
//             "X-Api-Key": "cb3c3367bfef96abaf6a85645c8c8418"
//         }
//     }).then(r => r.json());
//     let data = await request;
//     // document.getElementById("p1").innerHTML = "Стоимость 10,000тг";
//     // или
//     // let data; request.then(d => data = d);
//
// }

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
    modal.style.display = "none";
}

// When the user clicks anywhere outside the modal, close it
window.onclick = function(event) {
    if (event.target === modal) {
        modal.style.display = "none";
    }
}
