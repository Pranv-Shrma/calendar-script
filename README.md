# Start up Calendar

## Project Description
This project is a **simple Python script** that automatically opens your calendar when you start your PC. The motivation behind this project is straightforward: **to ensure you never miss out on planning your day**. Starting your day with an overview of your schedule helps you stay organized and productive.
Also, I have recently started using reclaim.ai along with google calendar, so I have listed these 2 main sites. Feel free to change and add your own custom websites.

The script is converted into an executable file using **Auto Py to Exe** and is set to run at startup using **Windows Task Scheduler**.

---

## Table of Contents
- [Installation Instructions](#installation-instructions)
- [Usage](#usage)
- [Tech Stack](#tech-stack)
- [Contributing](#contributing)
- [How to Use Your Project](#how-to-use-your-project)
- [Credits](#credits)
- [Future Scope](#future-scope)
- [Contact Information](#contact-information)

---

## Installation Instructions
Follow these steps to set up the project:

1. **Clone the Repository**:
   ```
   git clone https://github.com/your-username/calendar-auto-opener.git
   cd calendar-auto-opener
   ```

2. **Install Python**:
   Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/).

3. **Install Required Libraries**:
   Install the necessary Python libraries by running:
   ```
   pip install -r requirements.txt
   ```

4. **Convert Python Script to Executable**:
   - Install **Auto Py to Exe**:
     ```
     pip install auto-py-to-exe
     ```
   - Run the following command to open the Auto Py to Exe GUI:
     ```
     auto-py-to-exe
     ```
   - Select the script (`calendar_opener.py`) and convert it to an `.exe` file.

5. **Set Up Windows Task Scheduler**:
   - Open **Task Scheduler** on your Windows system.
   - Create a new task and configure it to run the `.exe` file at system startup.
   - Save the task, and you're good to go!

---

## Usage
Once installed, the script will automatically open your calendar application every time you start your PC. This ensures you have an overview of your day right at the beginning.

---

## Tech Stack
- **Python**: Core programming language used for the script.
- **Auto Py to Exe**: Used to convert the Python script into an executable file.
- **Windows Task Scheduler**: Configured to run the executable at system startup.

---

## Contributing
Contributions are welcome! If you'd like to improve this project, follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```
   git commit -m "Add your message here"
   ```
4. Push to the branch:
   ```
   git push origin feature/your-feature-name
   ```
5. Open a pull request.

---

## How to Use Your Project
1. Clone the repository and follow the installation instructions.
2. Customize the script if needed (e.g., change the calendar application or add additional startup tasks).
3. Convert the script to an executable and set it up in Task Scheduler.
4. Restart your PC to test if the calendar opens automatically.

---

## Credits
- **Auto Py to Exe**: For simplifying the process of converting Python scripts to executables.
- **Windows Task Scheduler**: For enabling the script to run at startup.
- **Python Community**: For providing excellent resources and libraries.

---

## Future Scope
- Add support for **cross-platform startup** (e.g., macOS and Linux).
- Integrate with **Google Calendar API** to fetch and display events directly.
- Add a **notification system** to remind users of upcoming tasks.

---

## Contact Information
If you have any questions or suggestions, feel free to reach out:

- **Email**: pranvshrma13@gmail.com
- **GitHub**: [Pranv-Shrma](https://github.com/Pranv-Shrma)

---
