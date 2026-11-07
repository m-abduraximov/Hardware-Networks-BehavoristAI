# Part A – True / False

*Write True or False. If a statement is false, correct it.*

1. [2.1.1] A LAN usually covers a room, a building or a small campus.

2. [2.1.1] In a peer-to-peer network, devices share resources directly without a central server.

3. [2.1.3] A hub sends incoming data only to the port where the receiver is connected.

4. [2.2] The OSI model has seven layers, and the TCP/IP model has four layers.

5. [2.3.1] The World Wide Web and the Internet are the same thing.

6. [2.3.2] TCP starts a connection with three messages: SYN, SYN-ACK and ACK.

7. [2.3.3] 192.168.1.300 is a valid IPv4 address.

8. [2.3.3] DHCP gives devices IP addresses and other network settings automatically.

9. [2.3.5] Every router knows the complete path from the sender to the final destination.

10. [2.4.3] Authentication guarantees that data has not been changed during transmission.

# Part B – Multiple Choice

11. [2.1.1] Which of the following are typical connections for a PAN? *(Choose ALL correct answers.)*

    - A. Bluetooth
    - B. USB
    - C. Undersea cables
    - D. Fibre between cities

12. [2.1.3] Which device sends data only to the port of the receiving device, using MAC addresses? *(Choose ONE answer.)*

    - A. Hub
    - B. Switch
    - C. Modem
    - D. Access point

13. [2.2] In the TCP/IP model, which OSI layers are combined into the Application layer? *(Choose ONE answer.)*

    - A. Physical and Data Link
    - B. Network and Transport
    - C. Session, Presentation and Application
    - D. Transport and Session

14. [2.3.2] Which protocol gives reliable, ordered delivery and resends lost data? *(Choose ONE answer.)*

    - A. IP
    - B. UDP
    - C. TCP
    - D. ICMP

15. [2.3.2] Rover's report is sent with TCP as 5 numbered packets, and packet 3 is lost. What happens? *(Choose ONE answer.)*

    - A. The whole message is dropped
    - B. Only packet 3 is sent again
    - C. The phone ignores the missing word
    - D. A router rebuilds packet 3 itself

16. [2.3.3] Which of these are private IPv4 addresses? *(Choose ALL correct answers.)*

    - A. 10.0.0.5
    - B. 8.8.8.8
    - C. 172.20.4.1
    - D. 172.40.4.1

17. [2.3.4] In the address https://mail.google.com, which part is the subdomain? *(Choose ONE answer.)*

    - A. https
    - B. mail
    - C. google
    - D. .com

18. [2.3.4] What does DNS give your computer when you type a domain name? *(Choose ONE answer.)*

    - A. The web page itself
    - B. The IP address of the server
    - C. A new MAC address
    - D. A password

19. [2.3.5] A network has these links: Home–R1, Home–R2, R1–R3, R1–R4, R2–R4, R3–Server, R4–Server. Router R3 stops working. Which paths can still reach the server? *(Choose ALL correct answers.)*

    - A. Home → R1 → R3 → Server
    - B. Home → R2 → R4 → Server
    - C. Home → R3 → Server
    - D. Home → R1 → R4 → Server

20. [2.4.4] Someone changes Rover's report from "12 cm" to "2 cm" on the way. Which security property was broken? *(Choose ONE answer.)*

    - A. Privacy
    - B. Authentication
    - C. Integrity
    - D. Non-repudiation

# Part C – Open-ended

*Write a developed answer (normally more than 100 words), using examples, a diagram or worked steps.*

21. [2.3.2] Compare TCP and UDP. Then decide which protocol is better for (a) Rover's obstacle report and (b) a live video call. Justify both decisions.

22. [2.3] Explain step by step what happens from the moment you type https://www.example.com into a browser until the page appears on the screen. Use the terms DNS, IP address, TCP handshake, HTTPS, router and server.

23. [2.4] Rover sends its reports to a phone through home Wi-Fi. Write a simple security plan for this system. Explain how firewalls, privacy (encryption), authentication, integrity and non-repudiation each protect Rover's reports, and give one real risk for each idea.

---

# Answer Key

## Part A – True / False

**1. True.** A LAN is a local network, such as home Wi-Fi or a school computer lab.

**2. True.** In P2P all devices are equal; in client–server, central servers provide services.

**3. False.** A hub copies data to all ports. A switch is the device that sends data only to the correct port, using MAC addresses.

**4. True.** OSI: Physical to Application (7). TCP/IP: Link, Internet, Transport, Application (4).

**5. False.** The Internet is the whole infrastructure (cables, routers, servers, protocols). The Web is only one service that runs on it, using HTTP/HTTPS.

**6. True.** This is the TCP three-way handshake (Figure 2.6).

**7. False.** Each of the four numbers in an IPv4 address must be between 0 and 255, so 300 is not allowed.

**8. True.** DHCP also gives the subnet mask, default gateway and DNS server, using the DORA steps.

**9. False.** Each router only decides the next hop, using its routing table. The packet reaches the destination hop by hop.

**10. False.** Authentication checks who a user or device is. Protecting data from being changed is integrity.

## Part B – Multiple Choice

**11. A, B.** A PAN connects personal devices around one person, usually with Bluetooth or USB. Undersea cables and city-to-city fibre are used for WANs and GANs.

**12. B.** A switch (Layer 2) uses MAC addresses. A hub copies data to every port.

**13. C.** OSI layers 5, 6 and 7 together match the TCP/IP Application layer (Figure 2.5).

**14. C.** TCP is connection-oriented and reliable. UDP is fast but does not resend; IP addresses and moves packets; ICMP reports errors.

**15. B.** TCP uses the numbers to find the missing piece and asks for only that packet again (Quick check 5).

**16. A, C.** Private ranges are 10.x.x.x, 172.16–172.31.x.x and 192.168.x.x. 172.40.4.1 is outside 172.16–172.31, and 8.8.8.8 is public.

**17. B.** https is the protocol, mail is the subdomain, google is the second-level domain and .com is the TLD.

**18. B.** DNS works like a phone book: it translates the domain name into the server's IP address.

**19. B, D.** Any path through R3 is broken, and there is no direct Home–R3 link. Both paths through R4 still work, which shows why several paths make the network reliable.

**20. C.** Integrity means data is not changed on the way. Hashes and digital signatures help the receiver detect such changes.

## Part C – Open-ended

*Other well-reasoned answers are also acceptable.*

**21. Compare TCP and UDP**

- TCP: connection-oriented, three-way handshake (SYN, SYN-ACK, ACK), numbering, error checking, resending, correct order; slower because of overhead.
- UDP: connectionless, no handshake, no resending; fast and lightweight.
- (a) Rover's report: TCP, because every word matters – a missing "12" or "LEFT" would make the report wrong or dangerous.
- (b) Live video: UDP, because speed matters more than perfect delivery; a late frame is useless, so resending it would only add delay.
- Good answers mention reliability vs. speed as a trade-off.

**22. From typing a web address to seeing the page**

- Browser reads the domain parts (protocol, subdomain, second-level domain, TLD).
- Device asks a DNS server; DNS returns the IP address of the web server.
- TCP connection is opened with the three-way handshake (SYN, SYN-ACK, ACK).
- Browser sends an HTTPS request (encrypted) to the server, normally port 443.
- Data is split into packets; routers forward them hop by hop using IP addresses and routing tables.
- Web server processes the request and sends the page back in packets.
- Browser receives the packets, TCP puts them in order, and the page is shown.
- The device's own IP address may have been given earlier by DHCP.

**23. A security plan for Rover**

- Firewall: allow only the needed traffic (for example, Rover's address to the app's port 443) and block unknown ports from the Internet.
- Privacy: send reports over HTTPS/TLS so other people on the Wi-Fi cannot read them.
- Authentication: Rover and the phone prove their identity (certificate, token, password), so a fake device cannot pretend to be Rover.
- Integrity: hashes or digital signatures show if "12 cm" was changed to "2 cm".
- Non-repudiation: digital signatures and logs prove which device sent which report.
- Conclusion: one measure is not enough; combining them gives defence in depth.
