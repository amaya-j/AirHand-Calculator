# Virtual Calculator

This project is a virtual calculator implemented using Python, OpenCV, and MediaPipe for hand tracking. It uses hand gestures to perform basic arithmetic operations.

## Features

- Hand tracking using MediaPipe.
- Virtual buttons for digits and basic arithmetic operations.
- Gesture-based input for interacting with the calculator.

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/virtual-calculator.git
    ```
2. Navigate to the project directory:
    ```sh
    cd virtual-calculator
    ```
3. Create and activate a virtual environment:
    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```
4. Install the required packages:
    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. Run the main script:
    ```sh
    python main.py
    ```
2. Use the webcam feed to interact with the virtual calculator using hand gestures.

## Hand Gestures

- **Tap on Buttons**: Use the tip of your index finger to tap on the virtual buttons.
- **Clear Input**: Bring the tip of your thumb and index finger close together.

## File Structure

- `main.py`: The main script to run the virtual calculator.
- `HandTrackingModule.py`: A module for hand tracking using MediaPipe.
- `requirements.txt`: A list of required packages.

## Dependencies

- Python 3.9+
- OpenCV
- MediaPipe
- cvzone

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## Acknowledgments

- [MediaPipe](https://mediapipe.dev/)
- [OpenCV](https://opencv.org/)
- [cvzone](https://github.com/cvzone/cvzone)
