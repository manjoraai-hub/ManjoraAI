// =========================
// STUDY PLANNER
// =========================

let totalTasks = 0;
let completedTasks = 0;

function updateProgress(){

    document.getElementById("total-tasks").innerText =
    totalTasks;

    document.getElementById("completed-tasks").innerText =
    completedTasks;

    let progress = 0;

    if(totalTasks > 0){

        progress =
        (completedTasks / totalTasks) * 100;
    }

    document.getElementById("progress-bar").style.width =
    progress + "%";

    document.getElementById("progress-bar").innerText =
    Math.round(progress) + "%";
}

function addTask(){

    let time =
    document.getElementById("time").value;

    let task =
    document.getElementById("task").value;

    if(time === "" || task === ""){

        alert("Please enter all fields");

        return;
    }

    totalTasks++;

    updateProgress();

    let taskList =
    document.getElementById("task-list");

    let div =
    document.createElement("div");

    div.className = "task";

    div.innerHTML = `

        <div>
            <input type="checkbox"
            onchange="completeTask(this)">

            <b>${time}</b> - ${task}
        </div>

        <button class="delete-btn"
        onclick="deleteTask(this)">
            Delete
        </button>
    `;

    taskList.appendChild(div);

    document.getElementById("time").value = "";
    document.getElementById("task").value = "";
}

function completeTask(checkbox){

    if(checkbox.checked){

        completedTasks++;

    }else{

        completedTasks--;
    }

    updateProgress();
}

function deleteTask(button){

    let parent = button.parentElement;

    let checkbox =
    parent.querySelector("input");

    if(checkbox.checked){

        completedTasks--;
    }

    totalTasks--;

    updateProgress();

    parent.remove();
}


// =========================
// JOB PREPARATION PLANS
// =========================

function openSoftware(){

    window.location.href = "/software";
}

function openUPSC(){

    window.location.href = "/upsc";
}

function openBanking(){

    window.location.href = "/banking";
}

function openGate(){

    window.location.href = "/gate";
}


// =========================
// POMODORO TIMER
// =========================

let timer;
let minutes = 25;
let seconds = 0;
let running = false;

function updateTimer(){

    let displayMinutes =
    String(minutes).padStart(2,'0');

    let displaySeconds =
    String(seconds).padStart(2,'0');

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

        }else{

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


// =========================
// DAILY MOTIVATION
// =========================

const quotes = [

"Success doesn't come from motivation alone. It comes from consistency.",

"Small progress every day adds up to big results.",

"Discipline is stronger than motivation.",

"Dream big. Start small. Act now.",

"Focus on progress, not perfection.",

"Winners are not people who never fail, but people who never quit.",

"Consistency creates confidence.",

"Push yourself because no one else will do it for you.",

"Study while others are sleeping.",

"Your future is created by what you do today."

];

function newQuote(){

    let random =
    Math.floor(Math.random() * quotes.length);

    document.getElementById("quote").innerText =
    quotes[random];
}


// =========================
// QUICK NOTES
// =========================

window.onload = function(){

    let savedNotes =
    localStorage.getItem("study_notes");

    if(savedNotes){

        document.getElementById("notes").value =
        savedNotes;
    }

    let streak =
    localStorage.getItem("study_streak");

    if(streak === null){

        streak = 0;
    }

    document.getElementById("streak-count").innerText =
    streak + " Days";
}

function saveNotes(){

    let notes =
    document.getElementById("notes").value;

    localStorage.setItem(
        "study_notes",
        notes
    );

    alert("✅ Notes Saved Successfully");
}


// =========================
// GOAL TRACKER
// =========================

function addGoal(){

    let goalInput =
    document.getElementById("goal-input");

    let goal =
    goalInput.value;

    if(goal === ""){

        alert("Please enter a goal");

        return;
    }

    let goalList =
    document.getElementById("goal-list");

    let div =
    document.createElement("div");

    div.className = "task";

    div.innerHTML = `

        <div>
            🎯 ${goal}
        </div>

        <button class="delete-btn"
        onclick="this.parentElement.remove()">
            Remove
        </button>
    `;

    goalList.appendChild(div);

    goalInput.value = "";
}


// =========================
// STUDY STREAK
// =========================

function increaseStreak(){

    let streak =
    localStorage.getItem("study_streak");

    if(streak === null){

        streak = 0;
    }

    streak++;

    localStorage.setItem(
        "study_streak",
        streak
    );

    document.getElementById("streak-count").innerText =
    streak + " Days";
}

function resetStreak(){

    localStorage.setItem(
        "study_streak",
        0
    );

    document.getElementById("streak-count").innerText =
    "0 Days";
}

console.log("🚀 Manjora AI Loaded Successfully");