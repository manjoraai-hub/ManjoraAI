// BOOK RECOMMENDATION SYSTEM

async function getBooks(){

    let category =
    document.getElementById("category")?.value;

    let subject =
    document.getElementById("subject")?.value;

    if(category === "" || subject === ""){

        alert("Please select category and subject");

        return;
    }

    let response =
    await fetch(
        `/get_books?category=${category}&subject=${subject}`
    );

    let books =
    await response.json();

    let bookList =
    document.getElementById("bookList");

    if(!bookList){
        return;
    }

    bookList.innerHTML = "";

    books.forEach(book => {

        let li =
        document.createElement("li");

        li.innerText =
        "📘 " + book;

        bookList.appendChild(li);
    });
}


// CAREER ROADMAP

async function getRoadmap(){

    let goal =
    document.getElementById("careerGoal")?.value;

    if(goal === ""){

        alert("Please select a career goal");

        return;
    }

    let response =
    await fetch(
        `/get_roadmap?goal=${goal}`
    );

    let roadmap =
    await response.json();

    let roadmapList =
    document.getElementById("roadmapList");

    if(!roadmapList){
        return;
    }

    roadmapList.innerHTML = "";

    roadmap.forEach(step => {

        let li =
        document.createElement("li");

        li.innerText =
        "🚀 " + step;

        roadmapList.appendChild(li);
    });
}


// STUDY PLANNER

let totalTasks = 0;
let totalHours = 0;

let subjects = [];
let hoursData = [];

function addStudyTask(){

    let subject =
    document.getElementById("subject")?.value;

    let hours =
    parseInt(
        document.getElementById("hours")?.value
    );

    if(subject === "" || isNaN(hours)){

        alert("Please enter subject and hours");

        return;
    }

    let studyList =
    document.getElementById("studyList");

    let li =
    document.createElement("li");

    li.innerText =
    "📘 " + subject + " — " + hours + " Hours";

    studyList.appendChild(li);

    totalTasks++;
    totalHours += hours;

    let totalTasksElement =
    document.getElementById("totalTasks");

    let totalHoursElement =
    document.getElementById("totalHours");

    if(totalTasksElement){

        totalTasksElement.innerText =
        totalTasks;
    }

    if(totalHoursElement){

        totalHoursElement.innerText =
        totalHours;
    }

    subjects.push(subject);

    hoursData.push(hours);

    updateChart();

    document.getElementById("subject").value = "";

    document.getElementById("hours").value = "";
}


// SMART TIMETABLE

function generateTimetable(){

    let timetable =
    document.getElementById("timetable");

    if(!timetable){
        return;
    }

    timetable.innerHTML = "";

    let startHour = 9;

    subjects.forEach((subject,index) => {

        let div =
        document.createElement("div");

        div.className = "timetable-card";

        let endHour =
        startHour + hoursData[index];

        div.innerText =
        `📚 ${startHour}:00 - ${endHour}:00 → ${subject}`;

        timetable.appendChild(div);

        startHour = endHour + 1;
    });
}


// POMODORO TIMER

let time = 25 * 60;

let timerInterval;

function startTimer(){

    clearInterval(timerInterval);

    timerInterval = setInterval(() => {

        let minutes =
        Math.floor(time / 60);

        let seconds =
        time % 60;

        seconds =
        seconds < 10 ? "0" + seconds : seconds;

        let timer =
        document.getElementById("timer");

        if(timer){

            timer.innerText =
            `${minutes}:${seconds}`;
        }

        if(time > 0){

            time--;

        }else{

            clearInterval(timerInterval);

            alert("Study Session Complete!");
        }

    },1000);
}

function resetTimer(){

    clearInterval(timerInterval);

    time = 25 * 60;

    let timer =
    document.getElementById("timer");

    if(timer){

        timer.innerText =
        "25:00";
    }
}


// PRODUCTIVITY CHART

let chart;

function updateChart(){

    let chartCanvas =
    document.getElementById("studyChart");

    if(!chartCanvas){

        return;
    }

    if(chart){

        chart.destroy();
    }

    chart = new Chart(chartCanvas, {

        type: 'bar',

        data: {

            labels: subjects,

            datasets: [{

                label: 'Study Hours',

                data: hoursData,

                borderWidth: 1
            }]
        },

        options: {

            responsive: true
        }
    });
}


// AI CHATBOT

async function sendMessage(){

    let userMessage =
    document.getElementById("userMessage")?.value;

    if(userMessage === ""){

        return;
    }

    let chatBox =
    document.getElementById("chatBox");

    if(!chatBox){
        return;
    }

    chatBox.innerHTML +=
    `<div class="user-chat">
        🧑 ${userMessage}
    </div>`;

    let response =
    await fetch('/chat', {

        method: 'POST',

        headers: {

            'Content-Type': 'application/json'
        },

        body: JSON.stringify({

            message: userMessage
        })
    });

    let data =
    await response.json();

    chatBox.innerHTML +=
    `<div class="bot-chat">
        🤖 ${data.reply}
    </div>`;

    document.getElementById("userMessage").value = "";

    chatBox.scrollTop =
    chatBox.scrollHeight;
}


// CURRENT AFFAIRS

async function loadNews(){

    let response =
    await fetch('/get_news');

    let news =
    await response.json();

    let newsContainer =
    document.getElementById("newsContainer");

    if(!newsContainer){
        return;
    }

    newsContainer.innerHTML = "";

    news.forEach(item => {

        let div =
        document.createElement("div");

        div.className = "news-card";

        div.innerText = item;

        newsContainer.appendChild(div);
    });
}


// REMINDER SYSTEM

function addReminder(){

    let reminderInput =
    document.getElementById("reminderInput");

    if(!reminderInput){
        return;
    }

    let reminderText =
    reminderInput.value;

    if(reminderText === ""){

        alert("Please enter reminder");

        return;
    }

    let reminderList =
    document.getElementById("reminderList");

    let div =
    document.createElement("div");

    div.className =
    "reminder-card";

    div.innerText =
    "🔔 " + reminderText;

    reminderList.appendChild(div);

    reminderInput.value = "";
}


// DARK MODE

function toggleDarkMode(){

    document.body.classList.toggle("dark-mode");
}

console.log("AI EDU MENTOR Loaded Successfully");
let timer;
let minutes = 25;
let seconds = 0;
let running = false;

function updateTimer(){

    let displayMinutes = String(minutes).padStart(2,'0');

    let displaySeconds = String(seconds).padStart(2,'0');

    document.getElementById("timer").innerText =
        `${displayMinutes}:${displaySeconds}`;

}

function startTimer(){

    if(running) return;

    running = true;

    timer = setInterval(() => {

        if(seconds === 0){

            if(minutes === 0){

                clearInterval(timer);

                alert("⏰ Focus Session Completed!");

                running = false;

                return;

            }

            minutes--;

            seconds = 59;

        }

        else{

            seconds--;

        }

        updateTimer();

    },1000);

}

function pauseTimer(){

    clearInterval(timer);

    running = false;

}

function resetTimer(){

    clearInterval(timer);

    running = false;

    minutes = 25;

    seconds = 0;

    updateTimer();

}