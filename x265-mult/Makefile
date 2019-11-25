#$(shell cd build/linux ; ./multilib.sh)
.NOTPARALLEL:
all:
	$(shell ./multilib.sh ; cp 8bit/libx265.a . ; cp 8bit/x265.pc . ; cp 8bit/x265_config.h .)
