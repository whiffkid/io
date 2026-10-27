import streamlit as st

# Configure the page
st.set_page_config(page_title="Lab Exam Codes", layout="centered")

st.title("📝 Lab Exam Code Reference")
st.write("Use the tabs below to view and copy the code for your lab exam.")

# Create tabs for the three codes
tab1, tab2, tab3 = st.tabs(["1. Voltage Monitor", "2. Matrix Keypad", "3. RPi LED Control"])

with tab1:
    st.header("Arduino Voltage Monitor")
    voltage_code = """#define v_pin A0
#define led_pin 13

const float R1=10000.0;
const float R2=10000.0;

const float VREF=5.0;
const float low_amp=7.0;

void setup(){
  pinMode(led_pin,OUTPUT);
  Serial.begin(9600);
}

void loop(){
  float absValue=analogRead(v_pin);
  float v_A0= (absValue*VREF)/1023.0;
  float v_battery= v_A0*((R1+R2)/R2);

  Serial.print("ADC Value");
  Serial.println(absValue);

  Serial.print("Battery voltage:");
  Serial.print(v_battery);
  Serial.println(" V");

  if(v_battery<low_amp){
    digitalWrite(led_pin,HIGH);
    Serial.println("LOW VOLTAGE");
  }
  else{
    digitalWrite(led_pin,LOW);
    Serial.println("NORMAL VOLTAGE");
  }
  delay(1000);
}"""
    st.code(voltage_code, language='cpp')

with tab2:
    st.header("Arduino Matrix Keypad")
    keypad_code = """#include<Keypad.h>

const byte ROWS=4;
const byte COLS=4;

char keys[ROWS][COLS]={
  {'1','2','3','A'},
  {'4','5','6','B'},
  {'7','8','9','C'},
  {'*','0','#','D'}
};

byte rowPins[ROWS]={9,8,7,6};
byte colPins[COLS]={A0,A1,A2,A3};

Keypad keypad=Keypad(makeKeymap(keys),rowPins,colPins,ROWS,COLS);

String input ="";

void setup(){
  Serial.begin(9600);
  Serial.println("MATRIX KEYPAD");
  delay(1000);
}

void loop(){
  char key=keypad.getKey();
  if (key){
    if(key=='#'){
      input="";
      Serial.println("Input cleared");
      Serial.println("Enter:");
    }
    else if(key=='*'){
      if(input.length()>0){
        input.remove(input.length()-1);
      }
    }
    else{
      input+=key;
      Serial.println("key pressed:");
      Serial.println(key);

      Serial.println("Input");
      Serial.println(input);
    }
  }
}"""
    st.code(keypad_code, language='cpp')

with tab3:
    st.header("Raspberry Pi LED Control")
    rpi_code = """import RPi.GPIO as GPIO

LED=17
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED,GPIO.OUT)

try:
  while True:
    command=input("1,0,q")
    if command=='1':
      GPIO.output(LED,GPIO.HIGH)
      print("LED ON")
    elif command=='0':
      GPIO.output(LED,GPIO.LOW)
      print("LED OFF")
    else:
      break
except KeyboardInterrupt:
    print("\\nProgram down")
finally:
  GPIO.output(LED,GPIO.LOW)
  GPIO.cleanup()"""
    st.code(rpi_code, language='python')
