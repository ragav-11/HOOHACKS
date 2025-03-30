console.log("Cyberbullying Detector content script running.");

// List of keywords/phrases to look for (this can be expanded)
const bullyingKeywords = [
  "bully", "stupid", "hate", "idiot", "ugly", "loser", "worthless", "dumb", "fat"
];

// Function to check if the text contains any bullying keywords
function checkForBullying(text) {
  return bullyingKeywords.some(keyword => text.toLowerCase().includes(keyword));
}

// Function to analyze the page and detect cyberbullying
function analyzePage() {
  // Extract all text content from the page
  let bodyText = document.body.innerText;

  // Check if the page contains any bullying language
  if (checkForBullying(bodyText)) {
    // Highlight the text or trigger an alert
    alert("Potential cyberbullying detected on this page!");
    
    // Optional: Highlight offending text
    const elements = document.querySelectorAll("p, span, div");  // You can customize this selector
    elements.forEach(element => {
      if (checkForBullying(element.innerText)) {
        element.style.backgroundColor = "red";  // Highlight the text with a red background
      }
    });
  }
}

// Run the analysis when the document is fully loaded
document.addEventListener("DOMContentLoaded", analyzePage);