---
id: qNyJlfq-1RY
title: "SecTor 2025 | When Hackers Meet Burglars"
slug: sector-2025-when-hackers-meet-burglars
conference: black-hat
conference_name: "Black Hat"
category: "Security conferences"
edition: "Black Hat"
year: 2026
speakers: ["White Tuque"]
channel: "Black Hat"
duration_min: 31
published_at: 2026-05-19T17:00:01Z
video_id: qNyJlfq-1RY
url: https://www.youtube.com/watch?v=qNyJlfq-1RY
youtube_url: https://www.youtube.com/watch?v=qNyJlfq-1RY
tags: []
topics: ["Security, safety & red teaming"]
transcript: true
---

# SecTor 2025 | When Hackers Meet Burglars

**White Tuque**

`Black Hat` · `Black Hat` · `2026` · `31 min`

[Watch the recording](https://www.youtube.com/watch?v=qNyJlfq-1RY) · [Conference site](https://www.blackhat.com/)

## Description

Smart buildings blur the line between IT and physical infrastructure, connecting HVAC, lighting, access control, elevators, cameras, and more under a single "brain" called a Building Automation System (BAS). Drawing on real engagements against Canadian smart building deployments, this talk guides you through a red teaming exercise that uncovers both digital and physical attack paths. You'll see how attackers gather intel, probe entry points, exploit insecure IoT protocols, and seize control of critical systems. We'll examine live scans, protocol abuse and real world video demos.

Finally, we will flip to defense mode, offering a practical blue team playbook. Attendees will leave with an actionable framework rooted in Canadian field experience, for both offensive engagements and OT focused defenses.

By: Amir Hosseinpour  |  Offensive Security Specialist, White Tuque

## Transcript

*3,193 words · source: supa (en, exact timings)*

**[0:03](https://www.youtube.com/watch?v=qNyJlfq-1RY&t=3s)** Hello everyone. My name is Amir. I'm an offensive security specialist at White Tuk, uh, a hacker, a pentester, a security nerd, and I'm also a member at task security community where we get together every month, the last Wednesday of every month, and we chat about security. I'm not really a fan of introductions. So, uh, let's just jump right into it. So, before talking about the smart buildings, I want to just set the stage by showing you a few of the recent incidents.

**[0:55](https://www.youtube.com/watch?v=qNyJlfq-1RY&t=55s)** So over the past few years the incident in the smart building sector is increasing. Some of you might remember the famous target breach. This is one of the oldest ones from 2013. Uh attackers hacked target network through a HVAC contractor. They hacked the Hrack contractor, got the credentials, and through that vendor got into their systems, stole the credit card information, and over $40 million. Next one is more recent. It's a hack that it's actually a DOS attack that

**[1:46](https://www.youtube.com/watch?v=qNyJlfq-1RY&t=106s)** happened in Finland. two apartments in Finland were targeted by a random hacker group. I I couldn't find any information about those hackers, but they disrupted all of the operations in the building for almost a week. And I was researching about the property manager behind those two apartments. After a couple of months after that incident, they seized all of the operations across Finland. This is also another recent one. Um, some of you might might heard about the Omni Hotels and Resort that was targeted by ransomware group. The ransomware

**[2:34](https://www.youtube.com/watch?v=qNyJlfq-1RY&t=154s)** group demanded $2 million. Omni Hotels had to revert back to manual controls. They had to evacuate the hotels and later on they disclosed that the damage was almost $3.5 million. Another one uh a school district in Arizona was targeted by ransomware group. Uh they also lost all of their operations. The disruption on their system caused them to shut down the classes for a week. This one is really interesting. So I've been trying to spread awareness around the smart building security and I've

**[3:22](https://www.youtube.com/watch?v=qNyJlfq-1RY&t=202s)** been giving this talk. It's about a year now that I'm giving this talk and uh this incident actually happened two weeks ago. a school district in Texas was targeted by a ransomware group. uh FBI is already investigating it but there is no case study so we don't know how it happened but all of the phones the control systems the IoT devices there was a disruption in whole the operational technology systems so the ransomware in the smart building world is being called siege by security researchers And some of the hacker groups they call it siegeware because

**[4:11](https://www.youtube.com/watch?v=qNyJlfq-1RY&t=251s)** unlike the traditional ransomwarees it's not targeting the data is targeting the operation which is the most important thing for any smart building. So now let's talk about what is actually a smart building. A smart building is any building equipped with computerized controls and IoT devices that automate things like heating, ventilation, air conditioning, HVAC, elevators, security cameras, and so on. Controllers and sensors all connected everywhere to make life easier and more

**[4:59](https://www.youtube.com/watch?v=qNyJlfq-1RY&t=299s)** efficient. For example, sensors might detect the room is empty and automatically turn off lights or HVAC to save up energy. Occupants can unlock doors through their badge or a smartphone and everything is centrally managed by a building automation system often called BAS. In short, these innovations make buildings more efficient and convenient, but they also introduce new risks. All those connections and controllers are like digital doors and windows. If not secure, hackers can sink

**[5:49](https://www.youtube.com/watch?v=qNyJlfq-1RY&t=349s)** in and disrupt old operations. A smart building merges the digital and the physical world together. So a cyber attack can have real world consequences. Imagine heat turning off in winter or all the doors opening up at once. A smart building security is not just a feature but a fundamental requirement. And if you don't start with security, you won't definitely end up with it. In this talk, we'll see how redteamers approach these buildings, what vulnerabilities they find, the tools and techniques, or as I like to call it, the

**[6:39](https://www.youtube.com/watch?v=qNyJlfq-1RY&t=399s)** weapons and tactics they use. We also look at a couple of real world cases and case studies. And in the end we switched to the defense perspective to see how to defend buildings from the threats. So smart building red teaming like any other red team engagement and any other hack starts with the reconnaissance. So the red teamer starts with the external reconnaissance. Some smart building systems are connected to the internet maybe for remote management by vendors or building managers or sometimes often they are

**[7:29](https://www.youtube.com/watch?v=qNyJlfq-1RY&t=449s)** just connected to the internet without any reason and this happens much more often than you think. A favorite tool is showdown. Showdown is a search engine for internet connected devices and it's surprisingly effective. In one famous case, researchers found the control system for a Google office building in Sydney. The Google office building had a control system that was connected to the internet. It was unpatched and used the default password that let the researchers get into the building system and network.

**[8:18](https://www.youtube.com/watch?v=qNyJlfq-1RY&t=498s)** If even Google buildings was vulnerable to attemp due to a missed update, imagine how many others are. Researchers found over 25,000 other buildings connected online that had the same building management system and it was unpatched. So I want to talk about some of the statistics. This statistics is from 2024 and it shows the exposed OT devices connected to the internet. The showdown that I just mentioned and these are the top 10 countries and

**[9:08](https://www.youtube.com/watch?v=qNyJlfq-1RY&t=548s)** these are the number of devices that are connected. Canada is among the top 10 and these are the devices connected the protocols of those devices and as you can see over 15,000 devices that are connected to the internet are speaking backnet and backnet by default doesn't use any encryption. It could be configured to use encryption but by default it doesn't. But among this top 10 countries uh only two of them have decreased the number of devices that are connected to the internet which are Canada and the US and this chart shows that over 2024 the

**[10:00](https://www.youtube.com/watch?v=qNyJlfq-1RY&t=600s)** number of devices connected to the internet have been decreased which is a good factor because you don't want your smart building devices your control system connected to the internet. So a red teamer will use tools like showdown or Google searches to see if the target buildings hag or control systems are connected to the internet. They might search online for any manuals or user chatter ons or any default credentials. They look for clues like the building's name, the manufacturer of its systems, or any employee profile on the internet. Even a simple fine like the building's

**[10:49](https://www.youtube.com/watch?v=qNyJlfq-1RY&t=649s)** user manual can reveal default password. Then the red teamer might physically move closer. smartphone in hand but we scan for Wi-Fi networks in the building. Sometimes attackers even dress as HVAC technician. We sleep into the maintenance areas. This is all part of understanding the overall digital posture which goes hand in hand with the physical. Our operative might ride the elevator to a public floor or walk around the building's perimeter. Smartphone in hand scanning for Wi-Fi networks. A fine a Wi-Fi named building

**[11:41](https://www.youtube.com/watch?v=qNyJlfq-1RY&t=701s)** control or HVAC Wi-Fi means that there is a clue worth investigating. At the end of the recon, the red team will have a map of the potential entry points into the building's network. Once they have access to the building network, either by connecting through a misconfigured Wi-Fi or just cracking the Wi-Fi password, they will perform a networker scan. In simple terms, this means they are checking which digital doors are open on the network. Each device, servers, controllers

**[12:30](https://www.youtube.com/watch?v=qNyJlfq-1RY&t=750s)** communicate on certain ports like channels and some of these ports might be wide open with no guard. They use a scanning tool. One popular one is end mapap and they try to check to see which services and applications are running on the server. This is like rattling every door knob to see which one are unlocked. For example, they might discover a building management server at an IP address port 80 open, which means a web interface is running on the build on the building server, which usually is the building management system, or port 502 open, a port commonly used

**[13:21](https://www.youtube.com/watch?v=qNyJlfq-1RY&t=801s)** by industrial control systems, or UDP port 470 478 open, which is a port often associated with backnet. In this video, I'm on a red team exercise with my mentor Nick and after getting access to the server room, we are lockpicking the server door to get access to the switches and the main network. After unlocking the server door, I will

**[14:17](https://www.youtube.com/watch?v=qNyJlfq-1RY&t=857s)** try to run a porter scan on the on the building's network to see which ports are open. Now I just want to mention some of the tools that are being used in a red team exercise by security professionals or the malicious attackers for log picking. Uh usually a pick gun. I love pick guns because they are much easier to use. They are faster and if you use electronic pick gun, it usually

**[15:05](https://www.youtube.com/watch?v=qNyJlfq-1RY&t=905s)** can open normal server doors in just a sec in under seconds. For RFID cloning or badge access, they might use tools like Proxmark to clone the cards that are being used for access to the building. And of course, the favorite tool for every hacker is a laptop. Now think of each port as a door into the system. An open port means a server or program on the server is listening for connections. For example, port 80 indicates a web server is running.

**[15:54](https://www.youtube.com/watch?v=qNyJlfq-1RY&t=954s)** An open port by itself isn't necessarily bad, but it could be an unlocked door if the service behind it has a flaw. Hackers look for these because an old or misconfigured service might just let them slip in. In our scan, we find port 478 open, suggesting this building speaks back then. a common building automation language. Backnet often has little to no security by default. So finding that is like discovering a door which is unlocked by design. By testing these ports, we are essentially mapping the building's

**[16:43](https://www.youtube.com/watch?v=qNyJlfq-1RY&t=1003s)** digital floor plan, identifying all the ways we might break in. This matters because you can't defend a door that you don't know you have. Let's say the scan found a building management web interface open on port 80 and perhaps a few other services. The red teamer will try to open that web interface in a browser. Often these interfaces are protected by a login but many times the default credentials are never changed. For instance, common brand of HVAC controls might default

**[17:31](https://www.youtube.com/watch?v=qNyJlfq-1RY&t=1051s)** just to admin admin. If the building staff didn't update it, the red teamer can literally log in. This happens more often than you think. The Google building in Sydney that we mentioned had a default password and it worked. If the default credentials don't work, the red team might try a brute force attack, automate guessing, or look for leaked passwords. But often times an easier path exists. I also put a diagram that it was from a IBM survey in 2024.

**[18:20](https://www.youtube.com/watch?v=qNyJlfq-1RY&t=1100s)** It wasn't directly targeted for smart buildings or industrial control systems, but it shows that over 86% of the network devices are using default credentials. So, this is where the excitement really ramps up. The red team found a way inside one of the building control systems. Let's walk through a couple of real world cases that this happened. Remember that Google office in Sydney? It was running a building management platform called Tridium Niagara. Hackers had discovered a serious flaw in the software and the patch was released.

**[19:11](https://www.youtube.com/watch?v=qNyJlfq-1RY&t=1151s)** But the building system, the Google building was unpatched. The researchers exploited that flaw to get access to the building controls. In other words, one warnable HVAC controller was a pivot point to everything else. Smart buildings often have badge access panels and electronic locks. These are also computers and they can be hacked. In a defconerence presentation, two researchers showed how a compromised modern door control system can be exploited by the control panel

**[20:00](https://www.youtube.com/watch?v=qNyJlfq-1RY&t=1200s)** software. They found eight vulnerabilities in access controller which allowed them to do things like unlock doors without a proper badge swipe. But not all the attacks are purely technical. The red team might physically insert a device into the network. For example, hiding a tiny dropbox into a ceiling or a wall jack that creates a back door. Or they could use social engineering, tricking an employee into clicking on a malicious email that gives a foothold into the building's network. Once you have some access, you can often

**[20:49](https://www.youtube.com/watch?v=qNyJlfq-1RY&t=1249s)** mix and match the methods. Maybe send a malicious command to the HR controller to overhead the server room as a diversion while you go after the main target. One of the most striking cases of building automation attack is KN&X lock. Attackers remotely access the building's KN&X base authentication system commonly used for lighting, climate control, and other critical functions. An exploited standard KNX feature for reset password across hundreds of devices. This effectively locked out all of the

**[21:41](https://www.youtube.com/watch?v=qNyJlfq-1RY&t=1301s)** devices that were connected to the automation system, turning the affected devices into zombies. According to the investigation, the attackers systematically targeted devices that had little to no security in place. By issuing legitimate KN&X commands to set or change the passwords, they force the building's operator to negotiate or pay ransom if they ever wanted to regain control. Almost overnight, three quarters of the building's smart devices were rendered useless. From hback to lighting systems, it's a reminder that attacker doesn't

**[22:31](https://www.youtube.com/watch?v=qNyJlfq-1RY&t=1351s)** always need a zero day exploit or sophisticated malware. Sometimes a built-in feature if unsecured can become a devastating weapon. The KN&X log campaign drew so much attention that it was added to MITER list of attack techniques for industrial control systems emphasizing how building automation vulnerabilities can have serious real world consequences. While there isn't a single KN KNX lock CVE that addresses every vulnerable device, multiple KN&X related vulnerabilities have been

**[23:19](https://www.youtube.com/watch?v=qNyJlfq-1RY&t=1399s)** documented from under these two main CVES highlighting insecure KNX IP implementation. In addition, CISA publishes advisories on industrial and building automation systems, underscoring the wider spread nature of insecure configurations in KN&X networks. In 2023, researchers found 16,000 more connected devices that were using the same vulnerable automation system in Dutch area, which was Germany, Switzerland, and Austria. Now that we live through the nightmare scenario, let's switch to the defense

**[24:10](https://www.youtube.com/watch?v=qNyJlfq-1RY&t=1450s)** perspective. How can we secure these buildings against the threats? The good news is for every weakness we saw, there are effective counter measures. It's all about applying solid cyber security best practices to the ward of facilities and OT. Know all your assets. First, you can't protect what you don't know you have. Make an inventory of all smart systems in your building. Hback, controllers, batch systems, camera, lighting. Many buildings don't realize that a contractor installed a remote access

**[24:58](https://www.youtube.com/watch?v=qNyJlfq-1RY&t=1498s)** modem to an elevator for for control. Find it documented. Network segmentation. This is just a fancy term for creating separate lanes on the network highway. Your building control system should be on a separate network from your guest Wi-Fi. If the HVAC system doesn't need to talk to internet, pull up the virtual drawbridge. No internet access. If remote access is needed for vendors, use a secure VPN with multiffactor authentication. Rather than leaving the port exposed public segmentation also means that if

**[25:49](https://www.youtube.com/watch?v=qNyJlfq-1RY&t=1549s)** one system gets compromised, the attacker can't easily jump in to the other parts of the building. In the Google hack, Google said that the compromised HVAC system was not connected to the other parts of the network and that segmentation limited the damage. Secure configurations change default passwords. Every camera, every controller use a strong unique passphrases. Also disable any devices or ports that you don't use. If a building controller has a FTP service open, but you don't need it,

**[26:36](https://www.youtube.com/watch?v=qNyJlfq-1RY&t=1596s)** turn it off. Fewer open ports means fewer ways in. And of course, keep up with patches and updates. The patch that could have saved Google office building was already released. long before the attack, but they the updates could prevent the exploits from happening in the first place. Use a strong authentication for any user accounts. That might mean integrating the building systems with your corporate directory or adding two factor authentication for every user accounts.

**[27:24](https://www.youtube.com/watch?v=qNyJlfq-1RY&t=1644s)** Monitor everything and don't forget the physical side. Secure rooms and ports. Make sure server rooms and network closets are locked and only authorized personnel can get in. Have a plan before something happens. Have an incident response plan. Work with your IT team and facilities management to outline what to do if the building systems are attacked. For example, if suddenly the building automation is compromised, who has the authority to pull the plug and revert back to manual controls. And lastly, but not least, do what we are doing here proactively. Bring in experts to test your smart building security.

**[28:14](https://www.youtube.com/watch?v=qNyJlfq-1RY&t=1694s)** on a regular basis. They might find the holes so you can fix them. Also stay informed. Follow advisories and organizations or vendors bulletins for any new vulnerabilities. Each of the each of these measures adds layers to the building's overall security posture. All there is no single silver bullet. All of them can protect the buildings from being compromised. Thank you. If anyone has any questions. So when it comes to badge cloning right

**[29:07](https://www.youtube.com/watch?v=qNyJlfq-1RY&t=1747s)** that you mentioned is there a specific uh security standard those badges should have so that it won't be cloned >> from my understanding uh for the smart buildings like real estate highrise smart buildings there isn't a security compliance in place but what happens in practice is that a lot of this badge access and badge control systems and be clones pretty easily. >> But in the industrial environments, I don't know about the exact policies and uh compliances, but there is some that prevents it. For example, you have to use encryption on the keys that are being used for each card that makes it so hard to clone it almost impossible.

**[29:57](https://www.youtube.com/watch?v=qNyJlfq-1RY&t=1797s)** >> Got it. Got it. And also when it comes to executing these activities, right? um where and the scope is where it's multi-tenant building is the scope of performing physical security assessment very limited whereas where you you might not get access to the HWAX um or the common building assess um areas >> it depends on the project usually the buildings the real estate buildings who are asking for a security assessment are doing it before the tenants move in But in the cases that the tenants moved in uh they specify in the uh in the scoping call and in the scoping before the engagement uh you you can access a few areas of the buildings for example the electrical

**[30:46](https://www.youtube.com/watch?v=qNyJlfq-1RY&t=1846s)** closets or the edrack for example. Okay thanks.
