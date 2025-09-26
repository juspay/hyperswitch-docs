---
icon: sparkles
---

# Payment Features

HyperSwitch SDKs provide client-side payment capabilities across web and mobile platforms. Our frontend SDKs handle secure payment collection, user authentication, and seamless checkout experiences while maintaining PCI compliance.

### Core SDK Features

#### Payment Collection

* **Secure Card Input**: PCI-compliant form fields with real-time validation
* **Payment Method Selection**: Support for cards, wallets, and local payment methods
* **Tokenization**: Convert sensitive data to secure tokens on the client
* **Auto-formatting**: Smart card number, expiry, and CVV formatting

#### Authentication & Security

* **3D Secure 2.0**: Seamless authentication with challenge flows when needed
* **Biometric Authentication**: Touch ID, Face ID, and fingerprint support on mobile
* **Encryption**: End-to-end encryption for all sensitive data
* **Device Security**: Secure enclave and keystore utilization

#### User Experience

* **Card Scanning**: Camera-based card input (mobile only)
* **Saved Payment Methods**: Tokenized card storage and management
* **One-Click Payments**: Express checkout with saved methods
* **Auto-complete**: Browser and device autofill integration
* **Real-time Validation**: Instant feedback on form inputs

#### Platform-Specific Features

**Web SDK**

* Payment Request API integration
* Browser autofill support
* Apple Pay (with domain verification)
* Google Pay web integration

**Mobile SDKs (iOS/Android)**

* Native wallet integration (Apple Pay/Google Pay)
* NFC tap-to-pay support (Beta)
* Camera-based card scanning
* Biometric authentication
* Native UI components

**Cross-Platform (React Native/Flutter)**

* Platform-appropriate wallet integration
* Shared business logic with native UI
* Camera access for card scanning
* Cross-platform biometric support (Beta)
