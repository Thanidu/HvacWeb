# Absorption Chiller Plant Calculator

A Flask-based web application that predicts the performance of an absorption chiller plant using a machine learning model. The app allows users to input parameters such as generator duty, pump pressure, mass flow rate, and chiller input temperature to calculate outputs like chiller output temperature, evaporator duty, generator output, and coefficient of performance (COP).

## Features
- Interactive web interface for inputting chiller parameters.
- Displays constant parameters (e.g., absorber temperature, mass fractions).
- Predicts chiller performance using a pre-trained machine learning model (`hvac.pickle`).
- Responsive design with a clean, user-friendly layout.

## Project Structure
```
HvacWeb/
├── app.py                    # Flask application with prediction logic
├── requirements.txt          # Python dependencies
├── .gitignore                # Excludes venv, hvac.pickle, and other files
├── static/
│   ├── scripts.js            # JavaScript for form submission and API calls
│   ├── styles.css            # CSS for styling the web interface
├── templates/
│   ├── index.html            # HTML template for the web interface
```

## Prerequisites
- Python 3.6 or higher
- Git
- A copy of the `hvac.pickle` model file (not included in the repository)

## Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Thanidu/HvacWeb.git
   cd HvacWeb
   ```

2. **Create and Activate a Virtual Environment**:
   - On Windows:
     ```bash
     python -m venv venv
     venv\Scripts\activate
     ```
   - On Linux/macOS:
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Obtain the Model File**:
   - Download the `hvac.pickle` file from [https://drive.google.com/file/d/11yWUrH9RM-HS91NcSrHdlZsizOxqxsyL/view?usp=sharing].
   - Place it in the project root (`HvacWeb/`).

5. **Run the Application**:
   ```bash
   python app.py
   ```
   - Open a browser and navigate to `http://127.0.0.1:5000`.

## Usage
- **Input Parameters**: Enter values for Generator Duty (kW), Pump Pressure (kPa), Mass Flow Rate (kg/hr), and Chiller Input Temperature (°C) in the form.
- **View Results**: After submitting, the app displays the predicted Chiller Output Temperature (°C), Duty of Evaporator (kW), Generator Output (°C), and COP.
- **Constant Parameters**: Reference the left panel for fixed parameters like absorber temperature and mass fractions.

## Dependencies
Listed in `requirements.txt`:
- Flask: Web framework
- NumPy: Numerical computations
- scikit-learn: Machine learning model support

## Deployment
To deploy the app to a cloud platform:
- **Heroku**:
  1. Create a `Procfile` with:
     ```
     web: gunicorn --bind 0.0.0.0:$PORT app:app
     ```
  2. Install `gunicorn`:
     ```bash
     pip install gunicorn
     pip freeze > requirements.txt
     ```
  3. Follow Heroku's deployment guide to connect the GitHub repository.
- **Render or Koyeb**: Use GitHub integration for deployment, ensuring `hvac.pickle` is included or downloaded during setup.

## Notes
- The `hvac.pickle` file is excluded from the repository due to its size. Contact the repository owner for access or provide your own trained model.
- Ensure the virtual environment is activated before running `pip` or `python` commands.
- For development, run `python app.py` with `debug=True`. For production, use a WSGI server like Gunicorn.

## License


## Contact
For issues or questions, open a GitHub issue or contact (Email: thaniduthennakoon@gmail.com).
