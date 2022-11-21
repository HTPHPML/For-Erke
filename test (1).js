let tg = {
    token: "5795536583:AAGinMCu-OZKscjiFlBmJGl4yuIx0sN-pcE", // Your bot's token that got from @BotFather 5400134944:AAF5R6tUdz89oNyQGKNlrYCe-yqr58I2i-M
    chat_id: "822011385" // The user's(that you want to send a message) telegram chat id
}

function sendMessage(that)
{
    const url = `https://api.telegram.org/bot${tg.token}/sendMessage?chat_id=${tg.chat_id}&text=${that.name.value.concat(" ", that.number.value)}`; // The url to request
    const xht = new XMLHttpRequest();
    xht.open("GET", url);
    xht.send();
}
