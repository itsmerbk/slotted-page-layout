class SlottedPage:
    def __init__(self, size=256): self.buf, self.slots, self.free_end = bytearray(size), [], size
    def insert(self, rec_bytes):
        n = len(rec_bytes)
        if len(self.slots)*4 + 4 + n > self.free_end: raise MemoryError("Page full")
        self.free_end -= n; self.buf[self.free_end:self.free_end+n] = rec_bytes
        self.slots.append((self.free_end, n)); return len(self.slots) - 1
    def read(self, slot_id):
        off, n = self.slots[slot_id]; return bytes(self.buf[off:off+n])

if __name__ == "__main__":
    pg = SlottedPage(128); s0 = pg.insert(b"record-zero")
    assert pg.read(s0) == b"record-zero"
    print("[PASS] 049_slotted_page_layout")
