#include <stddef.h>
#include <stdio.h>                     /* This ert_main.c example uses printf/fflush */
#include <math.h>

#define PI 3.141592653
#define STEP 0.1

struct cosine_block {
  int cstate;
  double r;
  int k;
  double x_out;
};
struct cosine_block cosine;

// prototypes
void cosine_initialize(void);
void cosine_step(void);
void calc_x_out(void);
void calc_r(void);

void calc_x_out()
{
  cosine.x_out = cos(cosine.r);
}

void calc_r()
{
  if (cosine.cstate == 0)
  {
    cosine.r = cosine.r + 1 * STEP;
  }
  else
  {
    cosine.r = cosine.r + -3 * PI * cosine.k * STEP;
  }
}

void cosine_initialize()
{
  cosine.cstate = 0;
  cosine.r = 0;
  cosine.k = 1;
  cosine.x_out = 0;
  calc_x_out();
}

void cosine_step()
{
    if (cosine.cstate == 0) //LeftTurn state
    {
      calc_r();
      calc_x_out(); 
      if (cos(cosine.r) <= -0.99)
      {
        cosine.cstate = 1;
      }
    }
    else // RightTurn state
    {
      calc_r();
      calc_x_out();
      if (cos(cosine.r) >= 0.99)
      {
        cosine.cstate = 0;
      }
    }
}

int main(int argc, const char *argv[])
{
  static double time = 0;
  int max_time = 10;

  printf(" Time, r, x_out\r\n");
  cosine_initialize();

  while(time <= max_time )
  {
    printf("%f, %f, %f\r\n", time, cosine.r, cosine.x_out );
    cosine_step();
    time = time + STEP;
  }

  return 0;
}