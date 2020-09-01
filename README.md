# Dino Machine Learning

<p align="center">
<img src="dino.gif">
</p>

A simple example how to teach Google Chrome's offline dinosaur to jump over obstacles using methods of machine learning (if you want "to make dino run by artificial intelligence"). It uses multiple methods such as Neural Networks and a simple Genetic Algorithm. These algorithms are written from scratch in vanilla Python primary by [utay](https://github.com/utay/dino-ml), which means that no external machine learning libraries were used.

# Usage / Prerequisites

* Python
* Install dependencies (tested on Windows only)
* 'screenshot.exe' utility is used inside "dino-ml" folder to make screenshots of a game
    - This utility could be used for this purpose - https://github.com/vdmitriyev/screenshot-cmd
* To start "dino game" in the Chrome Browser (and still have your Internet access) use following:
    - ```chrome://dino/```
* It uses only part of the screenshots (hardcoded ones), this why you will need to change "which" parts of the screen have to "screened" by utility (see ```scanner.py```)
* See the section with "Run & Learn"


## Run & Learn

* Install dependencies: `pip install -r requirements.txt`
* Open Chrome's dinosaur game and put aside the terminal (make sure that the screenshot utility makes proper screenshots of the screen with game on it)
    - Option 0: Disable your Internet connection :)
    - Option 1: Open in Chrome Browser following tab - ```chrome://dino/```
    - Option 2: Go to developer tools , and under network, set to offline
* Run the AI: `python ai.py`
* After 5/8 generations, the dino should be a ninja!

## Credentials

* An initial Python version comes from here and done by [utayh](https://github.com/utay]- [https://github.com/utay/dino-ml](https://github.com/utay/dino-ml)
* Initial idea - inspired by [https://github.com/ivanseidel/IAMDinosaur](https://github.com/ivanseidel/IAMDinosaur)

## TODO

- [ ] Find game automatically in the screen at the beginning
- [ ] Make it crossplatform (so far the pressed keyboard keys are for MacOS)
- [ ] Handle key down (some obstacles can't be jumped)
- [ ] Handle day *and* night
- [ ] Take obstacle height into account

## License

To be defined
