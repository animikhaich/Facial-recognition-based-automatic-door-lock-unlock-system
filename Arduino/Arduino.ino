int motorPin_1 = 10;
int motorPin_2 = 11;
int indicatorLED = 13;
int sensePin = 8;
int delay_ms = 1500;

void setup()
{
    pinMode(motorPin_1,OUTPUT);
    pinMode(motorPin_2,OUTPUT);
    pinMode(indicatorLED,OUTPUT);
    Serial.begin(9600);
}

void loop()
{   // Wait for serial connection to be initialied from the PC
    while(Serial.available())
    {        
      if  (Serial.read() == '1')  // When '1' is received, turn motor clockwise
        {
          digitalWrite(motorPin_1, HIGH);
          digitalWrite(motorPin_2, LOW);
          digitalWrite(indicatorLED, HIGH);
          delay(delay_ms);
          digitalWrite(motorPin_1, LOW);
          digitalWrite(motorPin_2, LOW);
          delay(delay_ms);
          digitalWrite(motorPin_1, LOW);
          digitalWrite(motorPin_2, HIGH);
          delay(delay_ms);
          digitalWrite(motorPin_1, LOW);
          digitalWrite(motorPin_2, LOW);
        }
    }
}

