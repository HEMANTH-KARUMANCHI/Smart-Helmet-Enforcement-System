# Smart Helmet Enforcement System

An IoT- and deep-learning-based prototype designed to encourage helmet use among two-wheeler riders. The system uses a camera and a YOLO-based computer vision model to detect whether a rider is wearing a helmet, then uses a Raspberry Pi to coordinate alerts and a motor-control demonstration.

## Overview

Helmet use is an important part of motorcycle safety, but riders may sometimes travel without one or remove it after starting the vehicle. The **Smart Helmet Enforcement System** explores a camera-based approach to identifying helmet use and connecting detection results to an IoT control system.

The project is developed in Python and uses a YOLO object-detection model trained on images of riders with and without helmets.

## Objectives

- Detect whether a rider is wearing a helmet.
- Encourage safer riding and helmet compliance.
- Demonstrate how computer vision and IoT hardware can work together.
- Explore automated alerts and vehicle-control behavior based on detection results.

## System Architecture

The project is organized into two main modules:

### 1. Helmet Detection Module

- Uses a Raspberry Pi camera to capture images or a live video feed of the rider.
- Uses a YOLO-based model to identify helmet use.
- The model is trained using images representing two categories: **with helmet** and **without helmet**.
- OpenCV and the Ultralytics toolkit are listed among the computer-vision tools used.

### 2. IoT Integration Module

A Raspberry Pi 4 Model B acts as the central controller. It receives the camera/model output and coordinates the connected indication and demonstration-control components.

Hardware described in the project includes:
- Raspberry Pi 4 Model B (8 GB)
- Raspberry Pi camera
- LCD screen (16×2)
- LEDs
- Buzzer
- Push button/switch
- DC motor (used to represent the bike engine in the prototype)
- SD card, connection cables, and external power supply

## How It Works

1. The Raspberry Pi camera captures the rider's image or video.
2. The YOLO model analyzes the camera input and determines whether a helmet is detected.
3. If a helmet is detected, the system allows the normal prototype flow to continue.
4. If a helmet is not detected, the system alerts the rider using the buzzer, LEDs, and LCD message.
5. The project description specifies a 30-second warning period. If the rider does not put on a helmet within that period, the prototype is designed to stop the motor/vehicle-control demonstration.



## Technology Stack

| Technology / Component | Purpose |
|---|---|
| Python | Main programming language |
| YOLO | Helmet object detection |
| Ultralytics | YOLO model tooling |
| OpenCV | Computer-vision and image-processing workflow |
| Pandas | Working with tabular/annotation data |
| NumPy | Image and array operations |
| Raspberry Pi OS | Operating system for the Raspberry Pi |
| Raspberry Pi Camera | Captures the rider's image/video input |
| Raspberry Pi 4 Model B | Central controller for the prototype |

## Requirements

### Hardware
- Raspberry Pi 4 Model B (8 GB)
- Raspberry Pi camera
- 16×2 LCD
- LEDs and buzzer
- Push button/switch
- DC motor for the demonstration
- SD card, connecting wires, and suitable power supply

### Software
- Python
- YOLO detection code/model
- OpenCV
- Ultralytics
- Pandas
- NumPy
- Raspberry Pi OS

The project document does not specify exact package versions, dataset download links, model-weight filenames, or a verified installation command sequence. Refer to the files in this repository for the implementation-specific setup.

## Project Modules

- **Helmet Detection:** Processes camera input and detects helmet presence.
- **IoT Integration:** Uses the detection result to coordinate alerts and the motor-control demonstration.

## Future Enhancements

The project document identifies the following possible extensions:

- **Driver drowsiness detection:** Add sensors and algorithms to analyze driver behavior and provide alerts.
- **Alcohol detection:** Add sensors to detect alcohol and discourage unsafe riding.
- **Night-vision enhancement:** Improve helmet detection in low-light conditions using night-vision camera technology.

## Project Documentation

The project documentation includes the system overview, requirements, project flow, technology stack, module descriptions, detailed design, UML diagrams, testing section, results/screens, conclusion, and future scope.

## Disclaimer

This project is intended for educational and demonstration purposes. Helmet detection may be affected by lighting, camera placement, occlusion, and model limitations. It is not a certified safety device and should not be relied on for real-world vehicle control or road-safety decisions.
