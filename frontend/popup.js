document.addEventListener("DOMContentLoaded", () => {
  setupTabs();
  loadLeaderboard();
  loadQuests();
});

function setupTabs() {
  const tabs = document.querySelectorAll(".nav-btn");
  const contents = document.querySelectorAll(".tab-content");

  tabs.forEach((tab) => {
    tab.addEventListener("click", () => {
      tabs.forEach((t) => t.classList.remove("active"));
      contents.forEach((c) => c.classList.remove("active"));

      tab.classList.add("active");
      const targetId = tab.getAttribute("data-tab");
      document.getElementById(targetId).classList.add("active");
    });
  });
}

function loadLeaderboard() {
  const container = document.getElementById("leaderboardList");
  const students = [
    { name: "Sarah J.", xp: "3,250", avatar: "👩‍🔬", rank: 1 },
    { name: "Mike R.", xp: "3,100", avatar: "👨‍🚀", rank: 2 },
    { name: "Jessica T.", xp: "2,950", avatar: "🦸‍♀️", rank: 3 },
    { name: "Alex Student", xp: "2,400", avatar: "🧙‍♂️", rank: 4 },
    { name: "David K.", xp: "2,200", avatar: "🥷", rank: 5 },
    { name: "Emily W.", xp: "2,050", avatar: "🧚‍♀️", rank: 6 },
  ];

  container.innerHTML = students
    .map(
      (student) => `
    <div class="rank-row ${student.rank <= 3 ? "top-3" : ""} ${student.rank === 4 ? "current-user-rank" : ""}">
      <div class="rank-num">${student.rank}</div>
      <div class="rank-avatar">${student.avatar}</div>
      <div class="rank-name">${student.name}</div>
      <div class="rank-xp">${student.xp} XP</div>
    </div>
  `,
    )
    .join("");
}

function loadQuests() {
  const container = document.getElementById("questList");
  const quests = [
    {
      title: "Perfect Attendance",
      progress: 5,
      total: 5,
      reward: "Badge",
      completed: true,
    },
    {
      title: "Submit Assignment Early",
      progress: 1,
      total: 3,
      reward: "300 XP",
      completed: false,
    },
    {
      title: "Help a Classmate",
      progress: 0,
      total: 1,
      reward: "150 XP",
      completed: false,
    },
    {
      title: "Score 90%+ on Quiz",
      progress: 2,
      total: 5,
      reward: "500 XP",
      completed: false,
    },
  ];

  container.innerHTML = quests
    .map(
      (quest) => `
    <div class="quest-item ${quest.completed ? "completed" : ""}">
      <div class="quest-header">
        <div class="quest-title">${quest.completed ? "✅ " : ""}${quest.title}</div>
        <div class="quest-reward">
          ${quest.reward === "Badge" ? "🏅" : "⚡️"} ${quest.reward}
        </div>
      </div>
      <div class="quest-progress-text" style="font-size: 10px; color: #94a3b8; margin-bottom: 4px;">
        ${quest.completed ? "Completed" : `${quest.progress} / ${quest.total}`}
      </div>
      <div class="quest-bar">
        <div class="quest-fill" style="width: ${(quest.progress / quest.total) * 100}%"></div>
      </div>
    </div>
  `,
    )
    .join("");
}
