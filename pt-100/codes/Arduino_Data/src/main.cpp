#include "Arduino.h"
#include <LiquidCrystal.h>

int rs =7;
int en = 8; 
int d4 = 9;
int d5 = 10;
int d6 = 11;
int d7 = 12;

LiquidCrystal lcd(rs,en,d4,d5,d6,d7);

double linear_regression(double v)
{
	// values obtained from Linear regression python code
	return (v - 1.5875)/ 0.00375;
}

void setup() 
{ 
	lcd.begin(16,2); // 16 coloumns, 2rows display
	Serial.begin(9600);
}

void loop() 
{ 
	int sensorValue = analogRead(A0);
	double voltage = (5*sensorValue/1024.0);
	double temper = linear_regression(voltage);
	Serial.println(voltage);

	lcd.setCursor(0,0);
	lcd.print("Temperature: ");

	lcd.setCursor(0,1);
	lcd.print(temper, 3);
	delay(1000);
	lcd.clear();
}
