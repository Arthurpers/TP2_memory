default: all

all: $(TARGET)
	gcc -o $(TARGET) $(TARGET).c -Wall -Werror
