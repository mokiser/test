#pragma once

class MotorController {
public:
    virtual ~MotorController() = default;
    virtual void setSpeed(float left, float right) = 0;
    virtual void emergencyStop() { setSpeed(0, 0); }
};
