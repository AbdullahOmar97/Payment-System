# Integrated Payment System

This project demonstrates an integrated payment system that can handle various payment methods such as credit cards, PayPal, and cryptocurrencies using the Strategy Pattern. The Strategy Pattern allows for easy switching between payment methods without modifying the core payment system.

## Introduction

The integrated payment system is designed to support multiple payment methods seamlessly. By utilizing the Strategy Pattern, we can define a family of algorithms (payment methods), encapsulate each one, and make them interchangeable. This approach promotes flexibility and maintainability.

## Design

The system consists of the following components:

- **PaymentStrategy**: An abstract base class that defines the `pay` method.
- **Concrete Strategies**: Implementations of different payment methods, including credit card, PayPal, and cryptocurrency payments.
- **PaymentContext**: A class that uses a payment strategy to process payments and allows switching between strategies at runtime.
