# Minor-Project-2nd-sem
-----

# 🏨 Hostel-ez: Digital Hostel Management System

**Hostel-ez** is a modern, responsive web application designed to bridge the gap between hostel administration and students. By replacing antiquated paper registers with a digital "Glassmorphism" UI, we ensure transparency in attendance, grievance redressal, and canteen management.

-----

## 🛠 Tech Stack & Requirements

To contribute to or run this project, you should be familiar with:

  * **Frontend:** Semantic HTML5, CSS3 (Flexbox/Grid), and Vanilla JavaScript (ES6+).
  * **Backend & Database:** \* **Google Apps Script (GAS):** Used as the middleware to handle API requests.
      * **Google Sheets API:** Used as a "NoSQL" style database for storing student records and complaints.
  * **Tools:** VS Code, Git/GitHub, and a Google Cloud Console account (for Sheets API integration).

-----

## 🚀 Key Modules

### 1\. Student Dashboard

  * **Real-time Stats:** View attendance percentage and room details.
  * **Digital Complaint Form:** Categorized submission (Electrical, Plumbing, etc.) with instant logging.
  * **Canteen Portal:** View daily menus and place orders digitally.

### 2\. Admin Interface (Warden/Staff)

  * **Attendance Manager:** Batch update student presence/absence.
  * **Complaint Resolver:** Track pending vs. resolved tickets with a status-toggle system.
  * **Database Management:** Direct sync with Google Sheets for easy export/auditing.

-----

## 🏗 System Architecture (For Developers)

The project uses a **Serverless Architecture**. Instead of maintaining a heavy Node.js/Python server, we leverage Google’s infrastructure:

1.  **Frontend** sends a `POST/GET` request via `fetch()` in JavaScript.
2.  **Google Apps Script** receives the JSON payload.
3.  **Spreadsheet Service** appends or retrieves rows from the designated Google Sheet.
4.  **Response** is sent back to the UI to update the DOM dynamically.

-----

## 📂 Project Structure

```text
├── assets/             # Images, Logos, and Icons
├── css/                # Component-based stylesheets (canteen.css, contact.css, etc.)
├── js/                 # Logic for API calls and DOM manipulation
├── backend/            # Google Apps Script (.gs) source code
├── dashboard.html      # Main Student Entry point
└── README.md
```

-----

👥 The Team & Contributions
- Project Leads & Integration: Raiyan Mirza, Dhananjai Avva

System architecture and overall project synchronization.

- Frontend & UI/UX Design: Abhinav Bajpai, Dhananjai Avva

Crafting the "Hostel-ez" glassmorphism theme and responsive layouts.

- Backend & Cloud Database: Gargi Verma, Prachi Yadav, Khushi Sharma, Raiyan Mirza

Google Apps Script development and Google Sheets API integration.

Faculty Mentor: Dr. Shahid Wani
-----

1.  **Badges:** It immediately shows the languages used, which coders look for first.
2.  **Tech Stack Detail:** It explains *how* you are using Google Sheets as a database, which is a clever "low-code" solution developers will appreciate.
3.  **Setup Guide:** It tells other developers exactly how to mirror your environment.
4.  **Architecture Section:** It shows that you understand the flow of data between the UI and the backend.
