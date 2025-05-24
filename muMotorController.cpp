#include "MotorController.h"
#include <iostream>

class EmuMotorController : public MotorController {
public:
    void setSpeed(float left, float right) override {
        std::cout << "[EMU] Motors: L=" << left*100 << "% R=" << right*100 << "%\n";
    }
};
