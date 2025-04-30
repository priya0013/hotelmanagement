🏨 Hotel Management System
A terminal-based Hotel Management System built in Python, designed to simplify hotel operations such as room booking, customer registration, billing, and room status tracking. Ideal for small-scale hotels or as an educational project to understand file handling, OOP, and basic UI interaction via the console.

🚀 Features
👤 User Authentication
Secure login system

Role-based access (admin/librarian concept can be added)

🛏️ Room Management
Add/view room details

Track available vs booked rooms

Update room status

🙍 Customer Management
Register and store customer information

Assign rooms to customers

View customer records

💸 Billing System
Generate bills for customers

Calculate total stay cost

Print and save invoice details

📋 Reports
Room availability report

Current checked-in customer list

Basic hotel statistics

🛠️ Tech Stack
Backend: Python 3

Storage: File handling (no database)

Interface: Command-line (CLI)

Modules Used: os, datetime, custom classes

💾 Project Structure
bash
Copy
Edit
hotelmanagement/
│
├── hotel.py          # Main driver script
├── login.py          # Handles login authentication
├── customer.py       # Customer operations
├── room.py           # Room operations
├── details.py        # Hotel details and info
├── images/           # Placeholder for future UI assets
└── __pycache__/      # Compiled Python files
🔧 Setup Instructions
📥 Clone the Repository
bash
Copy
Edit
git clone https://github.com/priya0013/hotelmanagement.git
cd hotelmanagement
▶️ Run the Application
bash
Copy
Edit
python hotel.py
Make sure you have Python 3.x installed on your system.

📝 Future Enhancements
💾 Transition to database (e.g., SQLite or MySQL)

🌐 Add a web interface using Flask/Django

📊 Export reports as PDF/CSV

🔐 Role-based access system with multiple user types

📱 Mobile-friendly GUI

🤝 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to contribute or change.

📄 License
This project is open-source and available under the MIT License.

