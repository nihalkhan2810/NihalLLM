# ASL Hand Gesture Analysis Using CNN
Project Role: Team Lead
Windsor, ON, Canada
January 2024 - October 2024

This project focused on developing a real-time system for recognizing American Sign Language (ASL) hand gestures using computer vision. The goal was to create an accessible tool that could potentially assist with communication or educational purposes, particularly targeting deployment on low-cost, portable hardware like the Raspberry Pi.

-   **Trained a TensorFlow-based CNN on 5000+ ASL images, achieving 98% test accuracy with a <5ms inference time on Raspberry Pi hardware.**
    I led the effort to train a convolutional neural network using TensorFlow to classify over 5,000 images of various ASL hand gestures. We focused on achieving high accuracy, reaching 98% on the test set, indicating reliable gesture recognition. A primary technical challenge and goal was optimizing the model and the inference process to run efficiently on resource-constrained hardware like the Raspberry Pi. Through careful model selection and optimization techniques, we achieved an impressive inference time of less than 5 milliseconds per image on the target hardware, making real-time gesture recognition feasible.

-   **Reduced misclassification in low-light conditions by 15% using adaptive histogram equalization and synthetic data augmentation.**
    Recognizing hand gestures reliably in varying lighting conditions is a common challenge. We identified that low-light environments significantly increased misclassifications. To address this, we implemented preprocessing techniques like adaptive histogram equalization using OpenCV to improve image contrast and visibility specifically in darker conditions. Additionally, we generated synthetic training data by programmatically reducing the brightness of existing images and adding simulated noise. This combined approach of preprocessing and data augmentation targeted the specific failure mode of low-light conditions and resulted in a 15% reduction in misclassification errors in those scenarios, making the system more robust.

-   **Team Leadership:** As Team Lead for this project (a team of 4), I was responsible for defining project milestones, assigning tasks to team members based on their strengths, coordinating our development efforts, facilitating communication, and resolving technical blockers. This role allowed me to develop my skills in project management, mentoring, and ensuring timely progress towards our goals while fostering a collaborative environment.

This project was a great experience in leading a technical team, focusing on model optimization for edge deployment, and developing solutions for real-world accessibility challenges.