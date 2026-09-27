async function apiRequest(endpoint, data) {
    const response = await fetch(endpoint, {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    });

    const result = await response.json();

    if (!response.ok) {
        throw new Error(result.error || "Something went wrong.");
    }

    return result;
}

function showLoading(elementId) {
    const element = document.getElementById(elementId);
    element.className = "result-box loading";
    element.textContent = "EduGenie is thinking...";
}

function showResult(elementId, text) {
    const element = document.getElementById(elementId);
    element.className = "result-box";
    element.textContent = text;
}

function showError(elementId, error) {
    const element = document.getElementById(elementId);
    element.className = "result-box error";
    element.textContent = "Error: " + error.message;
}

async function askQuestion() {
    const question = document.getElementById("question").value.trim();

    if (!question) {
        alert("Please enter a question.");
        return;
    }

    showLoading("qna-result");

    try {
        const result = await apiRequest("/api/qna", { question });
        showResult("qna-result", result.answer);
    } catch (error) {
        showError("qna-result", error);
    }
}

async function explainTopic() {
    const topic = document.getElementById("topic").value.trim();
    const level = document.getElementById("level").value;

    if (!topic) {
        alert("Please enter a topic.");
        return;
    }

    showLoading("explain-result");

    try {
        const result = await apiRequest("/api/explain", { topic, level });
        showResult("explain-result", result.answer);
    } catch (error) {
        showError("explain-result", error);
    }
}

async function generateQuiz() {
    const topic = document.getElementById("quiz-topic").value.trim();
    const count = Number(document.getElementById("quiz-count").value);

    if (!topic) {
        alert("Please enter a quiz topic.");
        return;
    }

    showLoading("quiz-result");

    try {
        const result = await apiRequest("/api/quiz", { topic, count });
        showResult("quiz-result", result.answer);
    } catch (error) {
        showError("quiz-result", error);
    }
}

async function summarizeNotes() {
    const text = document.getElementById("notes").value.trim();

    if (!text) {
        alert("Please paste your notes.");
        return;
    }

    showLoading("summary-result");

    try {
        const result = await apiRequest("/api/summarize", { text });
        showResult("summary-result", result.answer);
    } catch (error) {
        showError("summary-result", error);
    }
}

async function createLearningPath() {
    const subject = document.getElementById("learning-subject").value.trim();
    const goal = document.getElementById("learning-goal").value.trim();
    const days = Number(document.getElementById("learning-days").value);

    if (!subject) {
        alert("Please enter a subject.");
        return;
    }

    showLoading("learning-result");

    try {
        const result = await apiRequest("/api/learning-path", {
            subject,
            level: "College",
            goal,
            days
        });

        showResult("learning-result", result.answer);
    } catch (error) {
        showError("learning-result", error);
    }
}
