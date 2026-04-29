<<<<<<< HEAD
const serverTimeEl = document.getElementById("serverTime");

function updateTime() {
    const now = new Date();
    serverTimeEl.textContent = now.toLocaleString("ru-RU");
}

updateTime();
=======
const serverTimeEl = document.getElementById("serverTime");

function updateTime() {
    const now = new Date();
    serverTimeEl.textContent = now.toLocaleString("ru-RU");
}

updateTime();
>>>>>>> aa4e107e081c9951a176cd917952f3a9595c390e
setInterval(updateTime, 1000);