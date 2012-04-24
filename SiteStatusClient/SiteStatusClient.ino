const int pinGood = 12;
const int pinBad = 11;
const int pinNotStarted = 13;

int ledState = LOW;
int ledState2 = HIGH;
long previousMillis = 0;
long interval = 500;
boolean siteIsUp = false;
boolean started = false;
char inByte;

void setup() {
  Serial.begin(9600);
  
  pinMode(pinGood, OUTPUT);
  pinMode(pinBad, OUTPUT); 
  pinMode(pinNotStarted, OUTPUT);   
}

void allOff() {
  digitalWrite(pinGood, LOW);
  digitalWrite(pinBad, LOW);
  digitalWrite(pinNotStarted, LOW); 
}

void blinkOne(int pin) {
  allOff();
  digitalWrite(pin, HIGH);
  delay(100);
}

void loop()
{
  if (Serial.available() > 0) {
    started = true;
    inByte = Serial.read();
    siteIsUp = inByte != '0';
//    Serial.println(inByte);
  }
    
  if(!started) {
    blinkOne(pinGood);
    blinkOne(pinBad);
    blinkOne(pinNotStarted);
  } else {    
    if(siteIsUp) {
      allOff();
      digitalWrite(pinGood, HIGH);
    } else {
      unsigned long currentMillis = millis();
     
      if(currentMillis - previousMillis > interval) {
        allOff();
        previousMillis = currentMillis;   
        ledState = ledState == LOW ? HIGH : LOW;
        ledState2 = ledState2 == LOW ? HIGH : LOW;
        digitalWrite(pinBad, ledState);
        digitalWrite(pinNotStarted, ledState2);
      }
    }
  }
}

