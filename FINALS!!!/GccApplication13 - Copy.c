#define F_CPU 14745600
#include <avr/io.h>
#include <avr/interrupt.h>
#include <util/delay.h>

volatile unsigned long int ShaftCountLeft = 0; //to keep track of left position encoder
volatile unsigned long int ShaftCountRight = 0; //to keep track of right position encoder
volatile unsigned int Degrees; //to accept angle in degrees for turning
unsigned char data; //to store received data from UDR1

//Function to configure ports to enable robot's motion



void red2led_pin_config (void)
{
 DDRJ = DDRJ | 0x20;		//Setting PORTC 3 as outpt
 PORTJ = PORTJ & 0xDF;		//Setting PORTC 3 logic low to turnoff buzzer
}
void blue2led_pin_config (void)
{
 DDRJ = DDRJ | 0x04;		//Setting PORTC 3 as outpt
 PORTJ = PORTJ & 0xFB;		//Setting PORTC 3 logic low to turnoff buzzer
}
void green2led_pin_config (void)
{
 DDRJ = DDRJ | 0x08;		//Setting PORTC 3 as outpt
 PORTJ = PORTJ & 0xF7;		//Setting PORTC 3 logic low to turnoff buzzer
}



void red1led_pin_config (void)
{
 DDRJ = DDRJ | 0x40;		//Setting PORTC 3 as outpt
 PORTJ = PORTJ & 0xBF;		//Setting PORTC 3 logic low to turnoff buzzer
}
void blue1led_pin_config (void)
{
 DDRJ = DDRJ | 0x80;		//Setting PORTC 3 as outpt
 PORTJ = PORTJ & 0x7F;		//Setting PORTC 3 logic low to turnoff buzzer
}
void green1led_pin_config (void)
{
 DDRJ = DDRJ | 0x10;		//Setting PORTC 3 as outpt
 PORTJ = PORTJ & 0xEF;		//Setting PORTC 3 logic low to turnoff buzzer
}



void buzzer_pin_config (void)
{
 DDRC = DDRC | 0x08;		//Setting PORTC 3 as outpt
 PORTC = PORTC & 0xF7;		//Setting PORTC 3 logic low to turnoff buzzer
}





void motion_pin_config (void)
{
	DDRA = DDRA | 0x0F;
	PORTA = PORTA & 0xF0;
	DDRL = DDRL | 0x18;   //Setting PL3 and PL4 pins as output for PWM generation
	PORTL = PORTL | 0x18; //PL3 and PL4 pins are for velocity control using PWM.
}

//Function to configure INT4 (PORTE 4) pin as input for the left position encoder
void left_encoder_pin_config (void)
{
	DDRE  = DDRE & 0xEF;  //Set the direction of the PORTE 4 pin as input
	PORTE = PORTE | 0x10; //Enable internal pull-up for PORTE 4 pin
}

//Function to configure INT5 (PORTE 5) pin as input for the right position encoder
void right_encoder_pin_config (void)
{
	DDRE  = DDRE & 0xDF;  //Set the direction of the PORTE 4 pin as input
	PORTE = PORTE | 0x20; //Enable internal pull-up for PORTE 4 pin
}

//Function to initialize ports
void port_init()
{
	motion_pin_config(); //robot motion pins config
	left_encoder_pin_config(); //left encoder pin config
	right_encoder_pin_config(); //right encoder pin config
        green1led_pin_config();
        blue1led_pin_config();
        red1led_pin_config();
        green2led_pin_config();
        blue2led_pin_config();
        red2led_pin_config();
	buzzer_pin_config();
}

void left_position_encoder_interrupt_init (void) //Interrupt 4 enable
{
	cli(); //Clears the global interrupt
	EICRB = EICRB | 0x02; // INT4 is set to trigger with falling edge
	EIMSK = EIMSK | 0x10; // Enable Interrupt INT4 for left position encoder
	sei();   // Enables the global interrupt
}

void right_position_encoder_interrupt_init (void) //Interrupt 5 enable
{
	cli(); //Clears the global interrupt
	EICRB = EICRB | 0x08; // INT5 is set to trigger with falling edge
	EIMSK = EIMSK | 0x20; // Enable Interrupt INT5 for right position encoder
	sei();   // Enables the global interrupt
}

//ISR for right position encoder
ISR(INT5_vect)
{
	ShaftCountRight++;  //increment right shaft position count
}


//ISR for left position encoder
ISR(INT4_vect)
{
	ShaftCountLeft++;  //increment left shaft position count
}


//Function used for setting motor's direction
void motion_set (unsigned char Direction)
{
	unsigned char PortARestore = 0;

	Direction &= 0x0F; 		// removing upper nibbel for the protection
	PortARestore = PORTA; 		// reading the PORTA original status
	PortARestore &= 0xF0; 		// making lower direction nibbel to 0
	PortARestore |= Direction; // adding lower nibbel for forward command and restoring the PORTA status
	PORTA = PortARestore; 		// executing the command
}

void forward (void) //both wheels forward
{
	motion_set(0x06);
}

void back (void) //both wheels backward
{
	motion_set(0x09);
}

void left (void) //Left wheel backward, Right wheel forward
{
	motion_set(0x05);
}

void right (void) //Left wheel forward, Right wheel backward
{
	motion_set(0x0A);
}

void soft_left (void) //Left wheel stationary, Right wheel forward
{
	motion_set(0x04);
}

void soft_right (void) //Left wheel forward, Right wheel is stationary
{
	motion_set(0x02);
}

void soft_left_2 (void) //Left wheel backward, right wheel stationary
{
	motion_set(0x01);
}

void soft_right_2 (void) //Left wheel stationary, Right wheel backward
{
	motion_set(0x08);
}

void stop (void)
{
	motion_set(0x00);
}


//Function used for turning robot by specified degrees
void angle_rotate(unsigned int Degrees)
{
	float ReqdShaftCount = 0;
	unsigned long int ReqdShaftCountInt = 0;

	ReqdShaftCount = (float) Degrees/ 4.090; // division by resolution to get shaft count
	ReqdShaftCountInt = (unsigned int) ReqdShaftCount;
	ShaftCountRight = 0;
	ShaftCountLeft = 0;

	while (1)
	{
		if((ShaftCountRight >= ReqdShaftCountInt) | (ShaftCountLeft >= ReqdShaftCountInt))
		break;
	}
	stop(); //Stop robot
}

//Function used for moving robot forward by specified distance

void linear_distance_mm(unsigned int DistanceInMM)
{
	float ReqdShaftCount = 0;
	unsigned long int ReqdShaftCountInt = 0;

	ReqdShaftCount = DistanceInMM / 5.338; // division by resolution to get shaft count
	ReqdShaftCountInt = (unsigned long int) ReqdShaftCount;
	
	ShaftCountRight = 0;
	while(1)
	{
		if(ShaftCountRight > ReqdShaftCountInt)
		{
			break;
		}
	}
	stop(); //Stop robot
}

void forward_mm(unsigned int DistanceInMM)
{
	forward();
	linear_distance_mm(DistanceInMM);
}

void back_mm(unsigned int DistanceInMM)
{
	back();
	linear_distance_mm(DistanceInMM);
}

void left_degrees(unsigned int Degrees)
{
	// 88 pulses for 360 degrees rotation 4.090 degrees per count
	left(); //Turn left
	angle_rotate(Degrees);
}



void right_degrees(unsigned int Degrees)
{
	// 88 pulses for 360 degrees rotation 4.090 degrees per count
	right(); //Turn right
	angle_rotate(Degrees);
}


void soft_left_degrees(unsigned int Degrees)
{
	// 176 pulses for 360 degrees rotation 2.045 degrees per count
	soft_left(); //Turn soft left
	Degrees=Degrees*2;
	angle_rotate(Degrees);
}

void soft_right_degrees(unsigned int Degrees)
{
	// 176 pulses for 360 degrees rotation 2.045 degrees per count
	soft_right();  //Turn soft right
	Degrees=Degrees*2;
	angle_rotate(Degrees);
}

void soft_left_2_degrees(unsigned int Degrees)
{
	// 176 pulses for 360 degrees rotation 2.045 degrees per count
	soft_left_2(); //Turn reverse soft left
	Degrees=Degrees*2;
	angle_rotate(Degrees);
}

void soft_right_2_degrees(unsigned int Degrees)
{
	// 176 pulses for 360 degrees rotation 2.045 degrees per count
	soft_right_2();  //Turn reverse soft right
	Degrees=Degrees*2;
	angle_rotate(Degrees);
}





void red1led_on (void)
{
 unsigned char port_restore = 0;
 port_restore = PINJ;
 port_restore = port_restore | 0x40;
 PORTJ = port_restore;
}
void red1led_off (void)
{
 unsigned char port_restore = 0;
 port_restore = PINJ;
 port_restore = port_restore & 0xBF;
 PORTJ = port_restore;
}
void blue1led_on (void)
{
 unsigned char port_restore = 0;
 port_restore = PINJ;
 port_restore = port_restore | 0x80;
 PORTJ = port_restore;
}
void blue1led_off (void)
{
 unsigned char port_restore = 0;
 port_restore = PINJ;
 port_restore = port_restore & 0x7F;
 PORTJ = port_restore;
}
void green1led_on (void)
{
 unsigned char port_restore = 0;
 port_restore = PINJ;
 port_restore = port_restore | 0x10;
 PORTJ = port_restore;
}
void green1led_off (void)
{
 unsigned char port_restore = 0;
 port_restore = PINJ;
 port_restore = port_restore & 0xEF;
 PORTJ = port_restore;
}



void red2led_on (void)
{
 unsigned char port_restore = 0;
 port_restore = PINJ;
 port_restore = port_restore | 0x20;
 PORTJ = port_restore;
}
void red2led_off (void)
{
 unsigned char port_restore = 0;
 port_restore = PINJ;
 port_restore = port_restore & 0xDF;
 PORTJ = port_restore;
}
void blue2led_on (void)
{
 unsigned char port_restore = 0;
 port_restore = PINJ;
 port_restore = port_restore | 0x04;
 PORTJ = port_restore;
}
void blue2led_off (void)
{
 unsigned char port_restore = 0;
 port_restore = PINJ;
 port_restore = port_restore & 0xFB;
 PORTJ = port_restore;
}
void green2led_on (void)
{
 unsigned char port_restore = 0;
 port_restore = PINJ;
 port_restore = port_restore | 0x08;
 PORTJ = port_restore;
}
void green2led_off (void)
{
 unsigned char port_restore = 0;
 port_restore = PINJ;
 port_restore = port_restore & 0xF7;
 PORTJ = port_restore;
}


void buzzer_on (void)
{
 unsigned char port_restore = 0;
 port_restore = PINC;
 port_restore = port_restore | 0x08;
 PORTC = port_restore;
}

void buzzer_off (void)
{
 unsigned char port_restore = 0;
 port_restore = PINC;
 port_restore = port_restore & 0xF7;
 PORTC = port_restore;
}



//Function To Initialize UART0
// desired baud rate:9600
// actual baud rate:9600 (error 0.0%)
// char size: 8 bit
// parity: Disabled
void uart0_init(void)
{
 UCSR0B = 0x00; //disable while setting baud rate
 UCSR0A = 0x00;
 UCSR0C = 0x06;
 UBRR0L = 0x5F; //set baud rate lo
 UBRR0H = 0x00; //set baud rate hi
 UCSR0B = 0x98;
}



//Function to initialize all the devices
void init_devices()
{
	cli(); //Clears the global interrupt
	port_init();  //Initializes all the ports
	left_position_encoder_interrupt_init();
	right_position_encoder_interrupt_init();

        timer5_init();
        uart0_init(); //Initailize UART1 for serial communiaction

	sei();   // Enables the global interrupt
}




// Timer 5 initialized in PWM mode for velocity control
// Prescale:256
// PWM 8bit fast, TOP=0x00FF
// Timer Frequency:225.000Hz
void timer5_init()
{
	TCCR5B = 0x00;	//Stop
	TCNT5H = 0xFF;	//Counter higher 8-bit value to which OCR5xH value is compared with
	TCNT5L = 0x01;	//Counter lower 8-bit value to which OCR5xH value is compared with
	OCR5AH = 0x00;	//Output compare register high value for Left Motor
	OCR5AL = 0xFF;	//Output compare register low value for Left Motor
	OCR5BH = 0x00;	//Output compare register high value for Right Motor
	OCR5BL = 0xFF;	//Output compare register low value for Right Motor
	OCR5CH = 0x00;	//Output compare register high value for Motor C1
	OCR5CL = 0xFF;	//Output compare register low value for Motor C1
	TCCR5A = 0xA9;	/*{COM5A1=1, COM5A0=0; COM5B1=1, COM5B0=0; COM5C1=1 COM5C0=0}
 					  For Overriding normal port functionality to OCRnA outputs.
				  	  {WGM51=0, WGM50=1} Along With WGM52 in TCCR5B for Selecting FAST PWM 8-bit Mode*/
	
	TCCR5B = 0x0B;	//WGM12=1; CS12=0, CS11=1, CS10=1 (Prescaler=64)
}

// Function for robot velocity control
void velocity (unsigned char left_motor, unsigned char right_motor)
{
	OCR5AL = (unsigned char)left_motor;
	OCR5BL = (unsigned char)right_motor;
}








SIGNAL(SIG_USART0_RECV) 		// ISR for receive complete interrupt
{
	data = UDR0; 				//making copy of data from UDR0 in 'data' variable 

	UDR0 = data; 				//echo data back to PC

		
                if(data == 0x61) //ASCII value of a
                {
                        red1led_on();
                }
                if(data == 0x62) //ASCII value of b
                {
                        red1led_off();
                }
                if(data == 0x63) //ASCII value of c
                {
                        blue1led_on();
                }
                if(data == 0x64) //ASCII value of d
                {
                        blue1led_off();
                }
                if(data == 0x65) //ASCII value of e
                {
                        green1led_on();
                        red1led_on();
                }
                if(data == 0x66) //ASCII value of f
                {
                        green1led_off();
                        red1led_off();
                }
                if(data == 0x70) //ASCII value of p
                {
                        red2led_on();
                }
                if(data == 0x71) //ASCII value of q
                {
                        red2led_off();
                }
                if(data == 0x72) //ASCII value of r
                {
                        blue2led_on();
                }
                if(data == 0x73) //ASCII value of s
                {
                        blue2led_off();
                }
                if(data == 0x74) //ASCII value of t
                {
                        green2led_on();
                        red2led_on();
                }
                if(data == 0x75) //ASCII value of u
                {
                        green2led_off();
                        red2led_off();
                }


}





int main(void)
{
	data = UDR0; 				//making copy of data from UDR0 in 'data' variable 

	UDR0 = data; 				//echo data back to PC
        
        init_devices();

	velocity (255, 251); //Set robot velocity here. Smaller the value lesser will be the velocity
						 //Try different valuse between 0 to 255

        while(1)
         {

		if(data == 0x38) //ASCII value of 8
		{
			forward_mm(90); //Moves robot forward 100mm
			stop();
			_delay_ms(700);
		}

		if(data == 0x32) //ASCII value of 2
		{
			back_mm(90);   //Moves robot backward 100mm
			stop();
			_delay_ms(700);
		}

		if(data == 0x34) //ASCII value of 4
		{
			left_degrees(90); //Rotate robot left by 90 degrees
			stop();
			_delay_ms(700);
		}

		if(data == 0x36) //ASCII value of 6
		{
			right_degrees(90); //Rotate robot right by 90 degrees
			stop();
			_delay_ms(700);
		}
		if(data == 0x67) //ASCII value of g
		{
			forward_mm(40); //Rotate robot left by 90 degrees
			stop();
			_delay_ms(500);
		}
		if(data == 0x68) //ASCII value of h
		{
			left_degrees(10); //Rotate robot left by 90 degreesleft_degrees(180);
			stop();
			_delay_ms(500);
		}
		if(data == 0x69) //ASCII value of i
		{
			left_degrees(181); //Rotate robot left by 90 degrees
			stop();
			_delay_ms(500);
		}        
		if(data == 0x35) //ASCII value of 5
		{
			stop();						
		        _delay_ms(500);//stop
		}

		if(data == 0x37) //ASCII value of 7
		{
			buzzer_on();
		}

		if(data == 0x39) //ASCII value of 9
		{
			buzzer_off();
		}
                

}

}







