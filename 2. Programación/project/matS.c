
// row = [11, 7, 5, 3, 37, 35, 33, 31] # Board
// column = [18, 22, 24, 26, 32, 36, 38, 40] # Board

// row = [17, 4, 3, 2, 26, 19, 13, 6] # GPIO
// column = [24, 25, 8, 7, 12, 16, 20, 21] # GPIO


// Code taken from https://elinux.org/RPi_GPIO_Code_Samples

//  How to access GPIO registers from C-code on the Raspberry-Pi
//  Example program
//  15-January-2012
//  Dom and Gert
//  Revised: 15-Feb-2013

// Access from ARM Running Linux

#define BCM2708_PERI_BASE        0x3F000000
#define GPIO_BASE                (BCM2708_PERI_BASE + 0x200000) /* GPIO controller */

#define _GNU_SOURCE
#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <sys/mman.h>
#include <unistd.h>
#include <stdint.h>
#include <pthread.h>
#include <sched.h>


#define PAGE_SIZE (4*1024)
#define BLOCK_SIZE (4*1024)

int  mem_fd;
void* gpio_map;

// I/O access
volatile unsigned* gpio;


// GPIO setup macros. Always use INP_GPIO(x) before using OUT_GPIO(x) or SET_GPIO_ALT(x,y)
#define INP_GPIO(g) *(gpio+((g)/10)) &= ~(7<<(((g)%10)*3))
#define OUT_GPIO(g) *(gpio+((g)/10)) |=  (1<<(((g)%10)*3))
#define SET_GPIO_ALT(g,a) *(gpio+(((g)/10))) |= (((a)<=3?(a)+4:(a)==4?3:2)<<(((g)%10)*3))

#define GPIO_SET *(gpio+7)  // sets   bits which are 1 ignores bits which are 0
#define GPIO_CLR *(gpio+10) // clears bits which are 1 ignores bits which are 0

#define GET_GPIO(g) (*(gpio+13)&(1<<g)) // 0 if LOW, (1<<g) if HIGH

#define GPIO_PULL *(gpio+37) // Pull up/pull down
#define GPIO_PULLCLK0 *(gpio+38) // Pull up/pull down clock

void setup_io();

// START OF CODE

//#define deployed

const uint8_t r[8] = { 17, 4, 3, 2, 26, 19, 13, 6 }; // GPIO rows
const uint8_t c[8] = { 24, 25, 8, 7, 12, 16, 20, 21 }; // GPIO columns

uint32_t rMask;
uint32_t cMask;

const uint32_t waitTime = (1000000 / 120) / 8 / 10;
const uint32_t lastR[8] = { 7,0,1,2,3,4,5,6 };

volatile uint8_t matrix[8][7] = {};


void allOff() {
	GPIO_CLR = rMask;

#ifdef deployed
	GPIO_CLR = cMask;
#else
	GPIO_SET = cMask;
#endif
}

void columnsOff() {
#ifdef deployed
	GPIO_CLR = cMask;
#else
	GPIO_SET = cMask;
#endif
}

void updateLeds() {
	allOff();
	for (size_t i = 0; i < 8; i++) {
		GPIO_CLR = 1 << r[lastR[i]];
		columnsOff();

		uint32_t mask = matrix[i][0] << c[0] | matrix[i][1] << c[1] | matrix[i][2] << c[2] | matrix[i][3] << c[3] | matrix[i][4] << c[4] | matrix[i][5] << c[5] | matrix[i][6] << c[6];

		GPIO_SET = 1 << r[i]; // Turn on the row

		// Turn on the columns
#ifdef deployed
		GPIO_SET = mask;
#else
		GPIO_CLR = mask;
#endif

		usleep(waitTime);
	}
}

void* updateData(void* ptr) {

	while (1) {
		FILE* matrixData;

		matrixData = fopen("./data/files/matSdata.bin", "r");

		uint8_t buffer[56];
		int dataRead = fread(buffer, 1, 56, matrixData);
		fclose(matrixData);

		if (dataRead == 56) {

			for (size_t i = 0; i < 8; i++) {
				for (size_t j = 0; j < 7; j++) {
					matrix[i][j] = buffer[j + i * 7] & 1;
				}
			}

#ifdef deployed
			matrix[3][0] = matrix[1][1]; // Arreglo
			matrix[2][6] = matrix[1][3]; // Arreglo
#endif

		}

		sleep(1);
	}
}

int main(int argc, char** argv)
{
	// Set up gpi pointer for direct register access
	setup_io();

	rMask = 1 << r[0] | 1 << r[1] | 1 << r[2] | 1 << r[3] | 1 << r[4] | 1 << r[5] | 1 << r[6] | 1 << r[7];
	cMask = 1 << c[0] | 1 << c[1] | 1 << c[2] | 1 << c[3] | 1 << c[4] | 1 << c[5] | 1 << c[6] | 1 << c[7];

	// Set rows and columns to output
	for (size_t i = 0; i < 8; i++) {
		INP_GPIO(r[i]);
		OUT_GPIO(r[i]);
		INP_GPIO(c[i]);
		OUT_GPIO(c[i]);
	}

	allOff();

	pthread_t updateThread;
	pthread_create(&updateThread, NULL, updateData, NULL);

	// Set priorities to avoid flickering
	//nice(-20); // niceness to highest priority // Only with SCHED_OTHER or SCHED_BATCH

	struct sched_param sp = { .sched_priority = 99 };
	sched_setscheduler(0, SCHED_RR, &sp); // scheduler to RR, and highest priority

	cpu_set_t* set;
	set = CPU_ALLOC(1);
	CPU_SET(0, set);
	sched_setaffinity(0, sizeof(set), set); // run only on the cpu 0, which is only running this process
	CPU_FREE(set);

	while (1) {
		updateLeds();
	}

	return 0;

} // main


//
// Set up a memory regions to access GPIO
//
void setup_io()
{
	/* open /dev/mem */
	if ((mem_fd = open("/dev/mem", O_RDWR | O_SYNC)) < 0) {
		printf("can't open /dev/mem \n");
		exit(-1);
	}

	/* mmap GPIO */
	gpio_map = mmap(
		NULL,             //Any adddress in our space will do
		BLOCK_SIZE,       //Map length
		PROT_READ | PROT_WRITE,// Enable reading & writting to mapped memory
		MAP_SHARED,       //Shared with other processes
		mem_fd,           //File to map
		GPIO_BASE         //Offset to GPIO peripheral
	);

	close(mem_fd); //No need to keep mem_fd open after mmap

	if (gpio_map == MAP_FAILED) {
		printf("mmap error %d\n", (int)gpio_map);//errno also set!
		exit(-1);
	}

	// Always use volatile pointer!
	gpio = (volatile unsigned*)gpio_map;


} // setup_io
