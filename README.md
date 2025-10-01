# Set Up Training

- Find the voice you plan to train using [voices]: https://github.com/OHF-Voice/piper1-gpl/blob/main/docs/VOICES.md
- Make sure you download the wav files (put the files in their own folder called wavs) AND their associated metadata.csv file so that the trainer has phonetics to reference
- Put the wavs folder AND metadata.csv file inside the corpus directory
- once inside corpus, run the piper_files_from_corpus.py python file to make sure all files are the correct format.

# How to use run_training.sh

- First activate your enviorment: `source venv311/bin/activate`
- then run the training script `source ./run_training.sh`

---

Extra piper repo information

![Piper](etc/logo.png)

A fast and local neural text-to-speech engine that embeds [espeak-ng][] for phonemization.

Install with:

```sh
pip install piper-tts
```

- 🎧 [Samples][samples]
- 💡 [Demo][demo]
- 🗣️ [Voices][voices]
- 🖥️ [Command-line interface][cli]
- 🌐 [Web server][api-http]
- 🐍 [Python API][api-python]
- 🔧 [C/C++ API][libpiper]
- 🏋️ [Training new voices][training]
- 🛠️ [Building manually][building]

---

People/projects using Piper:

- [Home Assistant](https://github.com/home-assistant/addons/blob/master/piper/README.md)
- [NVDA - NonVisual Desktop Access](https://www.nvaccess.org/post/in-process-8th-may-2023/#voices)
- [Image Captioning for the Visually Impaired and Blind: A Recipe for Low-Resource Languages](https://www.techrxiv.org/articles/preprint/Image_Captioning_for_the_Visually_Impaired_and_Blind_A_Recipe_for_Low-Resource_Languages/22133894)
- [Video tutorial by Thorsten Müller](https://youtu.be/rjq5eZoWWSo)
- [Open Voice Operating System](https://github.com/OpenVoiceOS/ovos-tts-plugin-piper)
- [JetsonGPT](https://github.com/shahizat/jetsonGPT)
- [LocalAI](https://github.com/go-skynet/LocalAI)
- [Lernstick EDU / EXAM: reading clipboard content aloud with language detection](https://lernstick.ch/)
- [Natural Speech - A plugin for Runelite, an OSRS Client](https://github.com/phyce/rl-natural-speech)
- [mintPiper](https://github.com/evuraan/mintPiper)
- [Vim-Piper](https://github.com/wolandark/vim-piper)
- [POTaTOS](https://www.youtube.com/watch?v=Dz95q6XYjwY)
- [Narration Studio](https://github.com/phyce/Narration-Studio)
- [Basic TTS](https://basictts.com/) - Simple online text-to-speech converter.

[![A library from the Open Home Foundation](https://www.openhomefoundation.org/badges/ohf-library.png)](https://www.openhomefoundation.org/)

<!-- Links -->

[espeak-ng]: https://github.com/espeak-ng/espeak-ng
[cli]: https://github.com/OHF-Voice/piper1-gpl/blob/main/docs/CLI.md
[api-http]: https://github.com/OHF-Voice/piper1-gpl/blob/main/docs/API_HTTP.md
[api-python]: https://github.com/OHF-Voice/piper1-gpl/blob/main/docs/API_PYTHON.md
[training]: https://github.com/OHF-Voice/piper1-gpl/blob/main/docs/TRAINING.md
[building]: https://github.com/OHF-Voice/piper1-gpl/blob/main/docs/BUILDING.md
[voices]: https://github.com/OHF-Voice/piper1-gpl/blob/main/docs/VOICES.md
[samples]: https://rhasspy.github.io/piper-samples
[demo]: https://rhasspy.github.io/piper-samples/demo.html
[libpiper]: https://github.com/OHF-Voice/piper1-gpl/tree/main/libpiper
