CXXFLAGS = -o

CXX = gcc

OBJS = main.o
SRCS = main.c

TARGET = run.o


all:	$(TARGET)


$(TARGET):	$(OBJS)
	$(CXX) -o $(TARGET) $(OBJS) -lm

debug:
	$(CXX) -D_DEBUG -o $(TARGET) $(SRCS)
	
clean:
	rm -f $(OBJS) $(TARGET)
