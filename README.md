# Python implementation of 2048

Simple open-source python implementation of 2048 game.

## Description

This copy of 2048 game has two sides, front and engine. The front side is made on top of my own [Game](https://github.com/Gantulga9480/Game.git) module responsible for rendering the game. The engine computes and manipulates the state and logic of the game. The engine can be used without the front side.

## Getting Started

### Dependencies

- Properly installed python interpreter.

### Installing

    pip install git+https://github.com/Gantulga9480/py2048.git#egg=py2048

or directly download from [releases](https://github.com/Gantulga9480/py2048/releases) for more stable release

### Executing program

Copy and past the following code and run.

    from py2048 import Py2048
    g = Py2048()
    g.loop_forever()

## Authors

Contributors names and contact info

GitHub - [Gantulga G](https://github.com/Gantulga9480)
Email  - limited.tulgaa@gmail.com

## Change log

#### v1.0.4 - 2023/09/07
- Game module added as git submodule
- engine.reset method added
- py2048.reset method added

#### v1.0.3
- Base Game module upgraded to v2s

#### v1.0.2
- Base Game module included in py2048 module

#### v1.0.1
- Base game updated to 1.1.0.

#### v1.0.0
- Project published.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments

* [RL 2048 project](https://github.com/Gantulga9480/RL-2048.git)
* [Game](https://github.com/Gantulga9480/Game.git)