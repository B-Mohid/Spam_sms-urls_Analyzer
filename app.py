import streamlit as st
from streamlit.components.v1 import html

# Set page configuration for a wide, modern layout
st.set_page_config(layout="wide", page_title="Privacy-First URL Spam Classifier")

# The complete, self-contained HTML for the client-side application
# This includes Tailwind CSS, TensorFlow.js, and all UI/logic
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Privacy-First URL Spam Classifier</title>
    <!-- Tailwind CSS from CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- TensorFlow.js from CDN -->
    <script src="https://cdn.jsdelivr.net/npm/@tensorflow/tfjs@4.11.0/dist/tf.min.js"></script>
    <!-- Google Fonts: Inter -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
    <style>
        /* Custom styles for a polished look */
        body {
            font-family: 'Inter', sans-serif;
        }
        .section {
            display: none; /* Hide sections by default */
        }
        .section.active {
            display: block; /* Show active section */
        }
        /* Custom scrollbar for a better look */
        ::-webkit-scrollbar { width: 8px; }
        ::-webkit-scrollbar-track { background: #1a202c; }
        ::-webkit-scrollbar-thumb { background: #4a5568; border-radius: 4px; }
        ::-webkit-scrollbar-thumb:hover { background: #718096; }
    </style>
</head>
<body class="bg-gray-900 text-gray-200 flex min-h-screen">

    <!-- Sidebar Navigation -->
    <aside class="w-64 bg-gray-900/80 backdrop-blur-sm p-6 border-r border-gray-700 flex flex-col fixed h-full">
        <div class="flex items-center gap-3 mb-10">
            <svg class="w-8 h-8 text-indigo-400" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor">
                <path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75m-3-7.036A11.959 11.959 0 013.598 6 11.99 11.99 0 003 9.749c0 5.592 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.31-.21-2.571-.598-3.751h-.152c-3.196 0-6.1-1.248-8.25-3.286zm0 13.036h.008v.008h-.008v-.008z" />
            </svg>
            <h1 class="text-xl font-bold text-white">URL Shield</h1>
        </div>
        <nav>
            <ul class="space-y-2">
                <li>
                    <a href="#" class="nav-link active flex items-center gap-3 px-4 py-2 rounded-lg text-gray-300 hover:bg-indigo-500 hover:text-white transition-all" data-target="analyzer">
                        <svg class="w-5 h-5" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z" /></svg>
                        Analyzer
                    </a>
                </li>
                <li>
                    <a href="#" class="nav-link flex items-center gap-3 px-4 py-2 rounded-lg text-gray-300 hover:bg-indigo-500 hover:text-white transition-all" data-target="about">
                       <svg class="w-5 h-5" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M11.25 11.25l.041-.02a.75.75 0 011.063.852l-.708 2.836a.75.75 0 001.063.853l.041-.021M21 12a9 9 0 11-18 0 9 9 0 0118 0zm-9-3.75h.008v.008H12V8.25z" /></svg>
                        About
                    </a>
                </li>
            </ul>
        </nav>
        <div id="modelStatus" class="mt-auto text-center text-sm p-3 bg-gray-800 rounded-lg flex items-center justify-center gap-2">
            <div class="loader"></div>
            <span>Loading AI Model...</span>
        </div>
    </aside>

    <!-- Main Content -->
    <main class="ml-64 flex-1 p-8">
        <!-- Analyzer Section -->
        <div id="analyzer" class="section active">
            <div class="max-w-3xl mx-auto">
                <h2 class="text-3xl font-bold text-white mb-2">URL Spam Analyzer</h2>
                <p class="text-gray-400 mb-8">Enter a URL to analyze it for potential spam or malicious content. The analysis is done entirely in your browser; your data never leaves your computer.</p>
                
                <div class="bg-gray-800/50 p-6 rounded-xl border border-gray-700">
                    <div class="relative">
                         <textarea id="urlInput" class="w-full bg-gray-800 border border-gray-600 rounded-lg p-4 pr-24 text-gray-200 focus:ring-2 focus:ring-indigo-500 focus:outline-none transition resize-none" rows="3" placeholder="https://... or http://..."></textarea>
                         <button id="pasteButton" class="absolute top-3 right-3 text-sm bg-gray-700 hover:bg-gray-600 text-gray-300 font-medium py-1 px-3 rounded-md transition">Paste</button>
                    </div>
                   
                    <button id="analyzeButton" class="w-full mt-4 bg-indigo-600 text-white font-bold py-3 px-4 rounded-lg hover:bg-indigo-700 transition-all disabled:bg-gray-600 disabled:cursor-not-allowed flex items-center justify-center gap-2" disabled>
                        <svg class="w-5 h-5" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75m-3-7.036A11.959 11.959 0 013.598 6 11.99 11.99 0 003 9.749c0 5.592 3.824 10.29 9 11.622 5.176-1.332 9-6.03 9-11.622 0-1.31-.21-2.571-.598-3.751h-.152c-3.196 0-6.1-1.248-8.25-3.286zm0 13.036h.008v.008h-.008v-.008z" /></svg>
                        <span>Analyze URL</span>
                    </button>
                </div>

                <!-- Result Display -->
                <div id="result" class="mt-8 hidden">
                    <h3 class="text-lg font-semibold text-white mb-4">Analysis Result</h3>
                    <div id="resultCard" class="p-6 rounded-xl border">
                        <div class="flex items-center justify-between mb-4">
                            <span id="resultLabel" class="text-2xl font-bold"></span>
                            <span id="resultScore" class="text-xl font-mono px-3 py-1 rounded-md"></span>
                        </div>
                        <div class="w-full bg-gray-700 rounded-full h-2.5">
                            <div id="resultBar" class="h-2.5 rounded-full transition-all duration-500" style="width: 0%"></div>
                        </div>
                    </div>
                </div>
            </div>
        </div>

        <!-- About Section -->
        <div id="about" class="section">
             <div class="max-w-3xl mx-auto">
                <h2 class="text-3xl font-bold text-white mb-4">About This Application</h2>
                <div class="space-y-6 text-gray-300 leading-relaxed">
                    <p><strong>URL Shield</strong> is a privacy-focused tool designed to help you identify potentially harmful, spam, or malicious URLs without compromising your privacy.</p>
                    <h3 class="text-xl font-semibold text-white border-b border-gray-700 pb-2">How It Works</h3>
                    <p>Unlike traditional online scanners that require you to submit data to a server, this application leverages the power of TensorFlow.js to run a sophisticated AI model directly within your web browser. Here's the process:</p>
                    <ol class="list-decimal list-inside space-y-2 pl-4">
                        <li><strong>Model Loading:</strong> When you open this page, the pre-trained neural network and its associated files are downloaded to your browser.</li>
                        <li><strong>Client-Side Processing:</strong> When you enter a URL and click "Analyze", the URL is tokenized (converted into numbers) and fed into the AI model right on your device.</li>
                        <li><strong>Instant Analysis:</strong> The model processes the data and outputs a prediction, indicating the likelihood that the URL is spam.</li>
                    </ol>
                    <h3 class="text-xl font-semibold text-white border-b border-gray-700 pb-2">Your Privacy is Paramount</h3>
                    <p>Because the entire analysis happens on your computer (client-side), the URLs you test are never sent across the internet to any server. Your activity remains completely private and anonymous. This is the core principle behind the application's design.</p>
                     <h3 class="text-xl font-semibold text-white border-b border-gray-700 pb-2">The AI Model</h3>
                    <p>The model was trained on a large dataset of both benign and malicious URLs. It learned to recognize patterns and characteristics common in spam links, using a character-level tokenization approach to understand the structure of the URL text itself.</p>
                </div>
            </div>
        </div>
    </main>

    <script>
        // --- MODEL & UI CONSTANTS ---
        const MAX_LEN = 200;
        const MODEL_JSON_URL = '/static/model.json';
        const CHAR_INDEX_URL = '/static/char_index.json';

        // --- DOM ELEMENTS ---
        const urlInput = document.getElementById('urlInput');
        const analyzeButton = document.getElementById('analyzeButton');
        const pasteButton = document.getElementById('pasteButton');
        const modelStatus = document.getElementById('modelStatus');
        const resultDiv = document.getElementById('result');
        const resultCard = document.getElementById('resultCard');
        const resultLabel = document.getElementById('resultLabel');
        const resultScore = document.getElementById('resultScore');
        const resultBar = document.getElementById('resultBar');
        const navLinks = document.querySelectorAll('.nav-link');
        const sections = document.querySelectorAll('.section');

        // --- APP STATE ---
        let model = null;
        let charIndex = null;
        
        // --- PREPROCESSING LOGIC ---
        function preprocessUrl(url, charIndex, maxLength) {
            // 1. Character to Integer Mapping
            let sequence = url.split('').map(char => {
                return charIndex[char] || 0; // Use 0 for unknown characters (out-of-vocabulary)
            });

            // 2. Padding / Truncating
            if (sequence.length > maxLength) {
                sequence = sequence.slice(0, maxLength); // Truncate
            } else {
                const padding = Array(maxLength - sequence.length).fill(0);
                sequence = padding.concat(sequence); // Pad at the beginning
            }
            return sequence;
        }

        // --- PREDICTION LOGIC ---
        async function analyzeUrl() {
            const url = urlInput.value.trim();
            if (!url) {
                alert("Please enter a URL to analyze.");
                return;
            }

            // Preprocess the URL
            const sequence = preprocessUrl(url, charIndex, MAX_LEN);
            const tensor = tf.tensor2d([sequence]);

            // Make prediction
            try {
                const prediction = model.predict(tensor);
                const score = prediction.dataSync()[0];
                displayResult(score);
            } catch (error) {
                console.error("Error during prediction:", error);
                alert("An error occurred during analysis. Please check the console.");
            } finally {
                tensor.dispose(); // Clean up tensor memory
            }
        }

        // --- UI UPDATE LOGIC ---
        function displayResult(score) {
            const isSpam = score > 0.5;
            const confidence = isSpam ? score : 1 - score;
            const percentage = (confidence * 100).toFixed(2);

            resultDiv.classList.remove('hidden');

            if (isSpam) {
                resultLabel.textContent = "Likely Spam";
                resultLabel.className = "text-2xl font-bold text-red-400";
                resultCard.className = "p-6 rounded-xl border border-red-500/50 bg-red-500/10";
                resultScore.className = "text-xl font-mono px-3 py-1 rounded-md bg-red-500/20 text-red-300";
                resultBar.className = "h-2.5 rounded-full transition-all duration-500 bg-red-500";
            } else {
                resultLabel.textContent = "Likely Safe";
                resultLabel.className = "text-2xl font-bold text-green-400";
                resultCard.className = "p-6 rounded-xl border border-green-500/50 bg-green-500/10";
                resultScore.className = "text-xl font-mono px-3 py-1 rounded-md bg-green-500/20 text-green-300";
                resultBar.className = "h-2.5 rounded-full transition-all duration-500 bg-green-500";
            }
            resultScore.textContent = `${percentage}%`;
            
            // Set timeout to allow the element to be visible before transition
            setTimeout(() => {
                resultBar.style.width = `${percentage}%`;
            }, 100);
        }

        function setupNavigation() {
            navLinks.forEach(link => {
                link.addEventListener('click', (e) => {
                    e.preventDefault();
                    const targetId = link.getAttribute('data-target');

                    // Update active link
                    navLinks.forEach(l => l.classList.remove('active', 'bg-indigo-600', 'text-white'));
                    link.classList.add('active', 'bg-indigo-600', 'text-white');

                    // Update active section
                    sections.forEach(section => {
                        if (section.id === targetId) {
                            section.classList.add('active');
                        } else {
                            section.classList.remove('active');
                        }
                    });
                });
            });
        }

        // --- MAIN INITIALIZATION ---
        async function main() {
            try {
                // Load model and char index in parallel
                const [loadedModel, charIndexResponse] = await Promise.all([
                    tf.loadLayersModel(MODEL_JSON_URL),
                    fetch(CHAR_INDEX_URL)
                ]);
                model = loadedModel;
                charIndex = await charIndexResponse.json();

                // Update UI to reflect loaded state
                modelStatus.innerHTML = `
                    <svg class="w-5 h-5 text-green-400" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M9 12.75L11.25 15 15 9.75M21 12a9 9 0 11-18 0 9 9 0 0118 0z" /></svg>
                    <span>Model Ready</span>
                `;
                modelStatus.classList.replace('bg-gray-800', 'bg-green-500/20');
                analyzeButton.disabled = false;
                analyzeButton.querySelector('span').textContent = 'Analyze URL';

            } catch (error) {
                console.error('Failed to load model or char index:', error);
                modelStatus.innerHTML = `
                    <svg class="w-5 h-5 text-red-400" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor"><path stroke-linecap="round" stroke-linejoin="round" d="M12 9v3.75m9-.75a9 9 0 11-18 0 9 9 0 0118 0zm-9 3.75h.008v.008H12v-.008z" /></svg>
                    <span>Model Failed to Load</span>
                `;
                modelStatus.classList.replace('bg-gray-800', 'bg-red-500/20');
                alert("Could not load the AI model. Please check the console and ensure model files are in the 'static' directory.");
            }
        }

        // --- EVENT LISTENERS ---
        analyzeButton.addEventListener('click', analyzeUrl);
        pasteButton.addEventListener('click', async () => {
            try {
                const text = await navigator.clipboard.readText();
                urlInput.value = text;
            } catch (err) {
                console.error('Failed to read clipboard contents: ', err);
                alert('Could not paste from clipboard. Please paste manually.');
            }
        });
        
        // --- STARTUP ---
        setupNavigation();
        main();

    </script>
</body>
</html>
"""

# Render the HTML in the Streamlit app
html(html_template, height=1024, scrolling=True)
