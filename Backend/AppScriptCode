// ================= GLOBAL CONFIG =================
const MAIN_SHEET_ID = "1cyYJGNyT8zTYBf3uYhPu8Guv-_8YPOq2qV1JLmsmFiI";
const FEES_SHEET_ID = "1cyYJGNyT8zTYBf3uYhPu8Guv-_8YPOq2qV1JLmsmFiI";
// 1NqdQGzfIIAK7z1tODoszG4zf4v6UyVmisprMBcaF09Y

const mainSS = SpreadsheetApp.openById(MAIN_SHEET_ID);
const feesSS = SpreadsheetApp.openById(FEES_SHEET_ID);

// ================= MAIN ROUTER =================
function doGet(e) {

  const action = e.parameter.action;

  // ---------- Complaints ----------
  if (action === "complaints") {
    const sheet = mainSS.getSheetByName("Complaints");
    const data = sheet.getDataRange().getValues();
    return jsonOutput(data);
  }

  // ---------- Attendance Search ----------
  if (action === "attendanceSearch") {
    const roll = e.parameter.roll;
    const sheet = mainSS.getSheetByName("Students");
    const data = sheet.getDataRange().getValues();

    for (let i = 1; i < data.length; i++) {
      if (data[i][0] == roll) {
        return jsonOutput({
          roll: data[i][0],
          name: data[i][1],
          room: data[i][2],
          course: data[i][3]
        });
      }
    }
    return textOutput("Student Not Found");
  }

  // ---------- Night Canteen Status ----------
  if (action === "canteenStatus") {
    const sheet = mainSS.getSheetByName("Night_Canteen_Status");
    const data = sheet.getDataRange().getValues();
    const lastRow = data[data.length - 1];

    return jsonOutput({
      date: lastRow[0],
      isOpen: lastRow[1],
      openingTime: lastRow[2],
      closingTime: lastRow[3]
    });
  }

  // ---------- Night Canteen Menu ----------
  if (action === "canteenMenu") {
    const sheet = mainSS.getSheetByName("Night_Canteen_Menu");
    const data = sheet.getDataRange().getValues();
    let menu = [];

    for (let i = 1; i < data.length; i++) {
      menu.push({
        id: data[i][0],
        name: data[i][1],
        price: data[i][2],
        available: data[i][3]
      });
    }

    return jsonOutput(menu);
  }

  // ---------- Fees ----------
  if (action === "getFees") {
    const roll = e.parameter.rollNumber;
    return jsonOutput(getFeesByRoll(roll));
  }

  //------------GET FINES --------
  if (action === "getFines") {
    const roll = e.parameter.rollNumber;
    const sheet = mainSS.getSheetByName("Fines");
    const rows = sheet.getDataRange().getValues();
    let result = [];

    for (let i = 1; i < rows.length; i++) {
      if (rows[i][0] == roll) {
        result.push({
          rollNumber: rows[i][0],
          name: rows[i][1],
          reason: rows[i][2],
          amount: rows[i][3],
          date: rows[i][4],
          status: rows[i][5]
        });
      }
    }

    return jsonOutput(result);
  }

  return textOutput("API Running");
}

// ================= POST ROUTER =================
function doPost(e) {

  const action = e.parameter.action;
  const data = JSON.parse(e.postData.contents);

  // ---------- Mark Attendance ----------
  if (action === "markAttendance") {
    const sheet = mainSS.getSheetByName("Attendance");

    sheet.appendRow([
      new Date(),
      data.name,
      data.roll,
      data.room,
      data.status
    ]);

    return jsonOutput({ message: "Attendance Marked" });
  }

  // ---------- Add or Update Fee ----------
  if (action === "updateFee") {
    const result = addOrUpdateFee(data);
    return jsonOutput({ message: result });
  }

  // ---------- Add Canteen Item ----------
  if (action === "addCanteenItem") {
    const sheet = mainSS.getSheetByName("Night_Canteen_Menu");
    const id = new Date().getTime();

    sheet.appendRow([id, data.itemName, data.price, data.available]);
    return jsonOutput({ message: "Item Added" });
  }

  // ---------- Update Canteen Status ----------
  if (action === "updateCanteenStatus") {
    const sheet = mainSS.getSheetByName("Night_Canteen_Status");
    sheet.appendRow([
      data.date,
      data.isOpen,
      data.openingTime,
      data.closingTime
    ]);
    return jsonOutput({ message: "Status Updated" });
  }

  // ---------- Add Fine ----------
  if (action === "addFine") {
    const sheet = mainSS.getSheetByName("Fines");

    sheet.appendRow([
      data.rollNumber,
      data.studentName,
      data.reason,
      data.amount,
      data.date,
      "Unpaid"
    ]);

    return jsonOutput({ message: "Fine Added Successfully" });
  }

  return textOutput("Invalid POST Request");
}

// ================= FEES FUNCTIONS =================
function getFeesSheet() {
  return feesSS.getSheetByName("Fees");
}

function addOrUpdateFee(data) {
  const sheet = getFeesSheet();
  const rows = sheet.getDataRange().getValues();

  const roll = data.rollNumber;
  const name = data.studentName;
  const feeType = data.feeType;
  const total = Number(data.totalAmount);
  const paid = Number(data.paidAmount);
  const dueDate = data.dueDate;

  const due = total - paid;

  let status = "Unpaid";
  if (paid === 0) status = "Unpaid";
  else if (paid < total) status = "Partial";
  else status = "Paid";

  for (let i = 1; i < rows.length; i++) {
    if (rows[i][0] == roll && rows[i][2] == feeType) {
      sheet.getRange(i + 1, 4, 1, 5)
        .setValues([[total, paid, due, dueDate, status]]);
      return "Fee Updated";
    }
  }

  sheet.appendRow([
    roll, name, feeType, total, paid, due, dueDate, status
  ]);

  return "Fee Added";
}

function getFeesByRoll(rollNumber) {
  const sheet = getFeesSheet();
  const rows = sheet.getDataRange().getValues();
  let result = [];

  for (let i = 1; i < rows.length; i++) {
    if (rows[i][0] == rollNumber) {
      result.push({
        feeType: rows[i][2],
        totalAmount: rows[i][3],
        paidAmount: rows[i][4],
        dueAmount: rows[i][5],
        status: rows[i][7]
      });
    }
  }
  return result;
}

// ================= HELPERS =================
function jsonOutput(data) {
  return ContentService
    .createTextOutput(JSON.stringify(data))
    .setMimeType(ContentService.MimeType.JSON);
}

function textOutput(msg) {
  return ContentService
    .createTextOutput(msg)
    .setMimeType(ContentService.MimeType.TEXT);
}
