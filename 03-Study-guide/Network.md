# Chapter 2

# Networks

*How devices talk to each other*

---

## Chapter route

**Chapter 2. Networks**

- Before you start
- 2.1. Network fundamentals
  - 2.1.1. Types of networks
  - 2.1.2. Networking medium
  - 2.1.3. Networking devices
- 2.2. Network architecture
- 2.3. Internet infrastructure
  - 2.3.1. What is the Internet?
  - 2.3.2. Core protocols
  - 2.3.3. Internet addressing
  - 2.3.4. Domains
  - 2.3.5. Routing
  - 2.3.6. Servers
- 2.4. Security
  - 2.4.1. Firewalls
  - 2.4.2. Privacy
  - 2.4.3. Authentication
  - 2.4.4. Integrity
  - 2.4.5. Non-repudiation
- 2.5. Why networking matters
- Mission complete: Rover's message
- Chapter summary
- Glossary
- Quiz

---

## Before you start

### What you will learn

- What a network is, and the main types of networks.
- How data travels through cables, glass fibre and the air.
- What switches, routers, access points and modems do.
- How the OSI and TCP/IP models split communication into layers.
- How the Internet works: protocols, IP addresses, domains, routing and servers.
- The five basic ideas of network security.

### What you need to know already

Nothing special. You only need to know that computers, phones and robots are electronic devices. Every new word is explained before it is used, and the glossary at the end repeats the key terms.

### How to use this chapter

| Step | What to do | Why |
| --- | --- | --- |
| 1. Read | Read one short section. | Learn one idea at a time. |
| 2. Look | Study the picture next to it. | Pictures make invisible processes visible. |
| 3. Check | Answer the Quick check without looking back. | Use the idea instead of only reading it. |
| 4. Compare | Compare your answer with the Answer line. | Find what you still need to review. |

> **✏ Mission question – make a prediction**
>
> You send a message from your phone to a friend in another city, and it arrives in one second. **How does it find the right phone?** Write your guess in two or three sentences. Keep it: you will check it at the end of the chapter.

---

## 2.1. Network Fundamentals

A **network** is two or more devices connected so that they can exchange information and share resources, such as an Internet connection, files or a printer. Without a network, every device is alone, like an island.

> **🤖 Rover says...**
>
> Right now I am an island. I can see the wall, but nobody knows about it!

### 2.1.1. Types of networks

#### A. By size (geographical coverage)

| Type | Size | Example | Typical connection |
| --- | --- | --- | --- |
| **PAN** – Personal Area Network | A few metres around one person | Phone + wireless earbuds or smartwatch | Bluetooth, USB |
| **LAN** – Local Area Network | A room, building or small campus | Home Wi-Fi, a school computer lab | Ethernet, Wi-Fi |
| **MAN** – Metropolitan Area Network | A city | Several university buildings in one city | Fibre |
| **WAN** – Wide Area Network | A country or continent | A bank connecting branches in many cities | Fibre, leased lines |
| **GAN** – Global Area Network | The whole world | A global company network; the Internet is the largest example | Undersea cables, satellites |

#### B. By ownership

- **Private network** – owned and used by one person or organisation, with limited access (a company LAN).
- **Public network** – open to many users (public Wi-Fi in a café, a mobile network).

#### C. By role

- **Client–server** – central servers provide services to many clients. Organised and easier to secure.
- **Peer-to-peer (P2P)** – devices share directly with each other, without a central server. Simple and cheap, but harder to control.

#### D. By transmission

- **Wired** – cables. Usually faster and more stable, but devices cannot move freely.
- **Wireless** – radio waves. Flexible and mobile, but walls and other devices can disturb the signal.

> **✔ Quick check 1 – Network types**
>
> Which type is each one? (a) earbuds connected to your phone; (b) the Wi-Fi in your dormitory; (c) a network linking all libraries of one city; (d) a company linking offices in Beijing and Tashkent; (e) Rover on your home Wi-Fi.
>
> **Answer:** (a) PAN, (b) LAN, (c) MAN, (d) WAN, (e) LAN. The main difference between types is the area they cover.

### 2.1.2. Networking media

A **transmission medium** is the path that carries the signal from one device to another.

#### A. Guided media (wired)

- **Twisted-pair cable** – pairs of copper wires twisted together to reduce noise. The usual Ethernet cable in homes and offices.
- **Coaxial cable** – one central copper wire with insulation and a shield around it. Used for cable TV and some Internet connections.
- **Fibre-optic cable** – thin glass or plastic threads that carry pulses of light. Very fast and good for long distances.

#### B. Unguided media (wireless)

- **Radio waves** – Wi-Fi, Bluetooth and mobile networks.
- **Microwaves** – high-frequency radio waves for point-to-point and satellite links.
- **Infrared** – very short range and needs a clear line of sight, like a TV remote.
- **Satellite** – signals sent through satellites for places far from cables.

> **✔ Quick check 2 – Networking media**
>
> Which medium fits best? (a) a desktop PC next to the router; (b) Rover, which moves around the room; (c) a link between two cities 300 km apart; (d) a TV remote control.
>
> **Answer:** (a) twisted-pair Ethernet – stable and cheap; (b) Wi-Fi radio – Rover must move; (c) fibre optic – fast over long distances; (d) infrared – short range, line of sight.

### 2.1.3. Networking devices

#### A. End devices

End devices are the devices people use: PCs, laptops, smartphones, smart TVs, network printers – and Rover.

#### B. Interconnection devices

| Device | Layer (OSI) | What it does |
| --- | --- | --- |
| **Hub** | Layer 1 – Physical | Connects devices and copies incoming data to **all** ports. Simple, no intelligence; rarely used today. |
| **Switch** | Layer 2 – Data Link | Connects devices in one LAN and sends data **only** to the right port, using MAC addresses. |
| **Router** | Layer 3 – Network | Connects **different** networks (your home and the Internet) and forwards packets using IP addresses. |
| **Access point (AP)** | Layer 2 | Lets wireless devices join the wired network through Wi-Fi. |
| **Modem** | Layer 1 | Converts signals between your network and the provider's line (phone, cable or fibre). |

> **✔ Quick check 3 – Networking devices**
>
> Name the device: (a) "I send data only to the port where the receiver is." (b) "I connect your home network to the Internet." (c) "I copy everything to every port." (d) "I let phones join without a cable." (e) "I convert signals for the provider's line."
>
> **Answer:** (a) switch, (b) router, (c) hub, (d) access point, (e) modem. Rover's Wi-Fi message first reaches the access point.

---

## 2.2. Network Architecture

**Network architecture** describes how a network is organised: who asks, who answers, and how the work of sending data is divided.

### Layers: dividing a big job into small jobs

Sending a message is a big job: create the message, cut it into pieces, add addresses, and send signals through a cable or the air. Engineers divide this work into **layers**. Each layer does one job and passes the result to the next layer. It is like posting a parcel: you pack it, the post office labels it, trucks move it, and the receiver unpacks it.

### The OSI model (7 layers)

The **OSI model** (Open Systems Interconnection) is a conceptual model with seven layers. It is mainly used for learning and for describing where a problem happens.

| Layer | Job |
| --- | --- |
| 7. Application | Services for programs and users (web, email). |
| 6. Presentation | Formats data: encoding, compression, encryption. |
| 5. Session | Starts, keeps and ends a conversation (session). |
| 4. Transport | Delivers data between programs; splits it into segments; checks errors. |
| 3. Network | Logical (IP) addressing and routing between networks. |
| 2. Data Link | Delivery inside one local network using MAC addresses. |
| 1. Physical | Sends raw bits (0 and 1) as electricity, light or radio. |

### The TCP/IP model (4 layers)

The Internet really works with the simpler **TCP/IP model**. Its four layers combine some OSI layers, as the picture shows.

> **🧠 Memory trick for OSI (from 1 to 7)**
>
> **P**lease **D**o **N**ot **T**hrow **S**ausage **P**izza **A**way = Physical, Data Link, Network, Transport, Session, Presentation, Application.

> **✔ Quick check 4 – Layers**
>
> Put each item on its TCP/IP layer: HTTP, Wi-Fi, TCP, IP, DNS, UDP, Ethernet cable, ICMP.
>
> Why is it useful that Wi-Fi and HTTP are on different layers?
>
> **Answer:** Application – HTTP, DNS; Transport – TCP, UDP; Internet – IP, ICMP; Link – Wi-Fi, Ethernet cable. Separate layers let you change the connection (cable → Wi-Fi) without changing the web page or HTTP.

---

## 2.3. Internet Infrastructure

### 2.3.1. What is the Internet?

The **Internet** is a global **network of networks**. Millions of private, public, university, business and government networks are connected so that their devices can communicate. It is not one big computer – it is routers, servers, cables, satellites and shared rules (protocols) working together.

| Element | Role |
| --- | --- |
| Clients | Phones, laptops and PCs that ask for services. |
| Servers | Computers that store and provide websites, files, email and apps. |
| Protocols | Shared rules: TCP/IP, DNS, HTTP/HTTPS, email protocols (SMTP, IMAP, POP3). |
| Routers | Move packets from one network to the next, like a postal system. |
| IP addresses | Numbers that identify devices so data can find them. |
| Physical infrastructure | Fibre and undersea cables, satellites, mobile towers, data centres. |

#### Internet vs. World Wide Web

- **Internet** = the whole infrastructure (cables, routers, servers, protocols) – like the roads.
- **World Wide Web (WWW)** = one service on the Internet that delivers web pages through HTTP/HTTPS – like the shops along the roads.
- Other Internet services: email, video calls, online games, cloud storage – and Rover's reports.

> **✔ Quick check**
>
> Is a WhatsApp or WeChat voice call part of the Web?
>
> **Answer:** No. It uses the Internet, but it is not a web page delivered through a browser.

### 2.3.2. Core protocols

A **protocol** is a set of rules that both sides agree on, so devices made by different companies can understand each other.

| Protocol | Layer (TCP/IP) | Main job |
| --- | --- | --- |
| **IP** – Internet Protocol | Internet | Gives logical addresses and moves packets from the sender to the receiver across networks. Versions: IPv4 (32-bit) and IPv6 (128-bit). |
| **TCP** – Transmission Control Protocol | Transport | Connection-oriented and reliable: starts with a handshake, numbers the data, checks errors, resends lost pieces and puts them back in order. |
| **UDP** – User Datagram Protocol | Transport | Connectionless and fast: no handshake and no resending. Good when speed matters more than every piece (live video, games). |
| **ICMP** – Internet Control Message Protocol | Internet | Reports errors and status (for example, "destination unreachable"). The ping tool uses ICMP messages. |
| **ARP** – Address Resolution Protocol | Between Link and Internet | Finds the MAC address of a device on the same LAN when only its IP address is known. |

#### TCP's three-way handshake

Before TCP sends data, the two devices agree to talk. It works like the start of a phone call:

SYN → SYN-ACK → ACK

#### Packets

A long message is not sent in one piece. It is cut into small **packets**. Each packet has a **header** (sender address, receiver address, number) and a piece of the data. Packets can take different paths, and if one is lost, only that one is sent again. (More precisely, TCP calls its pieces "segments", and IP carries them in packets.)

> **✔ Quick check 5 – Protocols and packets**
>
> (a) Rover's report is split into 5 numbered packets, and packet 3 is lost. Which protocol notices and asks for it again: TCP or UDP?
>
> (b) Which protocol is better for a live video call where speed matters most?
>
> (c) What are the three messages of the TCP handshake?
>
> **Answer:** (a) TCP – it numbers the data and resends missing pieces. (b) UDP – fast, no resending. (c) SYN → SYN-ACK → ACK.

### 2.3.3. Internet addressing

An **IP address** is a number that identifies a device on a network, like a home address for your device. It has two jobs: **identification** (who is sending or receiving) and **location** (helping routers know where to forward packets).

| Version | Example | Key point |
| --- | --- | --- |
| IPv4 | 192.168.1.20 | Four numbers from 0 to 255, separated by dots (32 bits). About 4.3 billion addresses – not enough today. |
| IPv6 | 2001:db8::20 | 128 bits, written in hexadecimal. A huge number of addresses. |

#### Private and public addresses

Some IPv4 ranges are reserved for **private** networks such as homes and schools: **10.x.x.x**, **172.16.x.x – 172.31.x.x** and **192.168.x.x**. These addresses work only inside the local network, so millions of homes can use the same ones. A **public** address is used on the Internet.

#### Static and dynamic addresses

- **Static IP** – set by hand and does not change. Good for servers and printers.
- **Dynamic IP** – given automatically by a **DHCP** server and may change over time. Normal for phones and laptops.

#### DHCP – Dynamic Host Configuration Protocol

DHCP automatically gives a device an IP address and other settings (subnet mask, default gateway, DNS server). This avoids mistakes such as two devices using the same address. The process has four steps, called **DORA**: Discover, Offer, Request, Acknowledge.

> **✔ Quick check 6 – IP addresses**
>
> Write private, public or invalid: (a) 192.168.1.20; (b) 10.0.0.5; (c) 8.8.8.8; (d) 192.168.1.300; (e) 172.20.4.1; (f) 172.40.4.1.
>
> What do the letters DORA mean in DHCP?
>
> **Answer:** (a) private, (b) private, (c) public, (d) invalid – 300 is greater than 255, (e) private – inside 172.16–172.31, (f) public – outside that range. DORA = Discover, Offer, Request, Acknowledge.

### 2.3.4. Domains

A **domain name** is a human-friendly name for a website or other Internet resource, such as example.com. People remember names more easily than numbers.

- **Top-level domain (TLD)** – the last part: .com, .org, .net, .cn, .uz.
- **Second-level domain** – the name chosen by the owner: "example" in example.com.
- **Subdomain** – an optional part in front: www.example.com or mail.example.com. "www" is a subdomain that traditionally marks a website.

#### DNS – Domain Name System

**DNS** works like a phone book: it translates a domain name into the IP address that computers need. When you type a name, your device asks a DNS server, receives the IP address, and then contacts the web server.

> **✔ Quick check 7 – Domains and DNS**
>
> Split https://mail.google.com into protocol, subdomain, second-level domain and TLD.
>
> What does DNS give your computer?
>
> **Answer:** https / mail / google / .com. DNS gives back the IP address of the server.

### 2.3.5. Routing

**Routing** is choosing the path that packets take from the sender to the receiver across networks. Each router reads the destination IP address, checks its **routing table** (a list of possible paths) and sends the packet to the **next hop** – the next router. This repeats, hop by hop, until the packet arrives.

- **Static routing** – paths are set by hand by an administrator. Simple, but it does not adapt when the network changes.
- **Dynamic routing** – routers share information and update paths automatically, using protocols such as **RIP** (counts hops), **OSPF** (compares cost or speed) and **BGP** (connects large networks on the Internet).

Good routing gives **speed** (a good path), **reliability** (another path if one fails) and **scalability** (billions of devices).

> **✔ Quick check 8 – Routing**
>
> Look at Figure 2.9. (a) How many hops are on the red path from the home router to the server? (b) Router R3 breaks – write a new path.
>
> What is the difference between static and dynamic routing?
>
> **Answer:** (a) 3 hops: Home → R1 → R3 → Server. (b) Home → R2 → R4 → Server (or Home → R1 → R4 → Server). Static routes are set by hand; dynamic routes are updated automatically by routers.

### 2.3.6. Servers

A **server** is a computer (often more powerful than a normal PC and running all the time) that provides services or data to other computers, called **clients**. "Client" and "server" are roles: even Rover's phone app acts as a server when it receives Rover's reports.

| Server type | What it does | Example |
| --- | --- | --- |
| Web server | Sends web pages (HTTP port 80, HTTPS port 443). | Nginx, Apache |
| Application server | Runs the program logic behind an app. | Node.js, Tomcat |
| Database server | Stores organised data for a long time. | MySQL, PostgreSQL, MongoDB |
| Cache server | Keeps often-used data in fast memory. | Redis, Memcached |
| Streaming server | Sends audio and video streams. | Video platforms |
| Game server | Keeps multiplayer games in sync in real time. | Online game servers |
| Backup server | Stores copies of data for recovery. | Daily or weekly backups |

> **🔗 Putting it together**
>
> **Domain** = the name (example.com) · **DNS** = the phone book that finds the IP · **Routing** = the GPS that finds the path · **Server** = the house where the website lives.

> **✔ Quick check 9 – Servers**
>
> Which server type is used when: (a) you open a news website; (b) your exam marks are stored; (c) you watch a live stream; (d) you play an online match; (e) files are restored after a computer breaks?
>
> **Answer:** (a) web server, (b) database server, (c) streaming server, (d) game server, (e) backup server.

