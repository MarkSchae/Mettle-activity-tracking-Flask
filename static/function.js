// Request permission to show notifications
Notification.requestPermission();

// Set a variable to keep track of the current timeout
let currentTimeout;

// Add a click event listener to the button to set the interval time
document.getElementById("button").addEventListener("click", function() {
  let intervalInput = document.getElementById("timer");
  let intervalTime = intervalInput.value;

  // Clear the current timeout, if it exists
  if (currentTimeout) {
    clearTimeout(currentTimeout);
  }

  // Define a function to display the notification and set a new timeout
  function displayNotification() {
    // Check if the browser supports notifications
    if (Notification.permission === "granted") {
      // Display the notification with a link to the input page
      let notification = new Notification("Hello", {
        body: "Click here to input your activity",
        data: {
          url: "https://markschae-code50-116097277-qjwpvx54vrj26g9x-5000.preview.app.github.dev"
        },
        requireInteraction: true // Set requireInteraction to true
      });

      // Add an event listener for when the notification is clicked
      notification.addEventListener("click", function() {
        // Redirect to the specified URL
        window.focus();
        window.location.href = notification.data.url + "/input";
        notification.close(); // Close the notification after the user clicks on it
      });
    }
  }

  // Set a timeout to display the initial notification after the interval time has elapsed
  currentTimeout = setTimeout(displayNotification, intervalTime * 60 * 1000);
});


    const yearDropdown = document.getElementById("year");
    const monthDropdown = document.getElementById("month");
    const dayDropdown = document.getElementById("day");
    const tableRows = document.querySelectorAll("#query_result tbody tr");

    function filterTableRows() {
        const selectedYear = yearDropdown.value;
        const selectedMonth = monthDropdown.value;
        const selectedDay = dayDropdown.value;

        tableRows.forEach(row => {
            const yearCell = row.querySelector("td:nth-child(4)");
            const monthCell = row.querySelector("td:nth-child(5)");
            const dayCell = row.querySelector("td:nth-child(6)");

            if (selectedYear === "Year" || yearCell.textContent === selectedYear) {
                if (selectedMonth === "Month" || monthCell.textContent === selectedMonth) {
                    if (selectedDay === "Day" || dayCell.textContent === selectedDay) {
                        row.style.display = "";
                    } else {
                        row.style.display = "none";
                    }
                } else {
                    row.style.display = "none";
                }
            } else {
                row.style.display = "none";
            }
        });
    }

    yearDropdown.addEventListener("change", filterTableRows);
    monthDropdown.addEventListener("change", filterTableRows);
    dayDropdown.addEventListener("change", filterTableRows);


        // Get the select inputs and the table
    const yearSelect = document.getElementById("year");
    const monthSelect = document.getElementById("month");
    const daySelect = document.getElementById("day");
    const table = document.getElementById("query_result");

    // Add event listeners to the select inputs
    yearSelect.addEventListener("change", updateTableVisibility);
    monthSelect.addEventListener("change", updateTableVisibility);
    daySelect.addEventListener("change", updateTableVisibility);

    // Function to update the visibility of the table based on the select inputs
    function updateTableVisibility() {
      // Check if all the select inputs have their default option selected
      if (
        yearSelect.value === "Year" &&
        monthSelect.value === "Month" &&
        daySelect.value === "Day"
      ) {
        // Hide the table
        table.style.display = "none";
      } else {
        // Show the table
        table.style.display = "table";
      }
    }
