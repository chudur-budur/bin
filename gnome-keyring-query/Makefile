CC		:= gcc
IFLAGS		:= -I/usr/include/gnome-keyring-1 -I/usr/include/glib-2.0 \
			-I/usr/lib/x86_64-linux-gnu/glib-2.0/include
CFLAGS		:= -lgnome-keyring -lglib-2.0
SRC		:= gnome-keyring-query.c
BIN		:= gnome-keyring-query

.PHONY: clean all

all: $(BIN)

$(BIN): $(SRC)
	$(CC) $(IFLAGS) $< -o $@ $(CFLAGS)

clean:
	rm -f $(BIN)
