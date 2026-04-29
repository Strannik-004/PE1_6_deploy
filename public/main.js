const serverTimeEl = document.getElementById("serverTime");

function updateTime() {
  const now = new Date();
  serverTimeEl.textContent = now.toLocaleString("ru-RU");
}

updateTime();
setInterval(updateTime, 1000);
