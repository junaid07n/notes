#!/usr/bin/env python3
"""
Khan Academy Computers - Comprehensive PDF Notes Generator
Generates detailed study notes on computer fundamentals
"""

from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, Image
from reportlab.lib import colors
from datetime import datetime


def create_comprehensive_notes():
    """
    Create comprehensive notes on computer fundamentals
    Based on typical Khan Academy Computers curriculum
    """
    
    return {
        'title': 'Computers and Computer Science',
        'subtitle': 'Comprehensive Study Notes from Khan Academy',
        'sections': [
            {
                'title': '1. What is a Computer?',
                'subsections': [
                    {
                        'heading': 'Introduction to Computers',
                        'content': [
                            'A computer is an electronic device that manipulates information or data. It has the ability to store, retrieve, and process data. You may already know that you can use a computer to type documents, send email, play games, and browse the Web.',
                            'Computers are incredibly versatile machines that can perform a wide variety of tasks. From simple calculations to complex simulations, computers have become an integral part of modern life.',
                            'The word "computer" comes from the word "compute," which means to calculate. Originally, computers were people who performed calculations, but now the term refers to the machines that automate these calculations.'
                        ]
                    },
                    {
                        'heading': 'Basic Computer Functions',
                        'content': [
                            'All computers perform four basic functions:',
                        ],
                        'list_items': [
                            'INPUT: Receiving data from the outside world (keyboard, mouse, microphone, camera)',
                            'PROCESSING: Performing operations on data using the CPU (calculations, comparisons, decisions)',
                            'STORAGE: Saving data for later use (hard drive, SSD, RAM, cloud storage)',
                            'OUTPUT: Sending results back to the outside world (screen, speakers, printer)'
                        ],
                        'content_after': [
                            'These four functions work together in a cycle to accomplish any computing task, from browsing the internet to rendering 3D graphics in video games.'
                        ]
                    },
                    {
                        'heading': 'Types of Computers',
                        'content': [
                            'Computers come in many shapes and sizes, each designed for specific purposes:'
                        ],
                        'list_items': [
                            'Desktop Computers: Stationary computers designed for regular use at a single location',
                            'Laptop Computers: Portable computers with built-in screen, keyboard, and trackpad',
                            'Tablets: Touchscreen devices that are more portable than laptops',
                            'Smartphones: Pocket-sized computers with cellular connectivity',
                            'Servers: Powerful computers that provide services to other computers over a network',
                            'Mainframes: Very large computers used by major organizations for critical applications',
                            'Supercomputers: The most powerful computers, used for complex scientific calculations',
                            'Embedded Systems: Computers built into other devices (cars, appliances, medical equipment)'
                        ]
                    }
                ]
            },
            {
                'title': '2. Digital Information',
                'subsections': [
                    {
                        'heading': 'Binary System',
                        'content': [
                            'At its core, a computer is a machine that processes binary information. Binary means there are only two possible values: 0 and 1.',
                            'A single binary digit is called a BIT (Binary digIT). A bit is the smallest unit of data in computing.',
                            'Eight bits together form a BYTE. A byte can represent 256 different values (2^8 = 256).',
                            'Larger units of data measurement include:',
                        ],
                        'list_items': [
                            'Kilobyte (KB) = 1,024 bytes',
                            'Megabyte (MB) = 1,024 kilobytes = 1,048,576 bytes',
                            'Gigabyte (GB) = 1,024 megabytes = approximately 1 billion bytes',
                            'Terabyte (TB) = 1,024 gigabytes = approximately 1 trillion bytes',
                            'Petabyte (PB) = 1,024 terabytes',
                            'Exabyte (EB) = 1,024 petabytes'
                        ]
                    },
                    {
                        'heading': 'Why Binary?',
                        'content': [
                            'Computers use binary because it is easy to implement with electronic circuits. A transistor can be either ON (representing 1) or OFF (representing 0).',
                            'Binary is reliable because there are only two states to distinguish between, making it less susceptible to errors from electrical noise or component variations.',
                            'Modern computer processors contain billions of transistors, each capable of switching between these two states millions or billions of times per second.'
                        ]
                    },
                    {
                        'heading': 'Representing Information in Binary',
                        'content': [
                            'All information in a computer is represented using binary:',
                        ],
                        'list_items': [
                            'NUMBERS: Using binary number system (base-2). For example, the decimal number 5 is 101 in binary.',
                            'TEXT: Using character encoding schemes like ASCII or Unicode. Each character is assigned a unique binary number.',
                            'IMAGES: Using pixels, where each pixel\'s color is represented by binary numbers (typically RGB values).',
                            'AUDIO: By sampling sound waves at regular intervals and storing the amplitude as binary numbers.',
                            'VIDEO: As a sequence of images (frames) combined with audio, all stored as binary data.',
                            'PROGRAMS: As sequences of binary instructions that the CPU can execute.'
                        ]
                    },
                    {
                        'heading': 'Analog vs Digital',
                        'content': [
                            'ANALOG information is continuous and can have an infinite number of values. Examples include sound waves, light intensity, and temperature.',
                            'DIGITAL information is discrete and has distinct values. It is represented by specific numbers.',
                            'Converting analog to digital (digitization) involves sampling the analog signal at regular intervals and storing each sample as a digital value.',
                            'The sampling rate determines the quality of the digital representation. Higher sampling rates capture more detail but require more storage space.'
                        ]
                    }
                ]
            },
            {
                'title': '3. Computer Hardware',
                'subsections': [
                    {
                        'heading': 'Central Processing Unit (CPU)',
                        'content': [
                            'The CPU is often called the "brain" of the computer. It executes program instructions and performs calculations.',
                            'Modern CPUs contain multiple cores, allowing them to execute multiple tasks simultaneously (parallel processing).',
                            'CPU performance is measured by:'
                        ],
                        'list_items': [
                            'Clock Speed: Measured in Gigahertz (GHz), indicates how many cycles per second the CPU can execute',
                            'Number of Cores: More cores allow for better multitasking and parallel processing',
                            'Cache Size: Fast memory built into the CPU for storing frequently accessed data',
                            'Architecture: The design and instruction set of the CPU (x86, ARM, etc.)'
                        ]
                    },
                    {
                        'heading': 'Memory (RAM)',
                        'content': [
                            'RAM (Random Access Memory) is temporary storage that the CPU uses for currently running programs and data.',
                            'RAM is volatile, meaning it loses its contents when the power is turned off.',
                            'More RAM allows a computer to run more programs simultaneously and handle larger datasets.',
                            'Typical RAM capacities range from 4GB in basic systems to 64GB or more in high-performance workstations.'
                        ]
                    },
                    {
                        'heading': 'Storage Devices',
                        'content': [
                            'Storage devices permanently save data even when the computer is powered off:',
                        ],
                        'list_items': [
                            'Hard Disk Drives (HDD): Use spinning magnetic platters to store data. Slower but more affordable for large capacities.',
                            'Solid State Drives (SSD): Use flash memory with no moving parts. Much faster than HDDs but more expensive per gigabyte.',
                            'USB Flash Drives: Portable storage using flash memory.',
                            'Memory Cards: Used in cameras, phones, and other portable devices.',
                            'Optical Discs: CDs, DVDs, and Blu-ray discs (becoming less common).',
                            'Cloud Storage: Data stored on remote servers accessed via the internet.'
                        ]
                    },
                    {
                        'heading': 'Input Devices',
                        'content': [
                            'Input devices allow users to enter data and commands into the computer:',
                        ],
                        'list_items': [
                            'Keyboard: For typing text and entering commands',
                            'Mouse/Trackpad: For pointing, clicking, and navigating',
                            'Touchscreen: For direct interaction with on-screen elements',
                            'Microphone: For recording audio and voice commands',
                            'Camera/Webcam: For capturing images and video',
                            'Scanner: For digitizing physical documents and images',
                            'Game Controllers: For gaming input (joysticks, gamepads)',
                            'Sensors: Temperature, motion, light, proximity sensors in various devices'
                        ]
                    },
                    {
                        'heading': 'Output Devices',
                        'content': [
                            'Output devices present information from the computer to the user:',
                        ],
                        'list_items': [
                            'Monitor/Display: Shows visual information (text, images, video)',
                            'Speakers/Headphones: Output audio',
                            'Printer: Creates physical copies of digital documents',
                            '3D Printer: Creates three-dimensional physical objects',
                            'Projector: Displays content on a large screen',
                            'Haptic Devices: Provide tactile feedback (vibration in game controllers)'
                        ]
                    }
                ]
            },
            {
                'title': '4. How Computers Process Information',
                'subsections': [
                    {
                        'heading': 'The Fetch-Decode-Execute Cycle',
                        'content': [
                            'The CPU processes instructions in a continuous cycle:',
                        ],
                        'list_items': [
                            'FETCH: The CPU retrieves the next instruction from memory',
                            'DECODE: The CPU interprets what the instruction means',
                            'EXECUTE: The CPU carries out the instruction',
                            'STORE: The result is written back to memory (if needed)'
                        ],
                        'content_after': [
                            'This cycle repeats billions of times per second in modern processors.',
                            'The Control Unit manages this cycle, directing the flow of data between the CPU, memory, and input/output devices.'
                        ]
                    },
                    {
                        'heading': 'Machine Language and Assembly',
                        'content': [
                            'MACHINE LANGUAGE is the lowest-level programming language, consisting of binary instructions that the CPU can execute directly.',
                            'Each CPU architecture has its own machine language instruction set.',
                            'ASSEMBLY LANGUAGE uses human-readable mnemonics to represent machine language instructions. For example, "ADD" instead of a binary code.',
                            'An assembler translates assembly language into machine language.',
                            'High-level programming languages (Python, Java, C++) are compiled or interpreted into machine language so the CPU can execute them.'
                        ]
                    },
                    {
                        'heading': 'Memory Hierarchy',
                        'content': [
                            'Computer memory is organized in a hierarchy based on speed and size:',
                        ],
                        'list_items': [
                            'CPU Registers: Fastest, smallest storage directly in the CPU (a few dozen variables)',
                            'Cache Memory: Very fast memory built into or near the CPU (megabytes)',
                            'RAM (Main Memory): Fast temporary storage (gigabytes)',
                            'SSD/Hard Drive: Slower permanent storage (terabytes)',
                            'Network/Cloud Storage: Slowest but virtually unlimited capacity'
                        ],
                        'content_after': [
                            'The computer tries to keep frequently used data in faster memory levels to improve performance.',
                            'Cache hits (finding data in cache) are much faster than cache misses (having to fetch from RAM).'
                        ]
                    }
                ]
            },
            {
                'title': '5. Software and Operating Systems',
                'subsections': [
                    {
                        'heading': 'What is Software?',
                        'content': [
                            'Software is a collection of instructions that tells the computer what to do. Without software, hardware is useless.',
                            'Software can be divided into two main categories:',
                        ],
                        'list_items': [
                            'SYSTEM SOFTWARE: Manages the computer hardware and provides services for application software. The operating system is the most important system software.',
                            'APPLICATION SOFTWARE: Programs designed to help users perform specific tasks (word processors, web browsers, games, etc.)'
                        ]
                    },
                    {
                        'heading': 'Operating Systems',
                        'content': [
                            'An operating system (OS) is software that manages computer hardware and software resources. Popular operating systems include:',
                        ],
                        'list_items': [
                            'Windows: Microsoft\'s OS, most common on desktop and laptop computers',
                            'macOS: Apple\'s OS for Mac computers',
                            'Linux: Open-source OS with many distributions (Ubuntu, Fedora, etc.)',
                            'iOS: Apple\'s mobile operating system for iPhones and iPads',
                            'Android: Google\'s mobile operating system, most common on smartphones',
                            'Chrome OS: Google\'s lightweight OS for Chromebooks'
                        ],
                        'content_after': [
                            'The operating system provides essential services such as:',
                        ],
                        'list_items_2': [
                            'Managing memory allocation for programs',
                            'Scheduling CPU time for different processes',
                            'Handling input and output operations',
                            'Managing files and directories',
                            'Providing security and user authentication',
                            'Running multiple programs simultaneously (multitasking)'
                        ]
                    },
                    {
                        'heading': 'Programming Languages',
                        'content': [
                            'Programming languages allow humans to write instructions for computers. They can be categorized by level:',
                        ],
                        'list_items': [
                            'LOW-LEVEL: Assembly language, close to machine code, hardware-specific',
                            'HIGH-LEVEL: Python, Java, C++, JavaScript - easier for humans to read and write',
                            'SCRIPTING: Python, JavaScript, Ruby - interpreted languages for automation and web development',
                            'DOMAIN-SPECIFIC: SQL for databases, HTML/CSS for web pages, R for statistics'
                        ],
                        'content_after': [
                            'High-level languages must be translated into machine code through compilation or interpretation.',
                            'COMPILERS translate the entire program before execution (C, C++).',
                            'INTERPRETERS translate and execute the program line by line (Python, JavaScript).'
                        ]
                    }
                ]
            },
            {
                'title': '6. Networks and the Internet',
                'subsections': [
                    {
                        'heading': 'Computer Networks',
                        'content': [
                            'A computer network is a group of computers connected together to share resources and information.',
                            'Networks can be classified by size and scope:',
                        ],
                        'list_items': [
                            'PAN (Personal Area Network): Very small network, typically within 10 meters (Bluetooth devices)',
                            'LAN (Local Area Network): Connects computers in a limited area like a home, school, or office',
                            'MAN (Metropolitan Area Network): Covers a city or large campus',
                            'WAN (Wide Area Network): Spans large geographical areas, potentially worldwide',
                            'The Internet: A global network of networks connecting billions of devices'
                        ]
                    },
                    {
                        'heading': 'How the Internet Works',
                        'content': [
                            'The Internet is a worldwide network of computers that communicate using standardized protocols.',
                            'Key concepts and components:',
                        ],
                        'list_items': [
                            'IP ADDRESS: A unique numerical identifier for each device on the network (e.g., 192.168.1.1)',
                            'DOMAIN NAME: Human-readable address (e.g., www.example.com) that maps to an IP address',
                            'DNS (Domain Name System): Translates domain names into IP addresses',
                            'PACKETS: Data is broken into small chunks called packets for transmission',
                            'ROUTERS: Direct packets along the best path to their destination',
                            'PROTOCOLS: Rules for communication (HTTP, HTTPS, FTP, SMTP, etc.)',
                            'ISP (Internet Service Provider): Company that provides internet access'
                        ]
                    },
                    {
                        'heading': 'World Wide Web',
                        'content': [
                            'The World Wide Web (WWW) is a system of interlinked documents and resources accessed via the Internet.',
                            'The Web is NOT the same as the Internet - it is a service that runs on top of the Internet.',
                            'Key Web technologies:',
                        ],
                        'list_items': [
                            'HTML (HyperText Markup Language): Defines the structure and content of web pages',
                            'CSS (Cascading Style Sheets): Controls the visual presentation of web pages',
                            'JavaScript: Adds interactivity and dynamic behavior to web pages',
                            'HTTP/HTTPS: Protocols for transferring web pages from servers to browsers',
                            'URLs (Uniform Resource Locators): Addresses for web resources',
                            'Web Browsers: Software that displays web pages (Chrome, Firefox, Safari, Edge)'
                        ]
                    },
                    {
                        'heading': 'Cybersecurity',
                        'content': [
                            'Cybersecurity is the practice of protecting systems, networks, and data from digital attacks.',
                            'Common security threats:',
                        ],
                        'list_items': [
                            'MALWARE: Malicious software including viruses, worms, trojans, and ransomware',
                            'PHISHING: Fraudulent attempts to obtain sensitive information by disguising as trustworthy',
                            'HACKING: Unauthorized access to computer systems',
                            'DDoS ATTACKS: Overwhelming a system with traffic to make it unavailable',
                            'DATA BREACHES: Unauthorized access to confidential data'
                        ],
                        'content_after': [
                            'Security best practices:',
                        ],
                        'list_items_2': [
                            'Use strong, unique passwords for different accounts',
                            'Enable two-factor authentication when available',
                            'Keep software and operating systems updated',
                            'Use antivirus software and firewalls',
                            'Be cautious about clicking links or downloading attachments',
                            'Use encrypted connections (HTTPS) for sensitive information',
                            'Regular backups of important data'
                        ]
                    }
                ]
            },
            {
                'title': '7. Algorithms and Problem Solving',
                'subsections': [
                    {
                        'heading': 'What is an Algorithm?',
                        'content': [
                            'An algorithm is a step-by-step procedure for solving a problem or accomplishing a task.',
                            'Algorithms are the foundation of computer programming and can be expressed in various ways: natural language, pseudocode, flowcharts, or programming code.',
                            'Good algorithms should be:',
                        ],
                        'list_items': [
                            'CLEAR: Each step is precisely defined',
                            'FINITE: Has a definite beginning and end',
                            'EFFECTIVE: Each step can actually be performed',
                            'CORRECT: Produces the right answer for all valid inputs',
                            'EFFICIENT: Uses reasonable amounts of time and memory'
                        ]
                    },
                    {
                        'heading': 'Algorithm Examples',
                        'content': [
                            'Everyday examples of algorithms:',
                        ],
                        'list_items': [
                            'RECIPE: Step-by-step instructions for cooking',
                            'ASSEMBLY INSTRUCTIONS: How to put together furniture',
                            'NAVIGATION: Directions from one location to another',
                            'SEARCH: Finding a word in a dictionary',
                            'SORTING: Organizing a deck of cards by value'
                        ]
                    },
                    {
                        'heading': 'Computational Thinking',
                        'content': [
                            'Computational thinking is a problem-solving approach that involves:',
                        ],
                        'list_items': [
                            'DECOMPOSITION: Breaking complex problems into smaller, manageable parts',
                            'PATTERN RECOGNITION: Identifying similarities and trends',
                            'ABSTRACTION: Focusing on important information while ignoring irrelevant details',
                            'ALGORITHM DESIGN: Creating step-by-step solutions',
                            'DEBUGGING: Testing and fixing errors'
                        ],
                        'content_after': [
                            'These skills are valuable not just in programming, but in solving problems in many areas of life.'
                        ]
                    },
                    {
                        'heading': 'Algorithm Efficiency',
                        'content': [
                            'Not all algorithms that solve the same problem are equally good. Efficiency matters when processing large amounts of data.',
                            'Time Complexity: How the algorithm\'s runtime grows as the input size increases',
                            'Space Complexity: How much memory the algorithm needs',
                            'Common complexity classes (from fastest to slowest):',
                        ],
                        'list_items': [
                            'O(1) - Constant: Same time regardless of input size',
                            'O(log n) - Logarithmic: Time grows slowly as input increases',
                            'O(n) - Linear: Time proportional to input size',
                            'O(n log n) - Linearithmic: Efficient sorting algorithms',
                            'O(n²) - Quadratic: Time grows with the square of input size',
                            'O(2ⁿ) - Exponential: Time doubles with each additional input'
                        ]
                    }
                ]
            },
            {
                'title': '8. Data Representation',
                'subsections': [
                    {
                        'heading': 'Number Systems',
                        'content': [
                            'Computers use different number systems for different purposes:',
                        ],
                        'list_items': [
                            'DECIMAL (Base 10): Uses digits 0-9. What humans typically use.',
                            'BINARY (Base 2): Uses only 0 and 1. What computers use internally.',
                            'HEXADECIMAL (Base 16): Uses 0-9 and A-F. Compact way to represent binary.',
                            'OCTAL (Base 8): Uses 0-7. Sometimes used in file permissions.'
                        ],
                        'content_after': [
                            'Converting between number systems is an important skill in computer science.',
                            'Example: Decimal 255 = Binary 11111111 = Hexadecimal FF'
                        ]
                    },
                    {
                        'heading': 'Text Encoding',
                        'content': [
                            'Computers represent text characters as numbers using encoding schemes:',
                        ],
                        'list_items': [
                            'ASCII (American Standard Code for Information Interchange): 7-bit encoding, 128 characters. Includes English letters, digits, and symbols.',
                            'Extended ASCII: 8-bit encoding, 256 characters. Adds accented letters and special symbols.',
                            'UNICODE: Modern standard supporting over 100,000 characters from all world languages, emojis, and symbols.',
                            'UTF-8: Variable-length Unicode encoding, most common on the web. Compatible with ASCII.',
                            'UTF-16: Uses 16 bits per character, used internally by many systems.'
                        ],
                        'content_after': [
                            'Example: The letter "A" is represented as decimal 65, binary 01000001, hexadecimal 41 in ASCII/Unicode.'
                        ]
                    },
                    {
                        'heading': 'Image Representation',
                        'content': [
                            'Digital images are composed of pixels (picture elements), each with a color value.',
                            'Common color models:',
                        ],
                        'list_items': [
                            'RGB (Red, Green, Blue): Each color channel typically uses 8 bits (0-255), allowing 16.7 million colors',
                            'CMYK (Cyan, Magenta, Yellow, Black): Used in printing',
                            'Grayscale: Single channel representing brightness'
                        ],
                        'content_after': [
                            'Image resolution is measured in pixels (e.g., 1920×1080) or dots per inch (DPI).',
                            'File formats:',
                        ],
                        'list_items_2': [
                            'JPEG: Lossy compression, good for photographs',
                            'PNG: Lossless compression, supports transparency',
                            'GIF: Limited to 256 colors, supports animation',
                            'SVG: Vector graphics that scale without quality loss'
                        ]
                    },
                    {
                        'heading': 'Audio Representation',
                        'content': [
                            'Digital audio is created by sampling analog sound waves at regular intervals.',
                            'Key parameters:',
                        ],
                        'list_items': [
                            'SAMPLE RATE: How many samples per second (measured in Hz). CD quality is 44,100 Hz.',
                            'BIT DEPTH: How many bits per sample. CD quality is 16 bits.',
                            'CHANNELS: Mono (1 channel) or Stereo (2 channels) or more for surround sound'
                        ],
                        'content_after': [
                            'Audio file formats:',
                        ],
                        'list_items_2': [
                            'WAV/AIFF: Uncompressed, large file size, high quality',
                            'MP3: Lossy compression, smaller files, slight quality loss',
                            'FLAC: Lossless compression, high quality, moderate file size',
                            'AAC: Lossy compression, better quality than MP3 at same bitrate'
                        ]
                    }
                ]
            },
            {
                'title': '9. Computing History and Future',
                'subsections': [
                    {
                        'heading': 'Brief History of Computing',
                        'content': [
                            'The evolution of computers spans several major eras:',
                        ],
                        'list_items': [
                            'MECHANICAL ERA (1600s-1900s): Mechanical calculators and Charles Babbage\'s Analytical Engine',
                            'ELECTROMECHANICAL ERA (1930s-1940s): Early computers using relays and vacuum tubes',
                            'FIRST GENERATION (1940s-1950s): ENIAC and other vacuum tube computers',
                            'SECOND GENERATION (1950s-1960s): Transistor-based computers',
                            'THIRD GENERATION (1960s-1970s): Integrated circuits made computers smaller and faster',
                            'FOURTH GENERATION (1970s-present): Microprocessors enabled personal computers',
                            'FIFTH GENERATION (present-future): AI and quantum computing'
                        ],
                        'content_after': [
                            'Moore\'s Law (1965): The observation that the number of transistors on a microchip doubles approximately every two years, while costs are halved. This trend has held true for decades but may be reaching physical limits.'
                        ]
                    },
                    {
                        'heading': 'Artificial Intelligence',
                        'content': [
                            'AI is the simulation of human intelligence by machines. Current AI approaches include:',
                        ],
                        'list_items': [
                            'MACHINE LEARNING: Systems that learn from data without explicit programming',
                            'NEURAL NETWORKS: Computing systems inspired by biological neural networks',
                            'DEEP LEARNING: Neural networks with many layers, powerful for image and speech recognition',
                            'NATURAL LANGUAGE PROCESSING: Understanding and generating human language',
                            'COMPUTER VISION: Analyzing and understanding visual information'
                        ],
                        'content_after': [
                            'AI applications are widespread: virtual assistants, recommendation systems, autonomous vehicles, medical diagnosis, language translation, and much more.'
                        ]
                    },
                    {
                        'heading': 'Emerging Technologies',
                        'content': [
                            'The future of computing includes several exciting areas:',
                        ],
                        'list_items': [
                            'QUANTUM COMPUTING: Uses quantum mechanics principles to solve certain problems exponentially faster than classical computers',
                            'INTERNET OF THINGS (IoT): Network of physical devices embedded with sensors and connectivity',
                            'EDGE COMPUTING: Processing data near where it\'s generated rather than in centralized data centers',
                            '5G AND BEYOND: Faster, more reliable wireless communications',
                            'AUGMENTED REALITY (AR): Overlay digital information on the real world',
                            'VIRTUAL REALITY (VR): Fully immersive computer-generated environments',
                            'BLOCKCHAIN: Distributed ledger technology for secure, transparent transactions',
                            'NEUROMORPHIC COMPUTING: Computer architectures modeled after the human brain'
                        ]
                    },
                    {
                        'heading': 'Ethical and Social Implications',
                        'content': [
                            'As computing becomes more powerful and pervasive, important questions arise:',
                        ],
                        'list_items': [
                            'PRIVACY: How is personal data collected, stored, and used?',
                            'SECURITY: How can we protect against cyber threats?',
                            'DIGITAL DIVIDE: Inequality in access to technology and digital literacy',
                            'AUTOMATION: Impact on employment as AI and robots replace human workers',
                            'BIAS IN AI: Ensuring algorithms don\'t perpetuate or amplify human biases',
                            'ENVIRONMENTAL IMPACT: Energy consumption of data centers and electronic waste',
                            'INTELLECTUAL PROPERTY: Copyright, patents, and open source in the digital age',
                            'MISINFORMATION: Spread of false information through digital platforms'
                        ],
                        'content_after': [
                            'Understanding these issues is crucial for responsible development and use of technology.'
                        ]
                    }
                ]
            }
        ]
    }


def create_pdf(output_file):
    """Generate comprehensive PDF notes"""
    
    # Get content
    notes = create_comprehensive_notes()
    
    # Create PDF document
    doc = SimpleDocTemplate(
        output_file,
        pagesize=letter,
        rightMargin=0.75*inch,
        leftMargin=0.75*inch,
        topMargin=0.75*inch,
        bottomMargin=0.75*inch
    )
    
    # Container for PDF elements
    story = []
    
    # Define styles
    styles = getSampleStyleSheet()
    
    # Custom styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=26,
        textColor=colors.HexColor('#1c4587'),
        spaceAfter=20,
        spaceBefore=12,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=colors.HexColor('#4a4a4a'),
        spaceAfter=30,
        alignment=TA_CENTER,
        fontName='Helvetica'
    )
    
    section_title_style = ParagraphStyle(
        'SectionTitle',
        parent=styles['Heading1'],
        fontSize=18,
        textColor=colors.HexColor('#1c4587'),
        spaceAfter=16,
        spaceBefore=20,
        fontName='Helvetica-Bold',
        borderWidth=1,
        borderColor=colors.HexColor('#1c4587'),
        borderPadding=8,
        backColor=colors.HexColor('#e8f0f8')
    )
    
    subsection_style = ParagraphStyle(
        'Subsection',
        parent=styles['Heading2'],
        fontSize=14,
        textColor=colors.HexColor('#2c5f8d'),
        spaceAfter=10,
        spaceBefore=12,
        fontName='Helvetica-Bold'
    )
    
    body_style = ParagraphStyle(
        'CustomBody',
        parent=styles['Normal'],
        fontSize=11,
        alignment=TA_JUSTIFY,
        spaceAfter=10,
        leading=15,
        fontName='Helvetica'
    )
    
    bullet_style = ParagraphStyle(
        'BulletPoint',
        parent=styles['Normal'],
        fontSize=11,
        leftIndent=20,
        spaceAfter=8,
        leading=14,
        fontName='Helvetica'
    )
    
    # Title page
    story.append(Spacer(1, 1.5*inch))
    story.append(Paragraph(notes['title'], title_style))
    story.append(Spacer(1, 0.3*inch))
    story.append(Paragraph(notes['subtitle'], subtitle_style))
    story.append(Spacer(1, 0.5*inch))
    
    # Date and source
    date_style = ParagraphStyle(
        'Date',
        parent=styles['Normal'],
        fontSize=10,
        textColor=colors.HexColor('#666666'),
        alignment=TA_CENTER
    )
    story.append(Paragraph(f"Generated: {datetime.now().strftime('%B %d, %Y')}", date_style))
    story.append(Paragraph("Based on Khan Academy Curriculum", date_style))
    
    story.append(PageBreak())
    
    # Table of Contents
    story.append(Paragraph("Table of Contents", section_title_style))
    story.append(Spacer(1, 0.2*inch))
    
    for section in notes['sections']:
        toc_entry = section['title']
        story.append(Paragraph(toc_entry, body_style))
        story.append(Spacer(1, 0.05*inch))
    
    story.append(PageBreak())
    
    # Content sections
    for section in notes['sections']:
        # Section title
        story.append(Paragraph(section['title'], section_title_style))
        story.append(Spacer(1, 0.15*inch))
        
        # Subsections
        for subsection in section['subsections']:
            # Subsection heading
            story.append(Paragraph(subsection['heading'], subsection_style))
            story.append(Spacer(1, 0.1*inch))
            
            # Content paragraphs
            if 'content' in subsection:
                for para in subsection['content']:
                    # Escape special characters
                    para = para.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
                    story.append(Paragraph(para, body_style))
            
            # List items
            if 'list_items' in subsection:
                for item in subsection['list_items']:
                    item = item.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
                    story.append(Paragraph(f"• {item}", bullet_style))
            
            # Content after list
            if 'content_after' in subsection:
                story.append(Spacer(1, 0.1*inch))
                for para in subsection['content_after']:
                    para = para.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
                    story.append(Paragraph(para, body_style))
            
            # Second list if exists
            if 'list_items_2' in subsection:
                for item in subsection['list_items_2']:
                    item = item.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
                    story.append(Paragraph(f"• {item}", bullet_style))
            
            story.append(Spacer(1, 0.15*inch))
        
        story.append(PageBreak())
    
    # Footer note
    footer_style = ParagraphStyle(
        'Footer',
        parent=styles['Normal'],
        fontSize=9,
        textColor=colors.HexColor('#666666'),
        alignment=TA_CENTER,
        fontName='Helvetica-Oblique'
    )
    
    story.append(Spacer(1, 0.5*inch))
    story.append(Paragraph("End of Notes", footer_style))
    story.append(Spacer(1, 0.1*inch))
    story.append(Paragraph(
        "For more information and interactive lessons, visit Khan Academy at www.khanacademy.org",
        footer_style
    ))
    
    # Build PDF
    print("Building PDF document...")
    doc.build(story)
    print(f"✓ PDF successfully created: {output_file}")


def create_html(output_file):
    """Generate a well-designed HTML website from the notes content"""

    notes = create_comprehensive_notes()

    def escape_html(text):
        return (text.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
                .replace('"', '&quot;').replace("'", '&#x27;'))

    # Build navigation items and section HTML
    nav_items = []
    sections_html = []

    for idx, section in enumerate(notes['sections']):
        section_id = f"section-{idx}"
        nav_items.append(
            f'<li><a href="#{section_id}">{escape_html(section["title"])}</a></li>'
        )

        subsections_html = []
        for subsection in section['subsections']:
            parts = []
            if 'content' in subsection:
                for para in subsection['content']:
                    parts.append(f'<p>{escape_html(para)}</p>')
            if 'list_items' in subsection:
                items = ''.join(
                    f'<li>{escape_html(item)}</li>' for item in subsection['list_items']
                )
                parts.append(f'<ul>{items}</ul>')
            if 'content_after' in subsection:
                for para in subsection['content_after']:
                    parts.append(f'<p>{escape_html(para)}</p>')
            if 'list_items_2' in subsection:
                items = ''.join(
                    f'<li>{escape_html(item)}</li>' for item in subsection['list_items_2']
                )
                parts.append(f'<ul>{items}</ul>')

            subsections_html.append(
                f'<div class="subsection">'
                f'<h3>{escape_html(subsection["heading"])}</h3>'
                f'{"".join(parts)}'
                f'</div>'
            )

        sections_html.append(
            f'<section id="{section_id}" class="section">'
            f'<h2>{escape_html(section["title"])}</h2>'
            f'{"".join(subsections_html)}'
            f'</section>'
        )

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{escape_html(notes['title'])}</title>
<style>
  :root {{
    --primary: #1c4587;
    --primary-light: #2c5f8d;
    --accent: #e8f0f8;
    --bg: #f5f7fa;
    --card: #ffffff;
    --text: #333333;
    --text-light: #666666;
    --border: #d0d7de;
    --sidebar-width: 280px;
  }}
  *, *::before, *::after {{ box-sizing: border-box; margin: 0; padding: 0; }}
  html {{ scroll-behavior: smooth; }}
  body {{
    font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    color: var(--text);
    background: var(--bg);
    line-height: 1.7;
  }}

  /* Sidebar Navigation */
  .sidebar {{
    position: fixed;
    top: 0; left: 0;
    width: var(--sidebar-width);
    height: 100vh;
    background: var(--primary);
    color: #fff;
    overflow-y: auto;
    padding: 24px 0;
    z-index: 100;
  }}
  .sidebar h2 {{
    font-size: 16px;
    padding: 0 20px 16px;
    border-bottom: 1px solid rgba(255,255,255,0.15);
    margin-bottom: 8px;
  }}
  .sidebar ul {{ list-style: none; }}
  .sidebar li a {{
    display: block;
    padding: 10px 20px;
    color: rgba(255,255,255,0.85);
    text-decoration: none;
    font-size: 14px;
    transition: background 0.2s, color 0.2s;
  }}
  .sidebar li a:hover,
  .sidebar li a:focus {{
    background: rgba(255,255,255,0.1);
    color: #fff;
  }}

  /* Main content */
  .main {{
    margin-left: var(--sidebar-width);
    padding: 0 40px 60px;
  }}

  /* Hero */
  .hero {{
    text-align: center;
    padding: 60px 20px 40px;
    background: linear-gradient(135deg, var(--primary) 0%, var(--primary-light) 100%);
    color: #fff;
    margin: 0 -40px 40px;
  }}
  .hero h1 {{ font-size: 2.4rem; margin-bottom: 12px; }}
  .hero p {{ font-size: 1.1rem; opacity: 0.9; }}
  .hero .meta {{ margin-top: 18px; font-size: 0.9rem; opacity: 0.75; }}

  /* Sections */
  .section {{
    background: var(--card);
    border: 1px solid var(--border);
    border-radius: 12px;
    padding: 32px 36px;
    margin-bottom: 32px;
    box-shadow: 0 1px 3px rgba(0,0,0,0.06);
  }}
  .section h2 {{
    font-size: 1.5rem;
    color: var(--primary);
    border-bottom: 3px solid var(--accent);
    padding-bottom: 10px;
    margin-bottom: 24px;
  }}
  .subsection {{ margin-bottom: 24px; }}
  .subsection h3 {{
    font-size: 1.15rem;
    color: var(--primary-light);
    margin-bottom: 10px;
  }}
  .subsection p {{
    margin-bottom: 10px;
    text-align: justify;
  }}
  .subsection ul {{
    padding-left: 24px;
    margin-bottom: 12px;
  }}
  .subsection li {{
    margin-bottom: 6px;
  }}

  /* Footer */
  .footer {{
    text-align: center;
    padding: 32px 20px;
    color: var(--text-light);
    font-size: 0.9rem;
  }}
  .footer a {{ color: var(--primary); text-decoration: none; }}
  .footer a:hover {{ text-decoration: underline; }}

  /* Mobile toggle */
  .menu-toggle {{
    display: none;
    position: fixed;
    top: 12px; left: 12px;
    z-index: 200;
    background: var(--primary);
    color: #fff;
    border: none;
    border-radius: 6px;
    padding: 8px 14px;
    font-size: 1.2rem;
    cursor: pointer;
  }}

  /* Responsive */
  @media (max-width: 768px) {{
    .menu-toggle {{ display: block; }}
    .sidebar {{
      transform: translateX(-100%);
      transition: transform 0.3s ease;
    }}
    .sidebar.open {{ transform: translateX(0); }}
    .main {{ margin-left: 0; padding: 0 16px 40px; }}
    .hero {{ margin: 0 -16px 24px; padding: 48px 16px 32px; }}
    .hero h1 {{ font-size: 1.8rem; }}
    .section {{ padding: 20px; }}
  }}
</style>
</head>
<body>

<button class="menu-toggle" id="menuToggle" aria-label="Toggle navigation">&#9776;</button>

<nav class="sidebar" id="sidebar">
  <h2>&#128218; Table of Contents</h2>
  <ul>
    {''.join(nav_items)}
  </ul>
</nav>

<div class="main">
  <div class="hero">
    <h1>{escape_html(notes['title'])}</h1>
    <p>{escape_html(notes['subtitle'])}</p>
    <div class="meta">Generated: {datetime.now().strftime('%B %d, %Y')} &bull; Based on Khan Academy Curriculum</div>
  </div>

  {''.join(sections_html)}

  <div class="footer">
    <p>End of Notes &mdash; For more information and interactive lessons, visit
      <a href="https://www.khanacademy.org" target="_blank" rel="noopener">Khan Academy</a>
    </p>
  </div>
</div>

<script>
  document.getElementById('menuToggle').addEventListener('click', function() {{
    document.getElementById('sidebar').classList.toggle('open');
  }});
  document.addEventListener('keydown', function(e) {{
    if (e.key === 'Escape') {{
      document.getElementById('sidebar').classList.remove('open');
    }}
  }});
  document.querySelectorAll('.sidebar a').forEach(function(link) {{
    link.addEventListener('click', function() {{
      document.getElementById('sidebar').classList.remove('open');
    }});
  }});
</script>
</body>
</html>"""

    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"✓ HTML website successfully created: {output_file}")


def main():
    """Main function"""
    output_file = "/mnt/user-data/outputs/khan_academy_computers_comprehensive_notes.pdf"
    html_output_file = "/mnt/user-data/outputs/khan_academy_computers_comprehensive_notes.html"
    
    print("=" * 70)
    print("Khan Academy - Computers: Comprehensive Study Notes Generator")
    print("=" * 70)
    print()
    
    create_pdf(output_file)
    create_html(html_output_file)
    
    print()
    print("=" * 70)
    print("SUCCESS! Your comprehensive study notes are ready!")
    print("=" * 70)
    print()
    print("The output includes detailed coverage of:")
    print("  • What is a Computer?")
    print("  • Digital Information & Binary")
    print("  • Computer Hardware Components")
    print("  • Information Processing")
    print("  • Software & Operating Systems")
    print("  • Networks & the Internet")
    print("  • Algorithms & Problem Solving")
    print("  • Data Representation")
    print("  • Computing History & Future")
    print()


if __name__ == "__main__":
    main()
