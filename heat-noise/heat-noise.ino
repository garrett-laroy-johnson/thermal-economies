
#include <Wire.h>
#include <Adafruit_AMG88xx.h>

Adafruit_AMG88xx amg;

float average2 = 0.0;
float pixels[AMG88xx_PIXEL_ARRAY_SIZE];
float average1 = 0.0;
float delta = 0.0;
float dif = 0.0;
float amp = 0.0;
float sum = 0.0;

#include <Audio.h>
#include <Wire.h>
#include <SPI.h>
#include <SD.h>
#include <SerialFlash.h>
#include <Adafruit_AMG88xx.h>


// GUItool: begin automatically generated code
AudioSynthNoisePink     noise1;         //xy=308,223
AudioOutputAnalog        dac1;           //xy=541,362
AudioConnection          patchCord1(noise1, dac1);

// GUItool: end automatically generated code


void setup() {
  // put your setup code here, to run once:
  // put your setup code here, to run once:
  AudioMemory(10);
  Serial.begin(115200);
  Serial.println(F("AMG88xx pixels"));

  bool status;

  // default settings
  status = amg.begin();
  if (!status) {
    Serial.println("Could not find a valid AMG88xx sensor, check wiring!");
    while (1);
  }

  Serial.println("-- Thermal Camera Test --");
  delay(100); // let sensor boot up

}

void loop() {

  //read all the pixels
  amg.readPixels(pixels);
  float sum = 0.0;
  for (int i = 1; i <= AMG88xx_PIXEL_ARRAY_SIZE; i++) {
    sum = pixels[i - 1] + sum;
  }


  //Serial.println()
  average1 = sum / 64.;
  dif = average1 - average2;
  delta = abs(dif);
  average1 = average2;
  Serial.println(delta);


  amp = (delta - 20.) / 15.;
  noise1.amplitude(amp);

  //delay
  delay(1);

}
